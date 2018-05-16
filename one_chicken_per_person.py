variables = input()
variable_list = variables.split()
if int(variable_list[0]) > int(variable_list[1]):
    number_of_pieces = int(variable_list[0]) - int(variable_list[1])
    if number_of_pieces > 1:
        print(f"Dr. Chaz needs {number_of_pieces} more pieces of chicken!")
    else:
        print(f"Dr. Chaz needs {number_of_pieces} more piece of chicken!")

else:
    number_of_pieces = int(variable_list[1]) - int(variable_list[0])
    if number_of_pieces > 1:
        print(f"Dr. Chaz will have {number_of_pieces} pieces of chicken left over!")
    else:
        print(f"Dr. Chaz will have {number_of_pieces} piece of chicken left over!")
        