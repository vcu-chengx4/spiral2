def spiralize(size, n=1):
	increment = 0
	diag_one = n
	diag_two = n
	diag_three = n
	diag_four = n
	old_sum =[]
	for x in range(0,size,2):
		diag_one = diag_one+8*increment
		diag_two = diag_one-6*increment
		diag_three = diag_one-4*increment
		diag_four = diag_one-2*increment
		current_sum = diag_one + diag_two + diag_three + diag_four
		old_sum.append(current_sum)
		increment = increment+1
	return(sum(old_sum)-(3*n))
