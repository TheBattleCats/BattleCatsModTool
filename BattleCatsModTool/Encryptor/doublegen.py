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
        dotruebytes = 0
        removebytes = 0
        ptruebytes = 0
        sortedpath = sorted(os.listdir(path), key=lambda s: s.casefold())
        fileoffset = 0
        totalfile = 0
        listfileplain = ""
        packfileplain = ""
        print ("Generating list & pack files...")
        for filename in sortedpath:
            totalfile += 1
        listfile = open("temp.list","w")
        listfile.write(str(totalfile))
        listfile.write(chr(0x0a))           
        rawpackfile = open("temp.pack","wb+")
        for filename in sortedpath:
            with open("%s/%s" % (path, filename),"rb") as file:
                if foldername != "ImageDataLocal":
                    breadfile = file.read()
                    file.seek(-1, os.SEEK_END)
                    bytetest = file.read()
                    if bytetest == b'\x00':
                        readfile = breadfile[:-1]
                        removebytes = 1
                        dotruebytes = 1
                    elif bytetest == b'\x01':
                        readfile = breadfile[:-1]
                        removebytes = 1
                        dotruebytes = 1
                    elif bytetest == b'\x02':
                        readfile = breadfile[:-2]
                        removebytes = 2
                        dotruebytes = 1
                    elif bytetest == b'\x03':
                        readfile = breadfile[:-3]
                        removebytes = 3
                        dotruebytes = 1
                    elif bytetest == b'\x04':
                        readfile = breadfile[:-4]
                        removebytes = 4
                        dotruebytes = 1
                    elif bytetest == b'\x05':
                        readfile = breadfile[:-5]
                        removebytes = 5
                        dotruebytes = 1
                    elif bytetest == b'\x06':
                        readfile = breadfile[:-6]
                        removebytes = 6
                        dotruebytes = 1
                    elif bytetest == b'\x07':
                        readfile = breadfile[:-7]
                        removebytes = 7
                        dotruebytes = 1
                    elif bytetest == b'\x08':
                        readfile = breadfile[:-8]
                        removebytes = 8
                        dotruebytes = 1
                    elif bytetest == b'\t':
                        readfile = breadfile[:-9]
                        removebytes = 9
                        dotruebytes = 1
                    elif bytetest == b'\n':
                        superbytetest = file.seek(-2, os.SEEK_END)
                        duperbytetest = file.read()
                        if duperbytetest == b'\n\n':
                            readfile = breadfile[:-10]
                            removebytes = 10
                            dotruebytes = 1
                        else:
                            readfile = breadfile
                            removebytes = 0
                    elif bytetest == b'\x0b':
                        readfile = breadfile[:-11]
                        removebytes = 11
                        dotruebytes = 1
                    elif bytetest == b'\x0c':
                        readfile = breadfile[:-12]
                        removebytes = 12
                        dotruebytes = 1
                    elif bytetest == b'\r':
                        readfile = breadfile[:-13]
                        removebytes = 13
                        dotruebytes = 1
                    elif bytetest == b'\x0e':
                        readfile = breadfile[:-14]
                        removebytes = 14
                        dotruebytes = 1
                    elif bytetest == b'\x0f':
                        readfile = breadfile[:-15]
                        removebytes = 15
                        dotruebytes = 1
                    elif bytetest == b'\x10':
                        readfile = breadfile[:-16]
                        removebytes = 16
                        dotruebytes = 1
                    else:
                        readfile = breadfile
                        removebytes = 0
                    filesizerinos = sys.getsizeof(readfile)-17
                    filesizery = filesizerinos%16
                    rawpackfile.write(readfile)
                    if filesizery == 0:
                        ptruebytes = 16
                    else:
                        ptruebytes = 16-filesizery
                    # I don't know how to automate it properly
                    if ptruebytes == 1:
                        rawpackfile.write(b'\x01')
                    elif ptruebytes == 2:
                        rawpackfile.write(b'\x02')
                        rawpackfile.write(b'\x02')
                    elif ptruebytes == 3:
                        rawpackfile.write(b'\x03')
                        rawpackfile.write(b'\x03')
                        rawpackfile.write(b'\x03')
                    elif ptruebytes == 4:
                        rawpackfile.write(b'\x04')
                        rawpackfile.write(b'\x04')
                        rawpackfile.write(b'\x04')
                        rawpackfile.write(b'\x04')
                    elif ptruebytes == 5:
                        rawpackfile.write(b'\x05')
                        rawpackfile.write(b'\x05')
                        rawpackfile.write(b'\x05')
                        rawpackfile.write(b'\x05')
                        rawpackfile.write(b'\x05')
                    elif ptruebytes == 6:
                        rawpackfile.write(b'\x06')
                        rawpackfile.write(b'\x06')
                        rawpackfile.write(b'\x06')
                        rawpackfile.write(b'\x06')
                        rawpackfile.write(b'\x06')
                        rawpackfile.write(b'\x06')
                    elif ptruebytes == 7:
                        rawpackfile.write(b'\x07')
                        rawpackfile.write(b'\x07')
                        rawpackfile.write(b'\x07')
                        rawpackfile.write(b'\x07')
                        rawpackfile.write(b'\x07')
                        rawpackfile.write(b'\x07')
                        rawpackfile.write(b'\x07')
                    elif ptruebytes == 8:
                        rawpackfile.write(b'\x08')
                        rawpackfile.write(b'\x08')
                        rawpackfile.write(b'\x08')
                        rawpackfile.write(b'\x08')
                        rawpackfile.write(b'\x08')
                        rawpackfile.write(b'\x08')
                        rawpackfile.write(b'\x08')
                        rawpackfile.write(b'\x08')
                    elif ptruebytes == 9:
                        rawpackfile.write(b'\x09')
                        rawpackfile.write(b'\x09')
                        rawpackfile.write(b'\x09')
                        rawpackfile.write(b'\x09')
                        rawpackfile.write(b'\x09')
                        rawpackfile.write(b'\x09')
                        rawpackfile.write(b'\x09')
                        rawpackfile.write(b'\x09')
                        rawpackfile.write(b'\x09')
                    elif ptruebytes == 10:
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                        rawpackfile.write(b'\x0a')
                    elif ptruebytes == 11:
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                        rawpackfile.write(b'\x0b')
                    elif ptruebytes == 12:
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                        rawpackfile.write(b'\x0c')
                    elif ptruebytes == 13:
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                        rawpackfile.write(b'\x0d')
                    elif ptruebytes == 14:
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                        rawpackfile.write(b'\x0e')
                    elif ptruebytes == 15:
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                        rawpackfile.write(b'\x0f')
                    elif ptruebytes == 16:
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                        rawpackfile.write(b'\x10')
                else:
                    readfile = file.read()
                    rawpackfile.write(readfile)
                filesize = os.path.getsize("%s/%s" % (path, filename))
                listfile.write("%s,%s,%s" % (filename, str(fileoffset), str(filesize+ptruebytes-removebytes)))
                listfile.write(chr(0x0a))
                fileoffset += filesize
                if dotruebytes == 1:
                    fileoffset += ptruebytes
                    fileoffset -= removebytes
                    dotruebytes = 0
                else:
                    fileoffset += ptruebytes
        rawpackfile.close()
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