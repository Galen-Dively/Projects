[bits 16] ; 16-bit mode is required by bios

[org 0x7C00] ; Bios reads the bootloader at memory adress 0x7C00

start:
    mov si, msg ; point SI register to message
    call print  ; calls the print function
    jmp $

print:
    lodsb ; Load byte from SI Into AL
    or al, al ; check if end of string
    jz done ; if zero return
    mov ah, 0x0E ; perpares the ah register for Bios teletype function
    int 0x10 ; call bios interruot
    jmp print ; repeat for the nect character

done:
    ret

msg db "Hello from bootloader", 0 ;  null terminated string 


times 510-($-$$) db 0 ; pad to 510 bytes required by bios
dw 0xAA55 ; allows bios to know this is bootable