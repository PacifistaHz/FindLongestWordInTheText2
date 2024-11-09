text=input("Enter a string: ")
longestWordLength=0
longestWord=""

dictionary={i:len(i) for i in text.split(" ")}

for i in dictionary:
    if dictionary[i]>longestWordLength:
        longestWordLength=dictionary[i]
        longestWord=i

print("The longest word length: " + str(longestWordLength))
print("The jongest word: " + str(longestWord))
print(dictionary)