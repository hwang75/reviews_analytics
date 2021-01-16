data = []
count = 0
with open ('reviews.txt','r') as f:
	for line in f:
		data.append(line)
# print(len(data))

# print(data[0])

# count words
wc = {} # word_count, declear a blank dict
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 
#双层回圈
for word in wc:
	if wc[word] > 100:
		print(word,wc[word])
print(len(wc))

while True:
	word = input('which do you want to search：')
	print(word,"it appears:", wc[word])




# sum_len = 0
# for d in data:
# 	sum_len = sum_len + len(d) 
# print(sum_len)

# new = []
# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('total', len(new),'less than 100') #when finished for loop, start print
# print(new[0])


# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('total',len(new), 'mention good')
# print(good[0])

# # better way for loop, advanced way: list comprehension
# good = [d for d in data if 'good' in d]:








