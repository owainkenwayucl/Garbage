function t = timemat(n, m)
	tic
	X = randn(m, n+1);
	Y = randn(m, 1);
	theta = pinv(X' * X) * X' * Y;
	toc
endfunction
