BITS 16
start:
mov	ax,	07c0h
add	ax,	288
mov	ss,	ax
mov	sp,	4096
mov	ax,	07c0h
mov	ds,	ax
mov	si,	text_string
call	print_string
jmp	$
text_string	db	'Hello, world!,	0
print_string:
mov	ah,	0eh
.repeat:
lodsb
cmp	al,	0
je	.done
int	10h
jmp	.repeat
.done:
ret
times	512-($-$$)	db	0
dw	0xaa55

