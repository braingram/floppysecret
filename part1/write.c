#include <sys/types.h> /* unistd.h needs this */
#include <unistd.h>    /* contains read/write */
#include <fcntl.h>

int main()
{
        char boot_buf[512];
        int floppy_desc, file_desc;
 
        
        file_desc = open("./boot", O_RDONLY);
        read(file_desc, boot_buf, 510);
        close(file_desc);
        
        boot_buf[510] = 0x55;
        boot_buf[511] = 0xaa;

        floppy_desc = open("./boot.img", O_RDWR | O_CREAT);
        lseek(floppy_desc, 0, SEEK_CUR);
        write(floppy_desc, boot_buf, 512);
        close(floppy_desc);
}
