import os.path, time
import pathlib

file = pathlib.Path('emojis.py')
print('Modified : ', time.ctime(os.path.getmtime(file)))
print('created : ', time.ctime(os.path.getctime(file)))
