import os
import os.path

root = os.path.dirname(os.path.realpath(__file__))

for path, subdirs, files in os.walk(root):
    print("->" + path)
    os.system("rm " + path + "/index.html*")