
entry start
start:
    mov     ah,#0x03                
    xor     bh,bh
    int     0x10

    mov     cx,#26                  
    mov     bx,#0x0007              
    mov     bp,#mymsg
    mov     ax,#0x1301              
    int     0x10

loop1:  jmp     loop1

mymsg:
    .byte  13,10
    .ascii "Handling BIOS interrupts"
