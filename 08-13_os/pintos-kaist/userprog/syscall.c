#include "userprog/syscall.h"
#include <stdio.h>
#include <syscall-nr.h>
#include "threads/interrupt.h"
#include "threads/thread.h"
#include "threads/loader.h"
#include "userprog/gdt.h"
#include "threads/flags.h"
#include "intrinsic.h"
/* project 2 */
#include "filesys/filesys.h"
#include "filesys/file.h"
#include "threads/palloc.h"
#include "threads/vaddr.h"
#include "userprog/process.h"
/* project 2 */

void syscall_entry (void);
void syscall_handler (struct intr_frame *);
/* project 2 */
// sys call fn
void halt (void);
void exit (int status);
tid_t fork (const char *thread_name, struct intr_frame *if_);
int exec (const char *file_name);
int wait (tid_t tid);
bool create(const char *file, unsigned initial_size);
bool remove(const char *file);
int open(const char *file);
int filesize(int fd);
int read(int fd, void *buffer, unsigned size);
int write(int fd, const void *buffer, unsigned size);
void seek(int fd, unsigned position);
unsigned tell(int fd);
void close(int fd);
int dup2(int oldfd, int newfd);
// aux fn
void check_address(void *addr);
static struct file *find_file_by_fd(int fd);
int add_file_to_fdt(struct file *file);
void remove_file_from_fdt(int fd);
/* project 2 */

/* System call.
 *
 * Previously system call services was handled by the interrupt handler
 * (e.g. int 0x80 in linux). However, in x86-64, the manufacturer supplies
 * efficient path for requesting the system call, the `syscall` instruction.
 *
 * The syscall instruction works by reading the values from the the Model
 * Specific Register (MSR). For the details, see the manual. */

#define MSR_STAR 0xc0000081         /* Segment selector msr */
#define MSR_LSTAR 0xc0000082        /* Long mode SYSCALL target */
#define MSR_SYSCALL_MASK 0xc0000084 /* Mask for the eflags */

void
syscall_init (void) {
	write_msr(MSR_STAR, ((uint64_t)SEL_UCSEG - 0x10) << 48  |
			((uint64_t)SEL_KCSEG) << 32);
	write_msr(MSR_LSTAR, (uint64_t) syscall_entry);

	/* The interrupt service rountine should not serve any interrupts
	 * until the syscall_entry swaps the userland stack to the kernel
	 * mode stack. Therefore, we masked the FLAG_FL. */
	write_msr(MSR_SYSCALL_MASK,
			FLAG_IF | FLAG_TF | FLAG_DF | FLAG_IOPL | FLAG_AC | FLAG_NT);
	
	/* project 2 */
	lock_init(&file_rw_lock);
	/* project 2 */
}

/* The main system call interface */
void
syscall_handler (struct intr_frame *f UNUSED) {
	// TODO: Your implementation goes here.
	// printf ("system call!\n");
	// thread_exit ();
	/* project 2 */
	// for test
	// printf("\n\n%d\n\n", f->R.rax);
	switch (f->R.rax)
	{
		case SYS_HALT:
			halt();
			break ;
		case SYS_EXIT:
			exit(f->R.rdi);
			break ;
		case SYS_FORK:
			f->R.rax = fork(f->R.rdi, f);
			break ;
		case SYS_EXEC:
			if (exec(f->R.rdi) == -1)
				exit(-1);
			break ;
		case SYS_WAIT:
			f->R.rax = wait(f->R.rdi);
			break ;
		case SYS_CREATE:
			f->R.rax = create(f->R.rdi, f->R.rsi);
			break ;
		case SYS_REMOVE:
			f->R.rax = remove(f->R.rdi);
			break ;
		case SYS_OPEN:
			f->R.rax = open(f->R.rdi);
			break ;
		case SYS_FILESIZE:
			f->R.rax = filesize(f->R.rdi);
			break ;
		case SYS_READ:
			f->R.rax = read(f->R.rdi, f->R.rsi, f->R.rdx);
			break ;
		case SYS_WRITE:
			f->R.rax = write(f->R.rdi, f->R.rsi, f->R.rdx);
			break ;
		case SYS_SEEK:
			seek(f->R.rdi, f->R.rsi);
			break ;
		case SYS_TELL:
			f->R.rax = tell(f->R.rdi);
			break ;
		case SYS_CLOSE:
			close(f->R.rdi);
			break ;
		case SYS_DUP2:
			f->R.rax = dup2(f->R.rdi, f->R.rsi);
			break;
		default:
			exit(-1);
			break ;
	}
	/* project 2 */
}

/* project 2 */
// sys call fn
/* shutdown pintos */
void halt (void)
{
	power_off();
}

/* status exit */
void exit (int status)
{
	struct thread *curr = thread_current();
	curr->exit_status = status;
	printf("%s: exit(%d)\n", thread_name(), status);
	thread_exit();
}

/* fork process */
tid_t fork (const char *thread_name, struct intr_frame *if_)
{
	return (process_fork(thread_name, if_));
}

/* exec process */
int exec (const char *file_name)
{
	check_address(file_name);
	int size = strlen(file_name)+1;
	char *fn_copy = palloc_get_page(PAL_ZERO);
	if (fn_copy == NULL)
		exit(-1);

	strlcpy(fn_copy, file_name, size);
	if (process_exec(fn_copy) == -1)
		return (-1);

	NOT_REACHED();
	return (0);
}

/* call process_wait(wait for tid to die and return exit status) */
int wait (tid_t tid)
{
	return (process_wait(tid));
}

/* create file with name, size */
bool create(const char *file, unsigned initial_size)
{
	check_address(file);
	return (filesys_create(file, initial_size));
}

