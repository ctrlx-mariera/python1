# File Creation
try:
    # Create and open 'my_file.txt' in write mode ('w')
    with open('my_file.txt', 'w') as file:
        # Write lines of text to the file
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Line 3 with a mix of text and numbers\n")
    print("File created and written successfully!")
except IOError as e:
    print("Error occurred while creating/writing to the file:", e)
    

# File Reading and Display
try:
    # Open 'my_file.txt' in read mode ('r')
    with open('my_file.txt', 'r') as file:
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print("Error occurred while reading the file:", e)


# File Appending
try:
    # Open 'my_file.txt' in append mode ('a')
    with open('my_file.txt', 'a') as file:
        file.write("Additional line 1\n")
        file.write("Append 123\n")
        file.write("Last line of the file\n")
    print("File appended successfully!")
except IOError as e:
    print("Error occurred while appending to the file:", e)
except Exception as e:
    print("Error occurred:", e)
