# Makefile for echo server
#
# If your echo*.c in same directory with csapp.c,
# switch annotation line 10 and line 11.
# And you can use 'make re' in place of 'make clean' and 'make all'

CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -lpthread

ECHO = echoclient echoserveri
#CSAPPD = .
CSAPPD = ..

echoclient.o: echoclient.c $(CSAPPD)/csapp.h
	$(CC) $(CFLAGS) -c echoclient.c -o echoclient.o

echoserveri.o: echoserveri.c $(CSAPPD)/csapp.h
	$(CC) $(CFLAGS) -c echoserveri.c -o echoserveri.o

echoclient: echoclient.o $(CSAPPD)/csapp.o
	$(CC) $(CFLAGS) echoclient.o $(CSAPPD)/csapp.o -o echoclient $(LDFLAGS)

echoserveri: echoserveri.o $(CSAPPD)/csapp.o
	$(CC) $(CFLAGS) echoserveri.o $(CSAPPD)/csapp.o -o echoserveri $(LDFLAGS)

$(CSAPPD)/csapp.o: $(CSAPPD)/csapp.c
	$(CC) $(CFLAGS) -c $(CSAPPD)/csapp.c -o $(CSAPPD)/csapp.o

all: echoclient echoserveri

clean:
	rm -f *.o *~ $(ECHO) $(CSAPPD)/csapp.o

re: clean all

.PHONY: all clean re