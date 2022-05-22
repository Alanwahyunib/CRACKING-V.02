import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from killerp import menu
    menu()
elif bit == '32bit':
    exit('\x1b[1;91m\n\tOpps Your Device Not Supported')
