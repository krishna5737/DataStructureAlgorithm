test_array = [1,3,5,2,4,7,0]
print("Original Array ->",test_array)

#######################
##### Buuble Sort #####
#######################

a = [int(x) for x in test_array]
for i in range(len(a)):
	for j in range(i,len(a)):
		if(a[i] > a[j]):
			(a[i],a[j]) = (a[j],a[i])

print("Bubble Sort ->",a)

##########################
##### Selection Sort #####
##########################
a = [int(x) for x in test_array]
for i in range(len(a)):
	min_index = i
	for j in range(i+1,len(a)):
		if(a[j]<a[min_index]):
			min_index  = j
		(a[i],a[min_index])=(a[min_index],a[i])
print("Selection Sort ->",a)

##########################
##### Insertion Sort #####
##########################

for i in range(1,len(a)):
	key = a[i]
	j = i-1
	while(j>=0 and key<a[j]):
		a[j+1] = a[j]
		j =j-1
	a[j+1] = key
print("Insertion Sort ->",a)
