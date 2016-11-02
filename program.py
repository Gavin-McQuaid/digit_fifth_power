sum_of_digits = 0
i = 2
while i < 2000000:
	j = str(i)
	sum_of_powers = 0 
	for l in j:
		sum_of_powers += int(l) ** 5
	if sum_of_powers == i:
		print sum_of_powers
		sum_of_digits += sum_of_powers
		


	i += 1

print sum_of_digits
