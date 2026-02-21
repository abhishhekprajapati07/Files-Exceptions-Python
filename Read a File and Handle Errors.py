# Task 1: Read a File and Handle Errors

try:
    file = open("sample.txt", "r")
    print("File content:\n")
    
    for line in file:
        print(line.strip())
    
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

except Exception as e:
    print("Some other error occurred:", e)
