import os

_dir="D:\\30DaysML\\fifthday\dataset"
name=input("Enter Folder Name")
_dir=os.path.join(_dir,name)
if not os.path.exists(_dir):
    os.makedirs(_dir)