all : test

boot.o : boot.s
	as86 boot.s -o boot.o

boot : boot.o
	ld86 -d boot.o -o boot

write : write.c
	cc write.c -o write

boot.img : boot write
	./write
	chmod +rw boot.img

build : boot.img

test : boot.img
	kvm -fda boot.img

clean :
	rm boot.img boot.o boot write


