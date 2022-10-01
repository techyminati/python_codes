#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) TechyMinati ( Aryan Sinha ) <sinha.aryan03@gmail.com>
import os
import sys
print ("==========================================")
print ("      Welcome to sGSI Building Script    ")
print ("==========================================")
n=input("Press Y to Proceed, N to Abort: ")
if (n=="Y") or (n=="y") :
    print("Cloning ErfanGSIs Sourcecode")
    print (" Warning: this is a Fork of ErfanGSIs, Adapted for our Usage")
    os.system('git clone --recurse-submodules https://github.com/sinhaaryan03/ErfanGSIs')
    os.system('sudo chmod -R 777 ErfanGSIs')
    import time
    print ("Initialising enviroment for GSI Building")
    time.sleep(5)
    print ("Enviroment Initialised")
    os.system('cd ErfanGSIs && sudo bash setup.sh')
    print("==========================================")
    print(" Are you ready to Build GSI?")
    print("==========================================")
    os.system('sudo bash assets/gsi.sh')
    n=input("Press Y to Proceed, N to Abort: ")
if (n=="Y") or (n=="y") :
    import time
    print("==========================================")
    print(" Initialising to Build GSI")
    print("==========================================")
    time.sleep(5)
    print("==========================================")
    print(" GSI Build Successfully, find it On ErfanGSIs/output ")
    print("==========================================")
else:
    import time
    time.sleep(5)
    print("Thanks for using the Tool")
    print("If you want to restart GSI Building")
    print("re-run this script")