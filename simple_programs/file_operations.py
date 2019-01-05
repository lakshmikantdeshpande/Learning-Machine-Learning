try:
    f = open("abc.txt", "w")
    f.write("Hello world\n")
    f.write("Bye world\n")
    print("Successfully written data to abc.txt\n\n")
finally:
    f.close()


try:
    print("Reading from abc.txt: \n")
    f = open("abc.txt", "r")
    print(f.read(4))
    print("\nCurrently the cursor is at position", f.tell())
    print("\nSeeking to zeroth position\n")
    f.seek(0)
    print("Entire file:\n", f.read(), "\n")
finally:
    f.close()


try:
    print("Reading with readline() function")
    f = open("abc.txt", "r")
    line = f.readline()
    while len(line) != 0: 
        print(line)
        line = f.readline()
finally:
    f.close()


try: 
    print("Reading with readlines()")
    f = open("abc.txt", "r")
    print(f.readlines())
finally:
    f.close()



