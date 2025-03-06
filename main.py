# Open the file in read mode
with open('example.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()

# Print the current contents of the file
print("Current content of the file:")
print(content)

# Open the file in write mode
with open('example.txt', 'w') as file:
    # Write new content to the file
    file.write("This is the new content of the file.")

# Open the file again in read mode to verify the changes
with open('example.txt', 'r') as file:
    # Read the new contents of the file
    new_content = file.read()

# Print the new contents of the file
print("New content of the file:")
print(new_content)