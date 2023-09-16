print_str: ;;arg in r20
    mov r10 #0

_ps_loop:
    beq _ps_end_loop !r20,r10 #0
    prc !r20,r10
    add r10 r10 #1
    jmp _ps_loop

_ps_end_loop:
    prc #10
    ret

main:

    add r30 r30 #-1
    mov !r30 r31

    mov @300 #83
    mov @301 #97
    mov @302 #108
    mov @303 #117
    mov @304 #116
    mov @305 #0

    mov r20 #300

    cal print_str
    mov r31 !r30
    add r30 r30 #1

    ret

