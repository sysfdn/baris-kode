level = int(input())

data = list()
for i in reversed(range(1, level+1)):
	data.append(i / (i+1))
print(data)
