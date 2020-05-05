FPC=fpc
FPARGS=-Mobjfpc

test.exe: test.pas Makefile
	$(FPC) $(FPARGS) -otest.exe test.pas

clean:
	rm -f test.exe test.o
