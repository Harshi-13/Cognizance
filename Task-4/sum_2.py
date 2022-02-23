# Question-2
# Write a program to accept a string from the user and display characters, that are present at an even index number.


# Get a string from the user
phrase = input("Enter a string: ")
# Characters that are at an even index number
new_phrase = phrase[1::2]
# Print it
print(new_phrase)