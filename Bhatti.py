import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[92;1m ❲\033[97;1m+\033[92;1m❳ Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/Hf6WUhpV822AmZlGM6RA8P')
bhatti=platform.architecture()[0]
if bhatti=="32bit":
    #os.system("clear");exit("\033[91;1m 32Bit Device Not Supported")
    __import__("Bhatti")
elif bhatti=="64bit":
    __import__("Bhatti")
