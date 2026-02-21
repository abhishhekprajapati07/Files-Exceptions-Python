# Task 2: Write and Append Data to a File

try:
    user_input = input("Enter a number: ")

    file = open("output.txt", "w")
    file.write("User entered: " + user_input + "\n")
    file.close()

    file = open("output.txt", "a")
    file.write("This line is appended to the file.\n")
    file.close()

    file = open("output.txt", "r")
    print("\nFinal content of the file:\n")
    print(file.read())
    file.close()

except Exception as e:
    print("Error occurred:", e)
