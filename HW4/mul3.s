.globl mul3
mul3:
    imul %rsi, %rdi  # rdi = rdi * rsi
    imul %rdx, %rdi  # rdi = rdi * rdx
    mov  %rdi, %rax  # Return value in rax
    ret              # Return to caller
