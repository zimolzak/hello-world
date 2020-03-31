.PHONY: all clean
all: alex
alex: alex.c
	cc $< -o $@
clean:
	rm -f alex
