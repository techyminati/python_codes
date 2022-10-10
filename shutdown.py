import os

#simple script to shutdown the computer

shutdown = input("Do you want to shutdown the computer? (y/n)")

# If the user does want to shutdown their machine, then shut it down, else exit

if shutdown == 'y':
    os.system("shutdown /t /s 1")
else:
    print('You do not want to shutdown the machine, why did you run the script?')