a = [3, 2, 2, 4]
for i in a[:]:
	if i % 2 == 0:
		a.remove(i)
print(a)
