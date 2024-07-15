import os

from datetime import datetime

print(os.getcwd())



# mod_time = os.stat('test_file_dir').st_mtime

# print(datetime.fromtimestamp(mod_time))

# print(os.stat('test_file_dir'))


# for dirpath, dirnames, filenames  in os.walk('D:\Python course'):
#     print('current path: ', dirnames)
#     print('directories: ', dirnames)
#     print("files", filenames)

print l(os.environ.get("HOME"))
