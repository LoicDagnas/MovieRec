CC = g++ -std=c++11
OCC = ./pickling_tools/
OC = $(OCC)opencontainers_1_8_2
OCINC = $(OC)/include

CFLAGS = -Wall -Wextra -fpic -O -fno-strict-aliasing -DLINUX_ -DOC_NEW_STYLE_INCLUDES -Wno-deprecated -I$(OCINC) -pthread -D_REENTRANT

CCFLAGS = -pthread $(CFLAGS)

all: main
.cpp.o:
	$(CC) $(CFLAGS) -c $<

main :  main.o 
	$(CC) $(CCFLAGS) main.o -o main

clean :
	$(info Cleaning.. )
	rm -rf *.o *.so *~ main
