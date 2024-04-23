CC = g++
CPPFLAGS = -std=c++11 -Wall -Wextra -Werror -O2
OBJS = obj/solver.o
LIBS = -larmadillo

all: $(OBJS)

obj/%.o: src_cpp/%.cpp headers/%.h
	$(CC) $(CPPFLAGS) $< -c -o $@

.PHONY: all clean

clean:
	rm -f $(OBJS)
