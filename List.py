my_list = [1, 2, 3, 4, 5]


# List operations

#indexing
print(my_list[0]) # 1
#neg indexing
print(my_list[-1]) # 5

#slicing
print(my_list[1:3]) # [2, 3]
print(my_list[:3]) # [1, 2, 3]
print(my_list[2:]) # [3, 4, 5]

#concatenation
new_list = [6, 7, 8, 9, 10]
print(my_list + new_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#inplace output same variable ei thake
#inplace na hole variable a assign kore rakhte hoy.

#removing elements
my_list.remove(3) # [1, 2, 4, 5]

#appending elements
my_list.append(6) # [1, 2, 4, 5, 6]

#inserting elements
my_list.insert(2, 3) # [1, 2, 3, 4, 5, 6]

#reversing elements
my_list.reverse() # [6, 5, 4, 3, 2, 1]

#sorting elements
my_list.sort() # [1, 2, 3, 4, 5, 6]

#sorting in descending order
my_list.sort(reverse=True) # [6, 5, 4, 3, 2, 1]

# string array sort
my_list = ['john', 'doe', 'jane']
my_list.sort() # ['doe', 'jane', 'john']

# lexographical sort

# change