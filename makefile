all: scheduler

scheduler: scheduler.cpp
	g++ -std=c++20 -Wall -o scheduler scheduler.cpp

clean:
	rm -f scheduler