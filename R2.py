numbers = input()
numbers_list = numbers.split()
missing_number = 2*int(numbers_list[1]) - int(numbers_list[0])
print(missing_number)