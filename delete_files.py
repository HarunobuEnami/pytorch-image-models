import glob
import os

files = glob.glob("outputs/*/*/*")

for file in files:
    if "checkpoint-" in file or "last.pth" in file:
        print(file)
        os.remove(file)