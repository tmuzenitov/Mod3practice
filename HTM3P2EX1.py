l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
l_repeat = []
for i in range(len(l)):
	val = l[i]
	count = 0
	for j in l:
		if val == j:
		  count += 1
	if count > 1 and val not in l_repeat:
		l_repeat.append(val)
print(l_repeat)