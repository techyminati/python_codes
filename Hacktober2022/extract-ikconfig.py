#!/usr/bin/env python3

import sys, gzip, zlib

IKCFG = b"IKCFG_ST\037\213\010"

if len(sys.argv) < 2:
    print("Usage: extract-ikconfig.py <path to gz kernel image>")
    exit()

def find_ikcfg_offset(fil):
    read = f.read()
    ret = read.find(IKCFG)
    f.seek(0)
    return ret

with gzip.open(sys.argv[1], 'rb') as f:
    offset = find_ikcfg_offset(f)
    f.seek(offset+8)
    f = f.read() 
    # https://mail.python.org/pipermail/python-bugs-list/2015-May/273371.html
    unzipped = zlib.decompress(f,  zlib.MAX_WBITS|16)
    print(unzipped.decode("utf-8"))
