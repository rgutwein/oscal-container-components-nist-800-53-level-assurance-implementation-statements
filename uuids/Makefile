CC=gcc
CFLAGS=-Wall -g
BINS=uuidtest

all: $(BINS)

%: %.c
    $(CC) $(CFLAGS) $< -o $0 -luuid
    
Clean
    $(RM) *.o $(BINS)
    
