## 范權榮 111210557 power.c

產生組合語言.s檔
```
gcc -S 0326.c
```
編譯與執行
```
 gcc power.c
 ./a.exe
```
建立目的檔 .o
```
gcc -c power.c
```
使用 objdump 查看反組譯
```
objdump -d power.o
```
```sh
power.o:     file format pe-i386


Disassembly of section .text:

00000000 <_power>:
   0:   55                      push   %ebp
   1:   89 e5                   mov    %esp,%ebp
   3:   83 ec 10                sub    $0x10,%esp
   6:   c7 45 fc 01 00 00 00    movl   $0x1,-0x4(%ebp)
   d:   c7 45 f8 00 00 00 00    movl   $0x0,-0x8(%ebp)
  14:   eb 0e                   jmp    24 <_power+0x24>
  16:   8b 45 fc                mov    -0x4(%ebp),%eax
  19:   0f af 45 08             imul   0x8(%ebp),%eax
  1d:   89 45 fc                mov    %eax,-0x4(%ebp)
  20:   83 45 f8 01             addl   $0x1,-0x8(%ebp)
  24:   8b 45 f8                mov    -0x8(%ebp),%eax
  27:   3b 45 0c                cmp    0xc(%ebp),%eax
  2a:   7c ea                   jl     16 <_power+0x16>
  2c:   8b 45 fc                mov    -0x4(%ebp),%eax
  2f:   c9                      leave  
  30:   c3                      ret

00000031 <_main>:
  31:   55                      push   %ebp
  32:   89 e5                   mov    %esp,%ebp
  34:   83 e4 f0                and    $0xfffffff0,%esp
  37:   83 ec 10                sub    $0x10,%esp
  3a:   e8 00 00 00 00          call   3f <_main+0xe>
  3f:   c7 44 24 04 03 00 00    movl   $0x3,0x4(%esp)
  46:   00 
  47:   c7 04 24 02 00 00 00    movl   $0x2,(%esp)
  4e:   e8 ad ff ff ff          call   0 <_power>
  53:   89 44 24 04             mov    %eax,0x4(%esp)
  57:   c7 04 24 00 00 00 00    movl   $0x0,(%esp)
  5e:   e8 00 00 00 00          call   63 <_main+0x32>
  63:   b8 00 00 00 00          mov    $0x0,%eax
  68:   c9                      leave
  69:   c3                      ret    
  6a:   90                      nop
  6b:   90                      nop
```
範例輸出（部分）
```
objdump -h power.o
```
```sh
power.o:     file format pe-i386

Sections:
Idx Name          Size      VMA       LMA       File off  Algn
  0 .text         0000006c  00000000  00000000  00000104  2**2
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  1 .data         00000000  00000000  00000000  00000000  2**2
                  ALLOC, LOAD, DATA
  2 .bss          00000000  00000000  00000000  00000000  2**2
                  ALLOC
  3 .rdata        00000010  00000000  00000000  00000170  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  4 .rdata$zzz    00000024  00000000  00000000  00000180  2**2
                  CONTENTS, ALLOC, LOAD, READONLY, DATA
  5 .eh_frame     00000058  00000000  00000000  000001a4  2**2
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, DATA   
```
