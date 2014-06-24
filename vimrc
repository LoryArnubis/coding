set sw=4
set ts=4
set nu
set ai
set hlsearch
set smarttab
syntax on
"set fileencoding=chinese
"let &termencoding=&encoding
"set fileencodings=utf-8,gb18030
set encoding=utf-8 termencoding=utf-8 fileencoding=utf-8

"set cursorline "set under line for cursor

func SetTitle()
    ".sh files"
    if &filetype == 'sh'
        call setline(1,          "\#########################################################################")
        call append(line("."),   "\# File Name: ".expand("%:t"))
        call append(line(".")+1, "\# Author: WangWeilong")
        call append(line(".")+2, "\# Created Time: ".strftime("%c"))
        call append(line(".")+3, "\#########################################################################")
        call append(line(".")+4, "\#!/bin/bash")
        call append(line(".")+5, "")
        call append(line(".")+6, "")
    endif
    if &filetype == 'python'
        call setline(1,          "\#########################################################################")
        call append(line("."),   "\# File Name: ".expand("%:t"))
        call append(line(".")+1, "\# Author: WangWeilong")
        call append(line(".")+2, "\# Company: Baidu")
        call append(line(".")+3, "\#########################################################################")
        call append(line(".")+4, "\#!/home/work/safe_psqa/python/bin/python")
        call append(line(".")+5, "\# coding=utf-8")
        call append(line(".")+6, "")
        call append(line(".")+7, "")
    endif
    if &filetype == 'c'
        call setline(1,          "\/******************************************************************************")
        call append(line("."),   "* Baidu.")
        call append(line(".")+1, "* File Name: ".expand("%:t"))
        call append(line(".")+2, "* Author: WangWeilong Version:   Date:")
        call append(line(".")+3, "* Explanation:")
        call append(line(".")+4, "* Version:")
        call append(line(".")+5, "* Function List:")
        call append(line(".")+6, "* Histroy:")
        call append(line(".")+7, "* <author>      <time>      <version>     <desc>")
        call append(line(".")+8, "* wangweilong")
        call append(line(".")+9, "******************************************************************************/")
        call append(line(".")+10,"#include <stdio.h>")
        call append(line(".")+11,"")
        call append(line(".")+12,"int main(int argc, char **argv)")
        call append(line(".")+13,"{")
        call append(line(".")+14,"    return 0;")
        call append(line(".")+15,"}")
        call append(line(".")+16,"")
    endif
    "makefile files"
    if &filetype == 'make'
    call setline(1,          "obj-m := ")
    call append(line("."),   "PWD := $(shell pwd) ")
    call append(line(".")+1, "#CC := ")
    call append(line(".")+2, "KERNELDIR ?= /lib/modules/2.6.32.12-0.7-default/build")
    call append(line(".")+3, "#KERNELDIR ?= ")
    call append(line(".")+4, "#ARCH ?= ")
    call append(line(".")+5, "#CROSS_COMPILE ?= ")
    call append(line(".")+6, "")
    call append(line(".")+7, "default:")
    call append(line(".")+8, "    $(MAKE) -C $(KERNELDIR) M=$(PWD) modules")
    call append(line(".")+9, "    #$(MAKE) -C $(KERNELDIR) ARCH=$(ARCH) CROSS_COMPILE=$(CROSS_COMPILE) M=$(PWD) modules")
    call append(line(".")+10, "clean:")
    call append(line(".")+11, "    rm -rf *.ko *.o Modules.* *.symvers *.mod.c .*cmd *.order .tmp* *.markers")
    endif
endfunc
    "cursor move to the last line and the end of line when new a file
highlight Comment ctermfg=blue guifg=blue
autocmd BufNewFile  *   call SetTitle()
autocmd BufNewFile * normal G

