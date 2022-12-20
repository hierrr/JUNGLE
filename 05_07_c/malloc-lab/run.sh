#!/bin/bash

# compile
gcc -Wall -O2 -m32 -fsanitize=address mdriver.c mm.c memlib.c fsecs.c fcyc.c clock.c ftimer.c

# run
./a.out #-V
