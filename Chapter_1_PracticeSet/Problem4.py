import os

# Specify the directory path
path = "/"   # Change this to your desired path

# Get and print the contents
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)