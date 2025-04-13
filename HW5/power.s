	.file	"power.c"
	.text
	.globl	_calc_power
	.def	_calc_power;	.scl	2;	.type	32;	.endef
_calc_power:
START_FUNC:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$16, %esp
	movl	$1, -4(%ebp)         # result = 1
	movl	$0, -8(%ebp)         # counter = 0
	jmp	CHECK_LOOP

LOOP_BODY:
	movl	-4(%ebp), %eax
	imull	8(%ebp), %eax        # result *= base
	movl	%eax, -4(%ebp)
	addl	$1, -8(%ebp)         # counter++

CHECK_LOOP:
	movl	-8(%ebp), %eax
	cmpl	12(%ebp), %eax       # counter < exponent
	jl	LOOP_BODY
	movl	-4(%ebp), %eax        # return result
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc

	.section .rdata,"dr"
MSG:
	.ascii "The answer is: %d\12\0"

	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
MAIN_ENTRY:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$3, 4(%esp)
	movl	$2, (%esp)
	call	_calc_power
	movl	%eax, 4(%esp)
	movl	$MSG, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
