
try:
#Step1 : Takes user input and writes it to a file named output.txt.
    user_input = input("Enter text to write to the file: ")
    with open("output.txt", "wt") as file:
        file.write(user_input + "\n")

# Step 2: Append additional data
    additional_input = input("Enter additional text to append: ")
    with open("output.txt", "at") as file:
        file.write(additional_input + "\n")

# Step 3: Read and display final content
    print("\nFinal content of the output.txt :")
    with open("output.txt", "rt") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("The file 'output.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

