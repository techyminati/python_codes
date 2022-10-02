	#	Program
	# important note : donot open your csv file in computer system. It should remain close.
	# Note 1 : To add new row you must know the last index number. here ld variable gives you last index number , suppose last index number =2
	# Note 2 : after knowing last index number +1 should be added to add new row at new index means 2+1 = 3 index number
	# note 3 : after making change , it should be saved in csv file also
	# note 4 : row should be deleted by id number only , but you can access the row by index number in python , so this statement gives you index number 
	# according to rollno entered by the user. 
import pandas as pd
df = pd.read_csv("d:/myfile.csv") 
print(df)
ch=None
while ch!=0:
    print("\n.....Main Menu....\n")
    print("press 0 to exit...")
    print("press 1 to add new row...")
    print("press 2 to delete row...")
    print("press 3 to update row...") 
    print("press 4 to search row...")
    ch = int(input("enter your choice..."))
    if ch==0:
        pass #do nothing statement
    elif ch==1:
        ld=df.index[-1] # Read Note 11
        rollno=int(input("enter roll no = "))
        name=input("enter student name = ")
        clas=int(input("enter clas  = "))
        section=input("enter section = ")
        physics=int(input("enter marks got in physics = "))
        chemistry=int(input("enter marks got in chemistry = "))
        maths=int(input("enter marks got in maths = "))
        english=int(input("enter marks got in english = "))
        computer=int(input("enter marks got in computer = "))
        total=physics+chemistry+maths+english+computer
        percent=total/5
        df.loc[ld+1]=[rollno,name,clas,section,physics,chemistry,maths,english,computer,total,percent] # Read Note 2 
        df.to_csv("d:/myfile.csv") # Read note 3
        print(df)
    elif ch==2:
        rollno=int(input("enter rollno to delete = "))
        ix=df.loc[df['rollno']==rollno].index.values   # Read note 4
        df.drop(index=ix,inplace=True)
        df.to_csv("d:/myfile.csv")
        print(df)
    elif ch==3:
        ch1=None  # Creating sub menu
        while ch1!=0:
            print("press 0 to return to main menu...")
            print("press 1 to update student name...")
            print("press 2 to update clas ....")
            ch1=int(input("enter your choice = "))
            if ch1==0:
                pass
            elif ch1==1:
                rollno=int(input("enter rollno whose name to be updated = "))
                ix1=df.loc[df['rollno']==rollno].index.values
                print(df.iloc[ix1])
                namenew=input("enter new name = ")
                df.at[ix1,'name']=namenew
                df.to_csv("d:/myfile.csv")
                print(df)
            elif ch1==2:
                rollno1=int(input("enter rollno whose clas to be updated = "))
                ix2=df.loc[df['rollno']==rollno1].index.values
                clasnew=float(input("enter new clas = "))
                print(df.iloc[ix2])
                df.at[ix2,'clas']=clasnew
                df.to_csv("d:/myfile.csv")
                print(df)
    elif ch==4:
        rollno=int(input("enter rollno to search = "))
        ix3=df.loc[df['rollno']==rollno].index.values
        print(df.iloc[ix3])
