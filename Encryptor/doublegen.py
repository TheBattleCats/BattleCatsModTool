#!/usr/bin/env python
import hashlib
import sys
from Crypto.Cipher import AES
import os
import csv
import itertools

def encrypt(key, data):
        hexkey = hashlib.md5()
        keies = "%s"%key
        hexkey.update(keies.encode('utf-8'))
        nice = "%s"%hexkey.hexdigest()[:16]
        meet = nice.encode("latin-1")
        encrypter = AES.new(meet,AES.MODE_ECB)
        return encrypter.encrypt(data)

def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

if len(sys.argv) != 3:
        print ("Usage: %s folder-name" % sys.argv[0])
else:
        path = sys.argv[1]
        foldername = sys.argv[2]
        sortedpath = sorted(os.listdir(path), key=lambda s: s.casefold())
        fileoffset = 0
        totalfile = 0
        listfileplain = ""
        packfileplain = ""
        print ("Generating list file...")
        for filename in sortedpath:
            totalfile += 1
        listfile = open("temp.list","w")
        listfile.write(str(totalfile))
        listfile.write(chr(0x0a))
        for filename in sortedpath:
            filesize = os.path.getsize("%s/%s" % (path, filename))
            listfile.write("%s,%s,%s" % (filename, str(fileoffset), str(filesize)))
            listfile.write(chr(0x0a))
            fileoffset += filesize
        my_path = os.path.dirname(__file__)
        listfile.close()
        listfilepath = os.path.join(my_path, "temp.list")
        listfilesize = os.path.getsize(listfilepath)
        newlistfile = open("temp.list","a")
        bytestoaddtolistfile = listfilesize%16
        if bytestoaddtolistfile == 0:
            truebytes = 16
        else:
            truebytes = 16-bytestoaddtolistfile
        for _ in itertools.repeat(None, truebytes):
            newlistfile.write(chr(0x00))
        newlistfile.close()
        newerlistfile = open("temp.list","rb")
        newestlistfile = open("%s.list" % (foldername),"wb")
        listfileencrypted = encrypt("pack", newerlistfile.read())
        newestlistfile.write(listfileencrypted)
        newerlistfile.close()
        newestlistfile.close()
        os.remove("temp.list")
        print ("Generating pack file...")
        rawpackfile = open("temp.pack","wb+")
        for filename in sortedpath:
            file = open("%s/%s" % (path, filename),"rb")
            readfile = file.read()
            rawpackfile.write(readfile)
        rawpackfile.close()
        rerawpackfile = open("temp.pack","rb")
        ready = rerawpackfile.read()
        if foldername != "ImageDataLocal":
            try:
                    readiest = encrypt("battlecats", ready)
                    packfile = open("%s.pack" % (foldername),"wb")
                    packfile.write(readiest)
                    rerawpackfile.close()
                    os.remove("temp.pack")
                    packfile.close()
            except:
                    print ("----------------------------------\nOne or more of the files is not properly aligned!\nIf you don't know what to do, try reading the aligning data section.\n----------------------------------") 
                    rerawpackfile.close()
                    os.remove("temp.pack")
                    os.remove("%s.list" % (foldername))
        else:
            readiest = ready
            packfile = open("%s.pack" % (foldername),"wb")
            packfile.write(readiest)
            rerawpackfile.close()
            os.remove("temp.pack")
            packfile.close()