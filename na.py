data = []
count = 0
with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)
print(len(data))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) 
print(sum_len)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('total', len(new),'less than 100') #when finished for loop, start print
print(new[0])



