#Working Directory: Directory we are working currently.

#Relative File Path = ./filename  it will search in the current directory.
# If wanna go one step up in the hirarchy or reverese in directories we use= ../filename
#Absolute File Path: Absolute file path is relative to the root, so it search the file from root
#Relative File Path: It is relative to current working directories- so it depends on where you are and where you trying to get in.
with open("/Users/hclxb/OneDrive/Desktop/my_file.txt") as file:
    contents = file.read()

    print(contents)
