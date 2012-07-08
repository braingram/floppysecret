entry start
start:
    mov ax,#0xb800
    mov es,ax
    seg es
    mov [0],#0x41
    seg es
    mov [1],#0x0f
    seg es
loop1: jmp loop1
