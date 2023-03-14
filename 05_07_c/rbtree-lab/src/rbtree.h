#ifndef _RBTREE_H_
#define _RBTREE_H_

#include <stddef.h>

// node
typedef enum { RBTREE_RED, RBTREE_BLACK } color_t;
typedef int key_t;
typedef struct node_t
{
    color_t color;
    key_t key;
    struct node_t *parent;
    struct node_t *left;
    struct node_t *right;
} node_t;

// tree
typedef struct rbtree
{
    node_t *root;
    node_t *nil;    // for sentinel
} rbtree;

// init, fin
rbtree *new_rbtree(void);
void delete_rbtree(rbtree *);

// ins
node_t *rbtree_insert(rbtree *, const key_t);

// peek
node_t *rbtree_find(const rbtree *, const key_t);
node_t *rbtree_min(const rbtree *);
node_t *rbtree_max(const rbtree *);

// del
int rbtree_erase(rbtree *, node_t *);

// to array
int rbtree_to_array(const rbtree *, key_t *, const size_t);

#endif   // _RBTREE_H_