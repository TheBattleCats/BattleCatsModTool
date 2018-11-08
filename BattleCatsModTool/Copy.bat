@echo off
SET version=750
copy checksums\autochecksum%version%.bat Decompiled_APK && copy checksums\autochecksum%version%.py Decompiled_APK
copy Decompiled_APK\assets\DataLocal.list Decryptor && copy Decompiled_APK\assets\DataLocal.pack Decryptor && Decryptor\decrypt.bat
pause

