#  script that creates a new output file called myfile.txt and writes the string
with open('myfile.txt', 'w') as file_obj:
    file_obj.write("Hello file world!\n")


# another script that opens myfile.txt, and reads and prints its contents
with open('myfile.txt', 'r') as file_obj:
    print(file_obj.read())
