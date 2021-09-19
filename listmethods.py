#list1
l1 = [1,6,3,8,5,0,3]
print(l1)

l1.sort() #sort the list
print(l1)

l1.reverse() #reverses the list
print(l1)

l1.append(34) #add at the end of the list
print(l1)

l1.insert(0,544) #insert the number at any given position
print(l1)
l1.insert(2,34)
print(l1)

l1.pop(2) #delete the given position number
print(l1)

l1.remove(3) #remove the given number 
print(l1)

l1.count(1) #count the numbers
print(l1)

book = ['math','english','science']    #add the elements of a list
cars = ['bmw','mercedes','ford','audi']
book.extend(cars)
print(book)

book.clear() #remove the elements from this list
print(book)

x = cars.copy() #returns a copy of the list
print(x)
