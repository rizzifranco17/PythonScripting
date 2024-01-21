for i in range (10):
    print ("Connection cannot be established")

username_list = ["Franco Rizzi", "Malena Espinosa", "Venu", "Lucho"]
username = "Lucho"
for name in username_list:
    if name == username :
        print ("The user is an approved user")
if username == username_list [3]:
    print ("This username is the final one in the list")


system = "OS 3"

patch_schdule = ["March 1st", "April 1st", "September 3rd"]

if system == "OS 1":
    print ("Patch date:", patch_schdule [0])
elif system == "OS 2":
    print ("Patch date:", patch_schdule [1])
elif system == "OS 3":
    print ("Patch date:", patch_schdule [2])
