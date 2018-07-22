# from os import listdir
from os.path import isfile, join
from os import path as fpath
from os import walk, makedirs
from PIL import Image
import errno
import shutil

mypath = "E:\-Ext-\osu\Songs"
bakpath = mypath + "\imgbak"
chosencolor = (10, 10, 10)
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
i = 0
j = 0
k = 0
if not fpath.isdir(bakpath): # create folder for backup
    try:
        makedirs(bakpath)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("backup folder exists!")
            raise  # raises the error again

for path, subdirs, files in walk(mypath):
    if not path.startswith(bakpath): # loop directory
        for name in files:
            sname = name.lower()
            if sname.endswith(('.png', '.jpg', '.bmp', '.jpeg')): # check if file is an image
                fullname = join(path, name)
                im = Image.open(fullname)
                if not im.size[0] < 640:
                    print(fullname)
                    print('  width: %d - height: %d' % im.size)
                    i += 1

                    dstdir = join(bakpath, fpath.relpath(path, mypath))

                    try:
                        makedirs(dstdir)
                    except OSError as e:
                        if e.errno != errno.EEXIST:
                            raise  # raises the error again
                    if not fpath.exists(dstdir + "\\" +name) or im.size != (555, 555):
                        shutil.copy(fullname, dstdir)
                        print("Copied")
                        img = Image.new('RGB', (555, 555), chosencolor)
                        ext = "JPEG"
                        if sname.endswith('.png'):
                            ext = "PNG"
                        elif sname.endswith('.bmp'):
                            ext = "BMP"
                        if img.save(fullname, ext):
                            print("Replaced")
                        else:
                            print("Cant replace")

                elif im.size == (555, 555):
                    getcolor = im.getpixel((0,0))
                    print(getcolor)
                    print(chosencolor)
                    if getcolor != chosencolor:

                        img = Image.new('RGB', (555, 555), chosencolor)
                        ext = "JPEG"
                        if sname.endswith('.png'):
                            ext = "PNG"
                        elif sname.endswith('.bmp'):
                            ext = "BMP"
                        img.save(fullname, ext)
                        print("Replaced")
                        k += 1
                    else:
                        print("Blanket")
                        j += 1

print("Total new: " + str(i))
print("Total blank: " + str(j))
print("Total replaced: " + str(k))
