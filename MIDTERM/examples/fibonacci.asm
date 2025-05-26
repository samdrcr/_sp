; Fibonacci Sequence Calculator
; This program calculates and prints the first 10 Fibonacci numbers

; Initialize first two Fibonacci numbers
LOAD R0 0  ; F(0) = 0
LOAD R1 1  ; F(1) = 1

; Print first two numbers
PRINT R0
PRINT R1

; Initialize counter
LOAD R3 2  ; Start from F(2)
LOAD R4 10 ; Calculate up to F(9)

; Loop start
loop:
    ; Calculate next Fibonacci number: F(n) = F(n-1) + F(n-2)
    MOVE R2 R1  ; R2 = F(n-1)
    ADD R2 R0   ; R2 = F(n-1) + F(n-2) = F(n)
    
    ; Print the new Fibonacci number
    PRINT R2
    
    ; Shift values: R0 = R1, R1 = R2
    MOVE R0 R1
    MOVE R1 R2
    
    ; Increment counter
    LOAD R5 1
    ADD R3 R5
    
    ; Check if we've calculated enough numbers
    SUB R5 R3
    ADD R5 R4
    
    ; If counter < 10, continue loop
    JGT R5 loop
    
    ; Otherwise halt
    HALT
