#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# (c) CyberJalagam <jaishnavprasad@disroot.org>

import os
import sys
print ("==========================================")
print ("       Android ROM Environment setup      ")
print ("==========================================")
n=input("Press Y to Continue, N to Exit: ")
if (n == "Y") or (n == "y"):
    print("Installing essential packages")
    os.system("sudo apt-get instal adb autoconf automake axel bc bison build-essential ccache clang cmake expat fastboot flex g++ g++-multilib gawk gcc gcc-multilib git gnupg gperf htop imagemagick lib32ncurses5-dev lib32z1-dev libtinfo5 libc6-dev libcap-dev libexpat1-dev libgmp-dev '^liblz4-.*' '^liblzma.*' libmpc-dev libmpfr-dev libncurses5-dev libsdl1.2-dev libssl-dev libtool libxml2 libxml2-utils '^lzma.*' lzop maven ncftp ncurses-dev patch patchelf pkg-config pngcrush pngquant python2.7 python-all-dev re2c schedtool squashfs-tools subversion texinfo unzip w3m xsltproc zip zlib1g-dev lzip libxml-simple-perl apt-utils -y")
    print("Installing repo")
    os.system('sudo curl --create-dirs -L -o /usr/local/bin/repo -O -L https://storage.googleapis.com/git-repo-downloads/repo')
    os.system('sudo chmod a+rx /usr/local/bin/repo')
    print("Build environment is complete!")
else:
    print(" Thank you for using this script!, Run again if you wish to.")