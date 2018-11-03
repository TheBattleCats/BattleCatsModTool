#!/usr/bin/env python
import hashlib
import sys
from Crypto.Cipher import AES
import os
import csv
# REEEEEEEEEEEEEE
import re

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def applychecksum(numberfile):
        if numberfile == 0:
            f1md5 = md5(datalocallist)
            f2md5 = md5(datalocalpack)
        elif numberfile == 1:
            f1md5 = md5(imagedatalocallist)
            f2md5 = md5(imagedatalocalpack)
        elif numberfile == 2:
            f1md5 = md5(imagelocallist)
            f2md5 = md5(imagelocalpack)
        elif numberfile == 3:
            f1md5 = md5(maplocallist)
            f2md5 = md5(maplocalpack)
        elif numberfile == 4:
            f1md5 = md5(numberlocallist)
            f2md5 = md5(numberlocalpack)
        elif numberfile == 5:
            f1md5 = md5(reslocallist)
            f2md5 = md5(reslocalpack)
        elif numberfile == 6:
            f1md5 = md5(unitlocallist)
            f2md5 = md5(unitlocalpack)
        if numberfile < 7:
            #Checksums in x86 lib are split to 8 pieces and sorted backwards.
            e1md5 = re.findall('....',f1md5)
            e2md5 = re.findall('....',f2md5)
            offset = 1094758+112*numberfile
            lib86.seek(offset)
            lib86.write(e1md5[0])
            lib86.seek(offset-6)
            lib86.write(e1md5[1])
            lib86.seek(offset-13)
            lib86.write(e1md5[2])
            lib86.seek(offset-20)
            lib86.write(e1md5[3])
            lib86.seek(offset-27)
            lib86.write(e1md5[4])
            lib86.seek(offset-34)
            lib86.write(e1md5[5])
            lib86.seek(offset-41)
            lib86.write(e1md5[6])
            lib86.seek(offset-48)
            lib86.write(e1md5[7])
            offset = 1095573+112*numberfile
            lib86.seek(offset)
            lib86.write(e2md5[0])
            lib86.seek(offset-6)
            lib86.write(e2md5[1])
            lib86.seek(offset-13)
            lib86.write(e2md5[2])
            lib86.seek(offset-20)
            lib86.write(e2md5[3])
            lib86.seek(offset-27)
            lib86.write(e2md5[4])
            lib86.seek(offset-34)
            lib86.write(e2md5[5])
            lib86.seek(offset-41)
            lib86.write(e2md5[6])
            lib86.seek(offset-48)
            lib86.write(e2md5[7])
            offset = 7035275
            lib86.seek(offset+33*numberfile)
            lib86.write(f1md5)
            lib86.seek(offset+33*(7+numberfile)) #+33
            lib86.write(f2md5)
            #lib arm64-v8a
            offset = 5669498
            libarm64.seek(offset+33*numberfile)
            libarm64.write(f1md5)
            libarm64.seek(offset+33*(7+numberfile)) #+33
            libarm64.write(f2md5)
            #lib armeabi
            offset = 5353312
            libarm.seek(offset+36*numberfile)
            libarm.write(f1md5)
            libarm.seek(offset+36*(7+numberfile)) #+36
            libarm.write(f2md5)
            #lib armeabi-v7a
            offset = 5291008
            libarmv7a.seek(offset+40*numberfile)
            libarmv7a.write(f1md5)
            libarmv7a.seek(offset+40*(7+numberfile)) #+40
            libarmv7a.write(f2md5)
            #lib x86_64
            offset = 6124524
            lib86_64.seek(offset+33*numberfile)
            lib86_64.write(f1md5)
            lib86_64.seek(offset+33*(7+numberfile)) #+33
            lib86_64.write(f2md5)
        else:
            print ("You inputted a wrong number.")

if len(sys.argv) != 1:
        print ("Script broke! Please notify me of it." % sys.argv[0])
else:
        my_path = os.path.dirname(__file__)
        #libs
        libarm64_path = os.path.join(my_path, "lib\\arm64-v8a\\libnative-lib.so")
        libarm64 = open(libarm64_path, "r+")
        libarm_path = os.path.join(my_path, "lib\\armeabi\\libnative-lib.so")
        libarm = open(libarm_path, "r+")
        libarmv7a_path = os.path.join(my_path, "lib\\armeabi-v7a\\libnative-lib.so")
        libarmv7a = open(libarmv7a_path, "r+")
        lib86_64_path = os.path.join(my_path, "lib\\x86_64\\libnative-lib.so")
        lib86_64 = open(lib86_64_path, "r+")
        lib86_path = os.path.join(my_path, "lib\\x86\\libnative-lib.so")
        lib86 = open(lib86_path, "r+")
        #Lists and packs
        #
        #DataLocal
        datalocallist = os.path.join(my_path, "assets\\DataLocal.list")
        datalocalpack = os.path.join(my_path, "assets\\DataLocal.pack")
        #ImageDataLocal
        imagedatalocallist = os.path.join(my_path, "assets\\ImageDataLocal.list")
        imagedatalocalpack = os.path.join(my_path, "assets\\ImageDataLocal.pack")
        #ImageLocal
        imagelocallist = os.path.join(my_path, "assets\\ImageLocal.list")
        imagelocalpack = os.path.join(my_path, "assets\\ImageLocal.pack")
        #MapLocal
        maplocallist = os.path.join(my_path, "assets\\MapLocal.list")
        maplocalpack = os.path.join(my_path, "assets\\MapLocal.pack")
        #NumberLocal
        numberlocallist = os.path.join(my_path, "assets\\NumberLocal.list")
        numberlocalpack = os.path.join(my_path, "assets\\NumberLocal.pack")
        #resLocal
        reslocallist = os.path.join(my_path, "assets\\resLocal.list")
        reslocalpack = os.path.join(my_path, "assets\\resLocal.pack")
        #UnitLocal
        unitlocallist = os.path.join(my_path, "assets\\UnitLocal.list")
        unitlocalpack = os.path.join(my_path, "assets\\UnitLocal.pack")
        
        applychecksum(0)
        applychecksum(1)
        applychecksum(2)
        applychecksum(3)
        applychecksum(4)
        applychecksum(5)
        applychecksum(6)