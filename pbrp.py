#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) eun0115 ( eun ) <gianpaoloestacio5@gmail.com>
import os
import sys
os.makedirs('pbrp')
os.system('sudo apt update')
os.system('sudo apt upgrade')
os.system('git clone https://github.com/akhilnarang/scripts')
os.chdir('scripts')
os.system('bash setup/android_build_env.sh')
os.chdir('../pbrp')
import time
print ("==========================================================")
print ("      Welcome to PitchBlackRecoveryProject Sync Script    ")
print ("==========================================================")
time.sleep(3)
import time
print ("==========================================================")
print ("              Do you want to sync the Source?             ")
print ("==========================================================")
time.sleep(1)
n=input("Press Y to Continue, N to Exit: ")
if (n=="Y") or (n=="y") :
    print("Starting Sync..")
    print(" Warning: Repo is needed to be installed in prior of running this script")
    os.system('repo init -u git://github.com/PitchBlackRecoveryProject/manifest_pb -b android-11.0')
    print ("Starting Repo Sync")
    os.system('repo sync -c --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j$(nproc --all)')
else :
    import time
    time.sleep(3)
    print("Re-run the script again to start sync incase you mistakenly pressed 'N' ")
     
