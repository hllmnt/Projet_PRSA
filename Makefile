CC = g++
CPPFLAGS = -std=c++11 -Wall -Wextra -Werror -O2
OBJS = obj/solver.o
LIBS = -larmadillo
CXXTESTGEN = cxxtestgen --error-printer

all: $(OBJS) bind

obj/%.o: src_cpp/%.cpp headers/%.h
	$(CC) $(CPPFLAGS) $< -c -o $@ $(LIBS)

bind:
	$(MAKE) -C bindings

test_solver: $(OBJS) obj/test_solver.o
	$(CC) $(CPPFLAGS) $^ -o test/$@ $(LIBS)

obj/test_solver.o: test/test_solver.cpp test/test_solver.h
	$(CC) $(CPPFLAGS) -c $< -o $@

test/test_solver.cpp : test/test_solver.h
	$(CXXTESTGEN) -o $@ $<

.PHONY: all clean

clean:
	rm -f obj/*.o test/test_solver test/test_solver.cpp
	$(MAKE) clean -C bindings
