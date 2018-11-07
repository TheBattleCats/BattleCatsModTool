@echo off

copy Encryptor\DataLocal.list Decompiled_APK\assets && copy Encryptor\DataLocal.pack Decompiled_APK\assets

apktool build --output BuiltAPK\battlecats.apk Decompiled_APK

