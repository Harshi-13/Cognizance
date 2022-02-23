# Question-5
# Print the following pattern.

def printstarpyramind(row):
    # First for creating spaces
    H = row - 1

    # Second,y create outer loop for the number of rows
    for i in range(0, row):

        # Then create inner loop to give the spaces
        for a in range(0, H):
            print(end=" ")

        # Finally decrement H after every loop
        H = H - 1

        # inner loop for the number of columns
        for a in range(0, i + 1):
            # this will print stars
            print("* ", end="")

        # ending line after every row
        print("\r")


# Given number of rows = 5
row = 5
printstarpyramind(row)
