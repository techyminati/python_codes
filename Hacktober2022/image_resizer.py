from fileinput import filename
from PIL import Image
import glob
def script():
    print("Welcome to WIXERA-the image master")
    print("1.Image converter")
    print("2.Image resizer")
    print("3.HELP ME")
    main=input("Enter the option for continuing(1/2/3) :")
    if main=='1':
        print("These are the type conversions available")
        print("To start conversion make sure that you upload the requested image here at a time")
        print("1.png to jpg")
        print("2.jpg to png")
        print("3.jpeg to png")
        cn = input("Enter choice for types of coversion(1/2/3):")
        if cn=='1':
            for file in glob.glob("*.png"):
                print("Image selecetd is =",file)
                choice = input("Enter choice for continuation(Y/N):")
                if choice=='Y':
                    im = Image.open(file)
                    rgb_im = im.convert('RGB')
                    rgb_im.save(file.replace("png", "jpg"), quality=95)
                    print ("Executed")
                else:
                    print("Thank you for using me")
        elif cn=='2':
            for file in glob.glob("*.jpg"):
                print("Image selecetd is =",file)
                choice = input("Enter choice for continuation(Y/N):")
                if choice=='Y':
                    im = Image.open(file)
                    rgb_im = im.convert('RGB')
                    rgb_im.save(file.replace("jpg", "png"), quality=95)
                    print ("Executed")
                else:
                    print("Thank your for using me")
        elif cn=='3':
            for file in glob.glob("*.jpeg"):
                print("Image selected is =",file)
                choice=input("Enter the choice for continuation(Y/N):")
                if choice=='Y':
                    im=Image.open(file)
                    rgb_im = im.convert('RGB')
                    rgb_im.save(file.replace("jpeg","png"),quality=95)
                    print ("Executed")
                else:
                    print("Thank You for using me")

        else:
            print("Error occured")
    elif main=='2':
        print("1.For resizing png images")
        print("2.For resizing jpg images")
        print("3.For resizing jpeg images")
        re = input("Enter choice for types of coversion(1/2/3):")
        if re=='1':
            for file in glob.glob("*.png"):
                print("Image selecetd is =",file)
                choice = input("Enter the confirmation(Y/N):")
                if choice=='Y':
                    im = Image.open(file)
                    w=int(input("enter the width :"))
                    h=int(input("enter the height :"))
                    resized_img = im.resize((w,h))
                    resized_img.save("copy.png")
                    print("executed")
                else:
                    print("Thank You")
        elif re=='2':
            for file in glob.glob("*.jpg"):
                print("Image selecetd is =",file)
                choice = input("Enter the confirmation(Y/N):")
                if choice=='Y':
                    im = Image.open(file)
                    w=int(input("enter the width :"))
                    h=int(input("enter the height :"))
                    resized_img = im.resize((w,h))
                    resized_img.save("copy.jpg")
                    print("executed")
                else:
                    print("Thank you")
        elif re=='3':
            for file in glob.glob("*.jpeg"):
                print("Image selected is =",file)
                choice = input("Enter the confirmation (Y/N) :")
                if choice=='Y':
                    im = Image.open(file)
                    w=int(input("enter the width :"))
                    h=int(input("enter the height :"))
                    resized_img = im.resize((w,h))
                    resized_img.save("copy.jpeg")
                    print("executed")
                else:
                    print("Thank you for your confirmation")
        else:
            print("Undefined variable used")
    elif main=='3':
        print("Help is here")
        print("use this resizer wisely")
        print("okay")
    else:
        print("Not matched to any options")
    restart =input("Would you like to continue ")
    if restart == "yes" or restart == "y":
        script()
    if restart == "n" or restart == "no":
        print ("Thank you for using me")
script()