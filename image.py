#!/usr/bin/env python3
import shutil
import os,sys
from PIL import Image
import subprocess
folder = '/home/user/images' #folder that has the images
new_folder = '/home/user/imaged' #folder the images will be copied to
ds = '/home/zizy/imaged/.DS_Store'
#iterate over the files in the folder variable
for filename in os.listdir(folder): 
    full_filename = os.path.join(folder,filename)
    if os.path.isfile(full_filename):
        shutil.copy(full_filename, new_folder) #copy the files to the new folder
# when copying the files a .DS_store file is created, delete it.
subprocess.run(["rm",ds])
#iterate over the files in the new_folder variable
for files in os.listdir(new_folder):
    full_file = os.path.join(new_folder,files)
    if os.path.isfile(full_file):
        img = Image.open(full_file).rotate(270).resize((128,128)) #rotate thand resize the files
        img = img.convert('RGB') #convert the files
        img.save(full_file, 'jpeg') #save the files

