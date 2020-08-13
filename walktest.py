from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("test"):
    print(dirpath, dirnames, filenames)
    f.extend(filenames)