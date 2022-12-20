/*
 * mm-naive.c - The fastest, least memory-efficient malloc package.
 * 
 * In this naive approach, a block is allocated by simply incrementing
 * the brk pointer.  A block is pure payload. There are no headers or
 * footers.  Blocks are never coalesced or reused. Realloc is
 * implemented directly using mm_malloc and mm_free.
 *
 * NOTE TO STUDENTS: Replace this header comment with your own header
 * comment that gives a high level description of your solution.
 */
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <string.h>

#include "mm.h"
#include "memlib.h"

/*********************************************************
 * NOTE TO STUDENTS: Before you do anything else, please
 * provide your team information in the following struct.
 ********************************************************/
team_t team = {
    /* Team name */
    "team05",
    /* First member's full name */
    "SON",
    /* First member's email address */
    "hieronimus92@gmail.com",
    /* Second member's full name (leave blank if none) */
    "",
    /* Second member's email address (leave blank if none) */
    ""
};

// align size
#define ALIGNMENT (8)
#define ALIGN(size) (((size) + (ALIGNMENT - 1)) & ~0x7)
#define SIZE_T_SIZE (ALIGN(sizeof(size_t)))
// sg, db word and chunk size alignment
#define WSIZE (4)
#define DSIZE (8)
#define CHUNKSIZE (1<<12)
// return max(x, y)
#define MAX(x, y) ((x) > (y) ? (x) : (y))
// pack size and alloc
#define PACK(size, alloc) ((size) | (alloc))
// read or write at addr(p)
#define GET(p) (*(unsigned int *)(p))
#define PUT(p, val) (*(unsigned int *)(p) = (val))
// get size or alloc from addr(p)
#define GET_SIZE(p) (GET(p) & ~0x7)
#define GET_ALLOC(p) (GET(p) & 0x1)
// get hdr, ftr addr from block ptr(bp)
#define HDRP(bp) ((char *)(bp) - WSIZE) // hdr = bp - word
#define FTRP(bp) ((char *)(bp) + GET_SIZE(HDRP(bp)) - DSIZE) // ftr = bp + size - db word
// get prev, next block addr from block ptr(bp)
#define PREV_BLKP(bp) ((char *)(bp) - GET_SIZE((char *)(bp) - DSIZE)) // prev = curr - prev_size
#define NEXT_BLKP(bp) ((char *)(bp) + GET_SIZE((char *)(bp) - WSIZE)) // next = curr + curr_size

// set heap_list
static void *heap_listp = NULL;

// coalesce alloc or free blocks
static void *mm_coalesce(void *bp)
{
    size_t prev_alloc = 0;
    size_t next_alloc = 0;
    size_t size = 0;

    prev_alloc = GET_ALLOC(FTRP(PREV_BLKP(bp)));
    next_alloc = GET_ALLOC(HDRP(NEXT_BLKP(bp)));
    size = GET_SIZE(HDRP(bp));
    if (prev_alloc && next_alloc) // case 1: prev, next alloc
        return (bp);
    else if (prev_alloc && !next_alloc) // case 2: prev alloc, next free >> curr + next
    {
        size += GET_SIZE(HDRP(NEXT_BLKP(bp))); // curr_size + next_size
        PUT(HDRP(bp), PACK(size, 0)); // reset curr_hdr
        PUT(FTRP(bp), PACK(size, 0)); // reset next_ftr
    }
    else if (!prev_alloc && next_alloc) // case 3: prev free, next alloc >> prev + curr
    {
        size += GET_SIZE(HDRP(PREV_BLKP(bp))); // prev_size + curr_size
        PUT(FTRP(bp), PACK(size, 0)); // reset curr_ftr
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0)); // reset prev_hdr
        bp = PREV_BLKP(bp); // bp >> prev
    }
    else // case 4: prev, next free >> prev + curr + next
    {
        size += GET_SIZE(HDRP(PREV_BLKP(bp))) + GET_SIZE(FTRP(NEXT_BLKP(bp))); // prev_size + curr_size + next_size
        PUT(HDRP(PREV_BLKP(bp)), PACK(size, 0)); // reset prev_hdr
        PUT(FTRP(NEXT_BLKP(bp)), PACK(size, 0)); // reset next_ftr
        bp = PREV_BLKP(bp); // bp >> prev
    }
    // memset(bp, 0, size-DSIZE);
    return (bp);
}

// extend additional heap
static void *mm_extend_heap(size_t size)
{
    char *bp = NULL;

    if ((bp = mem_sbrk(size)) == (void *)-1) // size aligned
        return (NULL); // err: mem_sbrk failed(ran out of memory)
    PUT(HDRP(bp), PACK(size, 0)); // new block hdr
    PUT(FTRP(bp), PACK(size, 0)); // new block ftr
    PUT(HDRP(NEXT_BLKP(bp)), PACK(0, 1)); // new block | eplg hdr
    return (mm_coalesce(bp)); // set all new block free
}

/* 
 * mm_init - initialize the malloc package.
 */
