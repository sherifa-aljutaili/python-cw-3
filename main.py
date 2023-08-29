
#pt1 
Favorite_animals = ['Dog', 'cat', 'monkey', 'rabbit']
print (Favorite_animals)

print (Favorite_animals[1])

Favorite_animals.remove('monkey')
#or Favorite_animals.pop(2)
print (Favorite_animals)

print('_________________________________________')

#pt2
Favorite_animals.append('duck')
print (Favorite_animals)

for Favorite_animal in Favorite_animals : 
    print(f'-I love {Favorite_animal}s')

print('_________________________________________')

#pt3
numbers = [1, 2, 3, 4, 5]
numbers_sum = 0 

for number in numbers : 
    numbers_sum += number

print(numbers_sum) 

    


