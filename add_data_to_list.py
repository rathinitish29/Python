# how to add items to our list
# most common things that we can do with our list and most important
# .append() = to add data in our list , add items in last , we can add only one item at a time 
fruits = []
fruits.append('mango')
fruits.append('banana')
print(fruits) 

#more methods to add data = .insert(position,'data')

fruit1 = ['mango','banana']
fruit1.insert(0,'apple')
print(fruit1)

#how to join(concatinate) two lists
fruit2 = ['a','b']
fruit3= ['apple', 'banana']
#fru = fruit2 + fruit3
#print(fru)
#extend()method = to join two lists
fruit2.extend(fruit3)
print(fruit2)
#append()=list inside list
fruit2.append(fruit3)
print(fruit2)