word = input()
list_of_words = word.split()
removing_duplicates = set(list_of_words)
if len(list_of_words) != len(removing_duplicates):
    print("no")
else:
    print("yes")