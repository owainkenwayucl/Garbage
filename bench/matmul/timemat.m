function t = timemat(n, m)
	start_t = time();
	X = randn(m, n+1);
	Y = randn(m, 1);
	theta = pinv(X' * X) * X' * Y;
	t = time() - start_t;
endfunction
