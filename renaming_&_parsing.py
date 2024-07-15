import os

print(dir(os))

os.chdir("D:/Python course/renme_file")


for f in os.listdir():
    f_name, f_ext =os.path.splitext(f)

    title, desc, num = f_name.split("-")

    num = num.strip()[1:].zfill(2)

    # print("{}-{}-{}".format(num, title, f_ext))
    new_name_structure ="{}-{}{}".format(num, title, f_ext)
    os.rename(f, new_name_structure)

