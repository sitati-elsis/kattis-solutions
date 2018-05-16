number_of_inputs = input()
count = 1
while count <= int(number_of_inputs):
    statement = input()
    # find the index of the string where simon is mentioned for the first time
    index = statement.find('Simon')
    # make sure Simon exists in the statement and its the first word uttered
    if index != -1 and index == 0:
        # print the substring after the word Simon says
        print(statement[index+11:])
    count = count + 1