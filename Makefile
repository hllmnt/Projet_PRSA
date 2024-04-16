CC = g++
CPPFLAGS = -std=c++11 -Wall -Wextra -Werror -O2
OBJS = obj/solver.o
TESTS = test_methods
LIBS = -larmadillo
CXXTESTGEN = cxxtestgen --error-printer

all: $(OBJS)

obj/%.o: src/%.cpp headers/%.h
	$(CC) $(CPPFLAGS) $< -c -o $@

test: $(TESTS)

test_%: $(OBJS) obj/test_%.o
	$(CC) $(CPPFLAGS) $^ -o $@ $(LIBS)
	./$@

obj/test_%.o: test/test_%.cpp test/test_%.h
	$(CC) $(CPPFLAGS) -c $< -o $@

test/test_%.cpp : test/test_%.h
	$(CXXTESTGEN) -o $@ $<

.PHONY: all clean

clean:
	rm -f $(OBJS) $(TESTS)
