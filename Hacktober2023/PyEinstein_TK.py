# Einsteins Famous Equation (E = mc ^2) or (E = mc squared)
# Ben Woodfield - proving the Power of Python
# Solve one of the greatest physics equations - With a nice GUI
# Tkinter version - NO additional python modules needed to run

# Python 2.7.11 used to write this app
# To run on Python 3....just change (Tkinter) to (tkinter)

import Tkinter as tk # Edit here for Py3
from Tkinter import * # edit here for py3

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        cvt_from = StringVar()
        cvt_to = StringVar()

#        if cvt_from == not.float
#            print('Please Enter A Numerical Value \n(e.g: 2 or 1.9 or 1.99999)')

        def emc2_formula():
            cSpeed = 299792458
            mass = float(cvt_from.get())
            energy = mass*cSpeed**2 
            cvt_to.set("E = %d \nkg*(m/s)2" % energy)
        
        lbl_one = Label(self,text='Enter your Mass \n in Kg',font='freesansbold')
        lbl_one.pack(fill=X)
        
        mass_input = Entry(self, textvariable=cvt_from,relief='sunken',justify='center',width=30,font=14)
        mass_input.pack()
        
        lbl_two = Label(self, text='Click the Calculate button',font='freesansbold')
        lbl_two.pack(fill=X)
        
        btn_one = Button(self,bg='Grey',text='CALCULATE',font='freesansbold',fg='Blue',command=emc2_formula)
        btn_one.pack(fill=X)

        #if cvt_from == str(''):
        #    print('Please Enter A Numerical Value \n(e.g: 2 or 1.9 or 1.99999)')

        lbl_result = Label(self,textvariable=cvt_to,relief='flat',bg='darkGrey',font='freesansbold', fg='Blue')
        lbl_result.pack(fill=BOTH, expand=1)

        lbl_four = Label(self,text='Proving the Power of Python',font='freesansbold')
        lbl_four.pack(fill=X)

        lbl_three = Label(self,text='Result',relief='flat',bg='Grey',font='freesansbold',fg='Blue')
        lbl_three.pack
        
        btn_exit = Button(self,text='Exit',command=quit)
        btn_exit.pack(side=BOTTOM,fill=X)
                
if __name__ == "__main__":
    root = tk.Tk()
    root.title('PyStein - Einsteins E = mc2')
    root.minsize(350,400)
    MainApplication(root).pack(side="top", fill="both", expand=True)
    
    root.mainloop()

