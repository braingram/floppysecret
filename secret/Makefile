all : gen_asm bsect sect2 write boot.img test

gen_asm: gen_asm.py
	python gen_asm.py > sect2.s

bsect	: bsect.o 
	  ld86 -d bsect.o -o bsect

sect2 : sect2.o 
	  ld86 -d sect2.o -o sect2

bsect.o : bsect.s
	    as86 bsect.s -o bsect.o

sect2.o : sect2.s
	    as86 sect2.s -o sect2.o

write : write.c
	cc write.c -o write

boot.img : bsect sect2 write
	./write
	chmod +rw boot.img

test : boot.img
	kvm -fda boot.img

clean :
	rm bsect.o sect2.o bsect sect2 write boot.img


