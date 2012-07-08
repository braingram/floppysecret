#include <sys/types.h> /* unistd.h needs this */
#include <unistd.h>    /* contains read/write */
#include <fcntl.h>

int main()
{
                char boot_buf[512];
                int floppy_desc, file_desc;

                file_desc = open("./bsect", O_RDONLY);

                read(file_desc, boot_buf, 510);
                close(file_desc);

                boot_buf[510] = 0x55;
                boot_buf[511] = 0xaa;

                floppy_desc = open("./boot.img", O_RDWR | O_CREAT);

                lseek(floppy_desc, 0, SEEK_SET);
                write(floppy_desc, boot_buf, 512);

                // second segment
                char second_buf[8192];

                file_desc = open("./sect2", O_RDONLY);
                read(file_desc, second_buf, 8192);
                close(file_desc);

                lseek(floppy_desc, 512, SEEK_SET);
                write(floppy_desc, second_buf, 8192);

                close(floppy_desc);
}

