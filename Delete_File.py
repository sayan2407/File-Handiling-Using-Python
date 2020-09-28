import os

ch = int(input("Enter 1 to Delete Folder\nEnter 2 to Delete File\n\nEnter Your Choice : "))
if ch == 1:
    folder = input("Enter Folder Name : ")
    if os.path.exists(folder):
        os.rmdir(folder)
    else:
        print(folder + " does't Exist")
else:
    filename = input("Enter filename you want to delete : ")
    if os.path.exists(filename):
        os.remove(filename)
        print(filename + " Deleted")
    else:
        print("File Does't Exist")
