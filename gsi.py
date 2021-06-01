#!/bin/bash
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) TechyMinati ( Aryan Sinha ) <sinha.aryan03@gmail.com>
import os
import sys
print ("==========================================")
print ("      Welcome to sGSI Building Script    ")
print ("==========================================")
n=input("Press Y to Continue, N to Exit: ")
if (n=="Y") or (n=="y") :
    print("Cloning ErfanGSIs Sourcecode")
    print (" Warning: this is a Fork of ErfanGSIs, Adapted for our Usage")
    os.system('git clone --recurse-submodules https://github.com/sinhaaryan03/ErfanGSIs')
    os.system('sudo chmod -R 777 ErfanGSIs')
    print ("Initialising enviroment for GSI Building")
    os.system('cd ErfanGSIs && sudo bash setup.sh')
    print("==========================================")
    print(" Ready to Build GSI")
    print("==========================================")
    os.system('sudo bash assets/gsi.sh')
    print("==========================================")
    print(" GSI Build Successfully, find it On ErfanGSIs/output ")
    print("==========================================")
else:
    print(" Thanks , If you want to restart GSI Building, re-run this script")
