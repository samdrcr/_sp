; Factorial Calculator
; This program calculates factorial of a number (5! in this example)

; Initialize number to calculate factorial for
LOAD R0 5  ; Calculate 5!

; Initialize result
LOAD R1 1  ; Start with 1

; Loop start
loop:
    ; Multiply result by current number
    MUL R1 R0
    
    ; Decrement counter
    LOAD R2 1
    SUB R0 R2
    
    ; Check if counter > 0
    JGT R0 loop
    
    ; Print the result
    PRINT R1
    
    ; Halt
    HALT
