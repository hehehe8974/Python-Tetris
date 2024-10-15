import os

root = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(root, "assets")
os.chdir(path)

from main import *
