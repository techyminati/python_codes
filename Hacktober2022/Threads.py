import threading

def ProcessOne():
    while(True):
        print(threading.current_thread().getName(),"is Running")

def ProcessTwo():
    while(True):
        print(threading.current_thread().getName(),"is Running")


T1=threading.Thread(target=ProcessOne,name="Dallas")
T2=threading.Thread(target=ProcessTwo,name='Houston')

T1.start()
T2.start()