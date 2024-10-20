first download android studio and run the emulator
then download app on emulator
for use this script you have keep the emulator open
if you want to use adb command in terminal, you need to add the path of adb to the terminal
open the terminal run nano ~/.bash_profile and add the path to the end of the file to let terminal use adb command
export PATH=$PATH:/Users/user_name/Library/Android/sdk/platform-tools then save and exit

to find the package name of the app run adb shell pm list packages | grep app_name
alternatively you can open play store and search for the app and copy the package name from the url it will be like this https://play.google.com/store/apps/details?id=com.app_name& -- package name is com.app_name
----------------------------------------------------------
for finding the path and pulling the package manuelly on terminal
adb shell pm path package_name -- this command will give you the path of the app
adb pull /data/app/~~uvOG09iJen7lE_gFJOXyZA==/com.opera.browser--mSDvOBBbz_V4dwx5JfaLQ==/base.apk ~/Downloads/opera_base.apk