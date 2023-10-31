#WAP to define read ,search,write
import pickle
def write():
    f=open("b.dat","wb")
    d=[]
    while True:
        r=int(input("enter roll:"))
        n=input("Enter name:")
        m=int(input("enter marks:"))
        l=[r,n,m]
        d.append(l)
        ch=input("Do you want to add more?Y/n")
        if ch in 'Nn':
            break
    pickle.dump(d,f)
    f.close()

def read():
    f=open("b.dat","rb")
    r=pickle.load(f)
    for i in r:
        k=i[0]
        n=i[1]
        m=i[2]
        print(k,n,m)
    f.close()

def search():
    f=open("b.dat","rb")
    x=pickle.load(f)
    r=int(input("Enter roll that is to be searched"))
    c=0
    for i in x:
        if i[0]==r:
            j=i[0]
            n=i[1]
            m=i[2]
            print(j,n,m)
            c=c+1
            break
    if c==0:
        print("roll not found")
    f.close()  
write()
read()
search()
