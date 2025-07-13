#Using if, elif, and else statements in Python
if 1 > 2:
    print('yes')
elif 2 == 4:
    print('maybe')
else:
    print('no')


#for loops
array_example = [1, 4, 7, 18, 23]
for number in array_example:
    print(number)

#while loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1

#range function
for i in range(0, 5, 1):
    print(i)

#List comprehensions
list_comprehension = [x * 2 for x in range(10)]
print('List comprehension:', list_comprehension)

#functions is python
#DOC stings in python within functions very important. Can be accessed using help(function_name)
def square_number(x):
    """Function to return the square of a number."""    
    return x * x
print('Square of 5:', square_number(5))
help(square_number)

#Using map function
sequence = [1, 2, 3, 4, 5]
mapped_sequence = map(square_number, sequence)
mapped_sequence = list(mapped_sequence) #Convert map object to list
print('Mapped sequence:', mapped_sequence)

#Using lambda functions
using_lambda = lambda input: input * 2
print('Using lambda on 5:', using_lambda(5))

#Using map and lambda together
mapped_with_lambda = map(lambda x: x * 2, sequence)
mapped_with_lambda = list(mapped_with_lambda)  # Convert map object to list
print('Mapped with lambda:', mapped_with_lambda)

#Using filter function
fitered_sequence = filter(lambda num : num%2==0, sequence)
fitered_sequence = list(fitered_sequence)  # Convert filter object to list
print('Filtered sequence (even numbers):', fitered_sequence)