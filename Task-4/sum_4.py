# Question-4
# Write a program to check if the given number is a palindrome number.

# Get number from the user.
User_val=int(input("Enter number: "))
# Store value in another variable
temp_no = User_val
# Set reverse value as 0
reverse = 0
# while loop contains the calculation part
while(User_val>0):
    # Method 1
    # ori_digits = User_val%10
    # rev = rev*10 + ori_digits
    # User_val = User_val//10

    # Simplified version of method 1
     reverse = reverse*10 + User_val%10
     User_val = User_val// 10

# If statement to display whether true or false
if(temp_no==reverse):
    print("True")
else:
    print("False")