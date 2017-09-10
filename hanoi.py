def hanoi(n, start, via, end):
	if n == 1:
		print(start, '->', end)

	else:
		hanoi(n-1, start, end, via)
		hanoi(1, start, via, end)
		hanoi(n-1, via, start, end)

hanoi(5,'A','B','C')