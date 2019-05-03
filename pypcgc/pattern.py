import os
import shutil


def download(repository):
    os.system("git clone {0} pattern".format(repository))
    shutil.rmtree("pattern/.git/")
    files = os.listdir("pattern/")

    for dir_file in files:
        shutil.move("pattern/" + dir_file, ".")

    shutil.rmtree("pattern/")
