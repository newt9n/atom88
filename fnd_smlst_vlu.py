smallest_so_far = None
print('Before' )
for value in [9, 41, 12, 3, 74, 15] :
    if smallest_so_far is None :
        smallest_so_far = value
    elif value < smallest_so_far :
        smallest_so_far = value
    print(smallest_so_far, value)

print('After', smallest_so_far)

#variable 'None' type will fix this (previous value in lesson was -1 - remember capital N!
#absence of a value or lack of a value
#None is a flag value in this scenario!
#None is a nice way to 'prime' a loop

