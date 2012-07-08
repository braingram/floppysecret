#!/usr/bin/env python

inFile = "secret.txt"

NLines = 25
attr = 'df'

header = """
entry start
start:
    mov     ax,#0x0600 ; clear screen
    mov     cx,#0x0000
    mov     dx,#0x184f
    mov     bh,#0xdf
    int     0x10
    
    mov     ax,#0x1003
    xor     bx,bx
    int     0x10
    
	mov	DH,#0x00 ; move cursor to start ;dh=row,dl=col
	mov	DL,#0x00
    mov	AH,#0x02
	mov	BH,#0x00
	int	0x10
"""

read_cursor = """
        mov     ah,#0x03                ; read cursor position.
        xor     bh,bh
        int     0x10"""
ascii = """    
        mov     ah,#0x03                ; read cursor position.
        xor     bh,bh
        int     0x10		

        mov     cx,#80			; length of our beautiful string.
        mov     bx,#0x00df              ; page 0, attribute 7 (normal)
        mov     bp,#mymsg
        mov     ax,#0x1301              ; write string, move cursor
        int     0x10"""

#footer = """\nloop1:	jmp	loop1"""

footer = """
    jmp     keyloop

infloop:
    jmp     infloop

clearscreen:
    mov     ax,#0x0600 ; clear screen
    mov     cx,#0x0000
    mov     dx,#0x184f
    mov     bh,#0x0f
    int     0x10
    ret

getkey:
    xor     dl,dl
    mov     ah,#0x00
    int     0x16
    ret

keyloop:
    call    getkey
    cmp     ah, #0x48
    jne     keyloop
    call    getkey
    cmp     ah, #0x48
    jne     keyloop
    call    getkey
    cmp     ah, #0x50
    jne     keyloop
    call    getkey
    cmp     ah, #0x50
    jne     keyloop
    call    getkey
    cmp     ah, #0x4B
    jne     keyloop
    call    getkey
    cmp     ah, #0x4D
    jne     keyloop
    call    getkey
    cmp     ah, #0x4B
    jne     keyloop
    call    getkey
    cmp     ah, #0x4D
    jne     keyloop
    call    getkey
    cmp     ah, #0x30
    jne     keyloop
    call    getkey
    cmp     ah, #0x1E
    jne     keyloop
    call    getkey
    cmp     ah, #0x1C
    jne     keyloop
    jmp     ROU

ROU:
    call    clearscreen
    
    mov     DH,#12 ; move cursor to start ;dh=row,dl=col
	mov     DL,#35
    mov     AH,#0x02
	mov     BH,#0x00
	int     0x10
    
    mov     ah,#0x03 ; read cursor position.
    xor     bh,bh
    int     0x10
    
    mov     cx,#11
    mov     bx,#0x000f
    mov     bp,#mymsg
    mov     ax,#0x1301
    int     0x10
    
    mov     DH,#13 ; move cursor to start ;dh=row,dl=col
	mov     DL,#28
    mov     AH,#0x02
	mov     BH,#0x00
	int     0x10
    
    mov     ah,#0x03 ; read cursor position.
    xor     bh,bh
    int     0x10
    
    mov     cx,#25
    mov     bx,#0x000f
    mov     bp,#rebootmsg
    mov     ax,#0x1301
    int     0x10    
    
    call    getkey
    int     0x19

mymsg:
    .ascii "Grow up :-)"
rebootmsg:
    .ascii "Press the any key to exit"
"""

if __name__ == "__main__":
    print header
    
    iF = open(inFile, 'r')
    
    for i in xrange(NLines):
        print "    mov ah,#0x03"
        print "    xor bh,bh"
        print "    int 0x10"
        if i < NLines-1:
            print "    mov cx,#80"
        else:
            print "    mov cx,#79"
        print "    mov bx,#0x00%s" % attr
        print "    mov bp,#line%i" % i
        if i < NLines-1:
            print "    mov ax,#0x1301"
        else:
            print "    mov ax,#0x1300"
        print "    int 0x10"

    print footer

    for i in xrange(NLines):
        print "line%i:" % i
        if i < NLines-1:
            print ' .ascii "%s"' % iF.readline().strip('\n')[:80]
        else:
            print ' .ascii "%s"' % iF.readline().strip('\n')[:79]
        #print " .byte 13,10"
