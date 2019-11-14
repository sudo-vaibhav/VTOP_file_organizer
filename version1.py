import os
import sys
import re
current_folder=os.path.dirname(sys.argv[0])
os.chdir(current_folder)
print(os.getcwd())
files = os.listdir()
pattern = re.compile(r"20[12]\d_(.+)$")
for f in files:
    x = pattern.search(f)
    if x:
        name = x.group(1)
        name = re.sub(r"--+", " ", name)
        name = re.sub("_", " ", name)
        name = re.sub("  +", " ", name)
        os.rename(f, name)