/* remove file with name, return T/F(success) */
bool remove(const char *file)
{
	check_address(file);
	return (filesys_remove(file));
}

/* return fd if success else -1 */
int open (const char *file)
{
	check_address(file);
	// get fileobj
	struct file *fileobj = filesys_open(file);
	if (fileobj == NULL)
		return (-1);
	// add file to ftd
	int fd = add_file_to_fdt(fileobj);
	if (fd == -1)
		file_close(fileobj);
	return (fd);
}

/* get filesize */
int filesize (int fd)
{
	struct file *fileobj = find_file_by_fd(fd);
	if (fileobj == NULL)
		return (-1);
	return (file_length(fileobj));
}

/* return bytes read actually or -1 if failed */
int read (int fd, void *buffer, unsigned size)
{
	check_address(buffer);
	int ret;

	struct file *fileobj = find_file_by_fd(fd);
	if (fileobj == NULL)
		return (-1);

	struct thread *curr = thread_current();

	if (fileobj == STDIN_FILEOBJ)
	{
		if (curr->stdin_cnt == 0)
		{
			NOT_REACHED();
			remove_file_from_fdt(fd);
			ret = -1;
		}
		else
		{
			for (ret = 0; ret < size; ret++)
			{
				unsigned char c = input_getc();
				((unsigned char *)buffer)[ret] = c;
				if (c == '\0')
					break ;
			}
		}
	}
	else if (fileobj == STDOUT_FILEOBJ)
		ret = -1;
	else
	{
		lock_acquire(&file_rw_lock);
		ret = file_read(fileobj, buffer, size);
		lock_release(&file_rw_lock);
	}
	return (ret);
}

/* return bytes written actually or -1 if failed */
int write (int fd, const void *buffer, unsigned size)
{
	check_address(buffer);
	int ret;

	struct file *fileobj = find_file_by_fd(fd);
	if (fileobj == NULL)
		return (-1);

	struct thread *curr = thread_current();

	if (fileobj == STDIN_FILEOBJ)
		ret = -1;
	else if (fileobj == STDOUT_FILEOBJ)
	{
		if (curr->stdout_cnt == 0)
		{
			NOT_REACHED();
			remove_file_from_fdt(fd);
			ret = -1;
		}
		else
		{
			putbuf(buffer, size);
			ret = size;
		}
	}
	else
	{
		lock_acquire(&file_rw_lock);
		ret = file_write(fileobj, buffer, size);
		lock_release(&file_rw_lock);
	}
	return (ret);
}

/* set pos to read or write */
void seek (int fd, unsigned position)
{
	struct file *fileobj = find_file_by_fd(fd);
	if (fileobj == NULL || fileobj == STDIN_FILEOBJ || fileobj == STDOUT_FILEOBJ)
		return ;
	file_seek(fileobj, position);
}

/* get pos to read or write */
unsigned tell (int fd)
{
	struct file *fileobj = find_file_by_fd(fd);
	if (fileobj == NULL || fileobj == STDIN_FILEOBJ || fileobj == STDOUT_FILEOBJ)
		return (-1);
	return (file_tell(fileobj));
}

/* close file */
void close (int fd)
{
	// get fileobj
	struct file *fileobj = find_file_by_fd(fd);
	if (fileobj == NULL)
		return ;
	struct thread *curr = thread_current();
	if (fd == 0 || fileobj == STDIN_FILEOBJ)
		curr->stdin_cnt--;
	else if (fd == 1 || fileobj == STDOUT_FILEOBJ)
		curr->stdout_cnt--;
	// remove file from fdt
	remove_file_from_fdt(fd);
	// close file
	if (fd < 2 || fileobj == STDIN_FILEOBJ || fileobj == STDOUT_FILEOBJ)
		return ;
	if (fileobj->dup_cnt == 0)
		file_close(fileobj);
	else
		fileobj->dup_cnt--;
}

/* copy(share file but not open status) oldfd to newfd, return newfd or -1 */
int dup2(int oldfd, int newfd)
{
	struct file *fileobj = find_file_by_fd(oldfd);
	if (fileobj == NULL)
		return (-1);
	struct file *copyobj = find_file_by_fd(newfd);
	if (oldfd == newfd)
		return (newfd);
	
	struct thread *curr = thread_current();
	if (fileobj == STDIN_FILEOBJ)
		curr->stdin_cnt++;
	else if (fileobj == STDOUT_FILEOBJ)
		curr->stdout_cnt++;
	else
		fileobj->dup_cnt++;
	
	close(newfd);
	curr->fd_table[newfd]= fileobj;
	return (newfd);
}

// aux fn
/* check if addr in user seg or exit process */
void check_address(void *addr)
{
	struct thread *curr = thread_current();
	if (addr == NULL || !(is_user_vaddr(addr))
		|| pml4_get_page(curr->pml4, addr) == NULL)
		exit(-1);
}

/* find file with fd */
static struct file *find_file_by_fd(int fd)
{
	struct thread *curr = thread_current();
	if (fd < 0 || fd >= OPEN_MAX)
		return (NULL);
	return (curr->fd_table[fd]);
}

/* add file to fd, return fd */
int add_file_to_fdt(struct file *file)
{
	struct thread *curr = thread_current();
	struct file **fdt = curr->fd_table;

	while (curr->fd < OPEN_MAX && fdt[curr->fd])
		curr->fd++;
	if (curr->fd >= OPEN_MAX)
		return (-1);
	fdt[curr->fd] = file;
	return (curr->fd);
}

/* remove file(fd) from fdt */
void remove_file_from_fdt(int fd)
{
	struct thread *curr = thread_current();
	if (fd < 0 || fd >= OPEN_MAX)
		return ;
	curr->fd_table[fd] = NULL;
}
/* project 2 */