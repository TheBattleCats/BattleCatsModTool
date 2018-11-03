#!/usr/bin/env python
import hashlib
import sys
from Crypto.Cipher import AES
import os
import csv

def decrypt(key, data):
        hexkey = hashlib.md5()
        keies = "%s"%key
        hexkey.update(keies.encode('utf-8'))
        nice = "%s"%hexkey.hexdigest()[:16]
        meet = nice.encode("latin-1")
        decrypter = AES.new(meet,AES.MODE_ECB)
        return decrypter.decrypt(data)

if len(sys.argv) != 3:
        print ("Usage: %s list-file pack-file" % sys.argv[0])
else:
        list_file = sys.argv[1]
        pack_file = sys.argv[2]
        checky = list_file.split("\\")
        check = checky[-1]

        with open(list_file,'rb') as f:
                listfile = f.read()
                
        list_file_data = decrypt('pack', listfile)

        with open(pack_file,'rb') as g:
                packfile = g.read()
                
        pack_file_data = packfile

        file_list = list_file_data.decode().split("\n")
        num_files = int(file_list[0])
        file_list = file_list[1:]
        print ("Decrypting...")

        for i in range(0, num_files):
                file_info = file_list[i].split(",")
                file_name = file_info[0]
                file_offset = int(file_info[1])
                file_size = int(file_info[2])
                file_data = pack_file_data[file_offset:file_offset+file_size]
                if check != "ImageDataLocal.list":
                    myFile = open("%s"%file_name,"wb")
                    Inside = decrypt('battlecats', file_data)
                    myFile.write(Inside)
                    myFile.close()
                else:
                    myFile = open("%s"%file_name,"wb")
                    myFile.write(file_data)
                    myFile.close()