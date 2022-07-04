import os
import zipfile
cwd = os.getcwd()
zfile = zipfile.ZipFile(file='ppak.pypak')
zfile.extractall(cwd);
os.system("python3 /usr/bin/PyPAK/cache/bin/main.py")


