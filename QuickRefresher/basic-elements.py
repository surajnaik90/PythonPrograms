#Using strings
variable_name = "Learning python"
print(variable_name)

#Using string methods
variable_name.split(' ')
print(variable_name.upper())

mathematical_operation = 3 + 9
print(mathematical_operation)

#Using power operator
power_operator = 5 ** 6
print(power_operator)

#Data type conversion
int_to_float = float(3)
print(int_to_float)
float_to_int = int(3.14)
print(float_to_int)

array_example = [1, 4, 7, 18, 23]
print('Differnet types of array printing:', array_example[:3], array_example[1:4], array_example[2:])

print('Using parametes {input1} and {input2} in a string'.format(input1=variable_name, input2=mathematical_operation))

#Using boolean operators
boolean_response_true = 1 < 2
boolean_response_false = 3 > 5
print(boolean_response_true, boolean_response_false)

#Using dictionaries
dictionary_example = {
    'what': 'learning python',
    'how': 'using vscode',
}
print(dictionary_example['what'])

#Using dictionary methods
dictionary_example['when'] = 'now'
print('Dictionary after adding "when":', dictionary_example)
dictionary_example.pop('how')  # Remove key 'how'
dictionary_example.items()  # Get all items in the dictionary
dictionary_example.keys()  # Get all keys in the dictionary
dictionary_example.values()  # Get all values in the dictionary

#Using Lists
list_example = [1, 'item2', 2.5, True]
print(list_example)

#List operations
list_example.append('new_item')
print('List after appending:', list_example)
list_example.pop(2)  # Remove item at index 2
print('List after popping index 2:', list_example)

#Using tuples
tuple_example = (1, 'item2', [1,2,3], False)
print(tuple_example)

#Tuple unpacking
tuple_unpacking_example = [(1, 2), (3, 4), (5, 6)]
for a, b in tuple_unpacking_example:
    print(f'Unpacked values: {a}, {b}')

#Using sets
set_example = {1, 1, 2, 2, 2, 2, 3, 4, 5}
print(set_example)

#using in operator
1 in set_example
print('1 is in set_example:', 1 in set_example)

'x' in variable_name
print("'x' is in variable_name:", 'x' in variable_name)