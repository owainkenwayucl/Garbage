	program fizzbuzz
	implicit none
	integer i,j
	do i=1,20
	j=0
	if (mod(i,3) .eq. 0) j = j + 1
	if (mod(i,5) .eq. 0) j = j + 2
	goto (10,20,30),j
	write(*,*) i
	goto 100
10	write(*,*) "       Fizz"
	goto 100
20	write(*,*) "       Buzz"
	goto 100
30	write(*,*) "   Fizzbuzz"
100	continue
	enddo
	end program 
