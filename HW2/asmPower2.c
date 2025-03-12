#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>

// Hardcoded machine code for power2 function
unsigned char power2_code[] = {
    0x55,                                     // push   %rbp
    0x48, 0x89, 0xe5,                         // mov    %rsp,%rbp
    0x89, 0x7d, 0xfc,                         // mov    %edi,-0x4(%rbp) (store n)
    0xc7, 0x45, 0xf8, 0x01, 0x00, 0x00, 0x00, // movl   $1,-0x8(%rbp) (r = 1)
    0xc7, 0x45, 0xf4, 0x00, 0x00, 0x00, 0x00, // movl   $0,-0xC(%rbp) (i = 0)
    // Loop:
    0x8b, 0x45, 0xf4,       // mov    -0xC(%rbp),%eax (i)
    0x3b, 0x45, 0xfc,       // cmp    -0x4(%rbp),%eax (compare i with n)
    0x7d, 0x0f,             // jge    end
    0x8b, 0x45, 0xf8,       // mov    -0x8(%rbp),%eax (r)
    0xc1, 0xe0, 0x01,       // shl    $1,%eax (r *= 2)
    0x89, 0x45, 0xf8,       // mov    %eax,-0x8(%rbp)
    0x83, 0x45, 0xf4, 0x01, // addl   $1,-0xC(%rbp) (i++)
    0xeb, 0xe8,             // jmp    Loop (go back)
    // End:
    0x8b, 0x45, 0xf8, // mov    -0x8(%rbp),%eax (return r)
    0x5d,             // pop    %rbp
    0xc3              // ret
};

int (*power2)(int);

int main()
{
    // Allocate executable memory
    void *mem = mmap(NULL, sizeof(power2_code), PROT_WRITE | PROT_EXEC, MAP_ANON | MAP_PRIVATE, -1, 0);
    if (mem == MAP_FAILED)
    {
        perror("mmap");
        return 1;
    }
    memcpy(mem, power2_code, sizeof(power2_code));
    power2 = mem;

    // Call the injected function
    int result = power2(3);
    printf("power2(3) = %d\n", result);

    return 0;
}
