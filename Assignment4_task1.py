#Opening a file in Python

try:
    with open("sample.txt", "rt") as fh:
        for line in fh:
            print(line.strip())

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

