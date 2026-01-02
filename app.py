import os

def createfile(filename):
    try:
        with open(filename, "x") as f:
            print(f"'{filename}' was successfully created! ")

    except FileExistsError:
        print(f"'{filename}' already exists")
    except Exception as E:
        print("an error occurred")


def allfile():
    files = os.listdir()
    if not files:
        print("No Files Found!")
    
    else:
        print("Files are: ")
        for i in files:
            print(i)


def delfile(filename):
    try:
        os.remove(filename)
        print(f"'{filename}' was successfully deleted! ")

    except FileNotFoundError:
        print(f"'{filename}' not found!")
    except Exception as e:
        print("an error occurred")



def readfile(filename):
    try: 
        with open(filename, "r") as f:
            content = f.read()
            print(f" Content of '{filename}' is '{content}'")
    
    except FileNotFoundError:
        print(f"'{filename}' not found!")
    except Exception as e:
        print("an error occurred")
    


def editfile(filename):

    try: 

        with open(filename, "a") as f:

            edit = input("Enter new content: ")
            f.write(edit + "\n ")
            print(f"Content of '{filename}' was updated! ")
    
    except FileNotFoundError:
        print(f"'{filename}' not found!")
    except Exception as e:
        print("an error occurred")

def main():
    while True:
        print("\n----FILE MANAGEMENT SYSTEM----- \n")
        print("Do you want to:  \n")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Edit a file")
        print("4. Delete a file")
        print("5. View all the files")
        print("6. Exit the program")


        a = int(input("Enter number (1-5) to perform the tasks: "))


        if a == 1:
            filename = input("Enter the name of your file: ")
            createfile(filename)

        elif a == 2:
            filename = input("Enter the name of your file: ")
            readfile(filename)

        elif a == 3:
            filename = input("Enter the name of your file: ")
            editfile(filename)

        elif a == 4:
            filename = input("Enter the name of your file: ")
            delfile(filename)

        elif a == 5:
            allfile()


        elif a == 6:
            print("---SYSTEM CLOSED---")
            break
        else:
            print("Enter a valid number!")


if __name__ == "__main__":
    main()