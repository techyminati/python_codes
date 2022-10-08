import os
import sys
print ("==========================================")
print ("      Welcome to PE Sync Script    ")
print ("==========================================")
n=input("Press Y to Continue, N to Exit: ")
if (n=="Y") or (n=="y") :
    print("Starting Sync..")
    print (" Warning: Repo is needed to be installed in prior of running this script)
    branch = input("Enter the branch name to sync: ")
    os.system(f'repo init -u https://github.com/PixelExperience/manifest -b {branch}')
    print ("Starting Repo Sync")
    os.system('repo sync -c --force-sync --optimized-fetch --no-tags --no-clone-bundle --prune -j$(nproc --all)')
else :
    print("Re run script to start sync incase you mistakenly pressed 'N' ")
