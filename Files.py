# In Python, you can read and write from files.
# We've seen that in cyber security, it's common to write a script and import or export it from a file; whether that be as a way to store the output of your script or to import a list of 100's of websites from a file to enumerate.

# Example:

f = open("file_name", "r")
print(f.read())

# Additional Examples:

f = open("demofile1.txt", "a") # Append to an existing file
f.write("The file will include more text..")
f.close()

f = open("demofile2.txt", "w") # Creating and writing to a new file
f.write("demofile2 file created, with this content in!")
f.close()

# THM Exersise

f = open("flag.txt", "r")
print(f.read())

# Result

# THM{F1LE_R3AD}

