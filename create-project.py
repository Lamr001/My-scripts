import os


def createFile(fileName):
    return open(fileName, "tw", encoding="utf-8").close()


PATH_ROOT = "./src/"
folders = ["template", "style/sass"]

createFile("gulpfile.js")

for folder in folders:

    if folder == folders[0]:

        path = os.path.join(PATH_ROOT, folder)
        os.makedirs(path)
        file = os.path.join(path, "template.pug")
        createFile(file)

    elif folder == folders[1]:

        path = os.path.join(PATH_ROOT, folder)
        os.makedirs(path)
        file = os.path.join(path, "main.sass")
        createFile(file)

    else:

        path = os.path.join(PATH_ROOT, folder)
        os.mkdir(path)

