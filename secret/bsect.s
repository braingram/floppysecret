LOC1=0x500

entry start
start:
        mov ax,#LOC1
        mov es,ax
        mov bx,#0 ;segment offset
        mov dl,#0 ;drive no.
        mov dh,#0 ;head no.
        mov ch,#0 ;track no.
        mov cl,#2 ;sector no.( 1..18 )
        mov al,#10 ;no. of sectors tranferred
        mov ah,#2 ;function no.
        int 0x13
	
	jmpi 0,#LOC1

