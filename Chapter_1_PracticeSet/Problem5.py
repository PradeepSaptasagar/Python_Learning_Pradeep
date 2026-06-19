import os

# Select the directory whose content you want to list
path = "/"

# Use the os module to list the directory content
contents = os.listdir(path)

# Print the contents of the directory
print("Contents of the directory:")
print(contents)