int mm_init(void)
{
    if ((heap_listp = mem_sbrk(4 * WSIZE)) == (void *)-1)
        return (-1); // err: mem_sbrk failed(ran out of memory)
    PUT(heap_listp, 0); // alignment padding
    PUT(heap_listp + (1*WSIZE), PACK(DSIZE, 1)); // prlg hdr
    PUT(heap_listp + (2*WSIZE), PACK(DSIZE, 1)); // prlg ftr
    PUT(heap_listp + (3*WSIZE), PACK(0, 1)); // eplg hdr
    heap_listp += (2*WSIZE); // heap_listp >> prlg ftr
    if (mm_extend_heap(CHUNKSIZE) == NULL) // set init heap size
        return (-1); // err: extend heap failed
    return (0);
}

// first fit
static void *mm_find_fit(size_t alloc_size)
{
    void *bp = NULL;

    bp = heap_listp;
    while (GET_SIZE(HDRP(bp)))
    {
        if (!GET_ALLOC(HDRP(bp)) && (GET_SIZE(HDRP(bp)) >= alloc_size))
            return (bp);
        bp = NEXT_BLKP(bp);
    }
    return (NULL); // err: no fit
}

static void mm_place(void *bp, size_t alloc_size)
{
    size_t curr_size = 0;

    curr_size = GET_SIZE(HDRP(bp));
    if (curr_size - alloc_size > 2 * DSIZE) // rest_size >= hdr + ftr
    {
        PUT(HDRP(bp), PACK(alloc_size, 1)); // set new alloc block hdr
        PUT(FTRP(bp), PACK(alloc_size, 1)); // set new alloc block ftr
        bp = NEXT_BLKP(bp); // bp >> next
        PUT(HDRP(bp), PACK(curr_size - alloc_size, 0)); // set rest block hdr
        PUT(FTRP(bp), PACK(curr_size - alloc_size, 0)); // set rest block ftr
    }
    else
    {
        PUT(HDRP(bp), PACK(curr_size, 1)); // not exist rest
        PUT(FTRP(bp), PACK(curr_size, 1)); // not exist rest
    }
}

/* 
 * mm_malloc - Allocate a block by incrementing the brk pointer.
 *     Always allocate a block whose size is a multiple of the alignment.
 */
void *mm_malloc(size_t size)
{
    size_t alloc_size = 0;
    size_t extend_size = 0;
    char *bp = NULL;
    
    if (size == 0)
        return (NULL); // err: alloc unavailable
    alloc_size = ALIGN(size) + DSIZE; // alloc_size = aligned size + hdr + ftr
    if ((bp = mm_find_fit(alloc_size)) != NULL) // first fit found
    {
        mm_place(bp, alloc_size); // alloc at fit
        return (bp);
    }
    extend_size = MAX(alloc_size, CHUNKSIZE); // no fit >> extend heap
    if ((bp = mm_extend_heap(extend_size)) == NULL)
        return (NULL); // err: mm_extend_heap failed(mem_sbrk failed(out of memory))
    mm_place(bp, alloc_size); // alloc at extended
    return (bp);
}

/*
 * mm_free - Freeing a block does nothing.
 */
void mm_free(void *ptr)
{
    size_t size = 0;

    size = GET_SIZE(HDRP(ptr)); // free block size
    PUT(HDRP(ptr), PACK(size, 0)); // hdr: alloc >> free
    PUT(FTRP(ptr), PACK(size, 0)); // ftr: alloc >> free
    mm_coalesce(ptr);
}

// /*
//  * mm_realloc - Implemented simply in terms of mm_malloc and mm_free
//  */
void *mm_realloc(void *ptr, size_t size)
{
    void *new_ptr = NULL;
    size_t cur_size = 0;

    size = ALIGN(size);
    if (!ptr) // case 1: NULL ptr >> malloc
        mm_malloc(size); // err: NULL ptr
    if (!size) // case 2: ZERO size >> free
    {
        mm_free(ptr);
        return (NULL); // err: ZERO size
    }
    cur_size = GET_SIZE(HDRP(ptr)) - DSIZE;
    if (size < cur_size) // case 3: new_size < cur_size >> realloc new_size at cur_mem
    {
        mm_place(ptr, size + DSIZE); // realloc new_size at cur_mem, free next
        return (ptr);
    }
    if (size == cur_size) // case 3-1: new_size = cur_size >> return cur
        return (ptr);
    // case 4: cur_size< new_size < next(free)_size + cur_size >> coalesce, free rest
    if (!GET_ALLOC(HDRP(NEXT_BLKP(ptr))) && (size <= cur_size + GET_SIZE(HDRP(NEXT_BLKP(ptr)))))
    {
        cur_size += GET_SIZE(HDRP(NEXT_BLKP(ptr)));
        PUT(HDRP(ptr), PACK(size + DSIZE, 1));
        PUT(FTRP(ptr), PACK(size + DSIZE, 1)); // coalesce
        PUT(FTRP(NEXT_BLKP(ptr)), PACK(cur_size - size, 0));
        PUT(HDRP(NEXT_BLKP(ptr)), PACK(cur_size - size, 0)); // free rest
        return (ptr);
    }
    new_ptr = mm_malloc(size); // case 4-1: new_size > cur_size >> find fit, realloc
    if (!new_ptr)
        return NULL; // err: malloc failed
    memcpy(new_ptr, ptr, size+DSIZE);
    mm_free(ptr);
    return new_ptr;
}
