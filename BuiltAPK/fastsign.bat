@echo off
cd %~dp0
java -jar signapk.jar certificate.pem key.pk8 battlecats.apk battlecats_custom.apk