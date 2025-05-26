范權榮 111210557 27/05/2025
; Counter Example
; This program counts from 1 to 10 and prints each number

; Initialize counter in R0
LOAD R0 1

; Loop start
loop:
    ; Print current counter value
    PRINT R0
    
    ; Increment counter
    LOAD R1 1
    ADD R0 R1
    
    ; Check if counter > 10
    LOAD R2 10
    LOAD R3 0
    SUB R3 R0
    ADD R3 R2
    
    ; If counter <= 10, continue loop
    JGT R3 loop
    
    ; Otherwise halt
    HALT
