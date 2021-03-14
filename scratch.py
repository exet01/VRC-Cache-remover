import os
import shutil

userName = input("type your Windows username and press enter...")
VRC_CACHE_FOLDER = "C:/Users/robin/AppData/LocalLow\VRChat\VRChat\Cache-WindowsPlayer"

#Find a way to insert the userName var into the path for deletion

def get_size(start_path = "C:/Users/robin/AppData/LocalLow\VRChat\VRChat\Cache-WindowsPlayer"):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)

            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

print(get_size(), 'bytes')



Join = input('Would you like to delete the folder?\n')
if Join in ['yes', 'Yes']:
    shutil.rmtree(VRC_CACHE_FOLDER)
else:
    print ("Not removed")

input("Done, press any-key to start. Have a nice day. UwU")


