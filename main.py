file_name = input("file name with extension: ")
with open(file_name, 'r') as txt:
    content = txt.read()
    txt.close()

mode = input("open as read/write? (r/w) ")
if mode == 'w':
    mode = input("append/overwrite? (a/o) ")

    if mode == 'o':
        with open(file_name, 'w') as txt:
            txt.write(input("Enter text to write: "))
            txt.close()

    elif mode == 'a':
        with open(file_name, 'a') as txt:
            txt.write(input("Enter text to append, use \\n for new line: ").replace("\\n", "\n"))

elif mode == 'r':
    with open(file_name, 'r') as txt:
        print(txt.read())
        txt.close() 