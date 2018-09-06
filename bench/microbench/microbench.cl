(defun pisum()(last (loop for j from 1 to 500 collect (loop for k from 1 to 10000 sum (/ 1.0d0 (* k k))))))

(defun bench()
	(let ((start) (stop) (runt) (temp))
		(setq start (get-internal-real-time))
		(setq temp (pisum))
		(setq stop (get-internal-real-time))
		(setq runt (/ (- stop start) internal-time-units-per-second))
		(format t "~f~%" runt)
		(* runt 1.0d0)
	)
) 
	
