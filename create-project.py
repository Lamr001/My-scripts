import pdb
import os
import argparse

parser = argparse.ArgumentParser(prog="create-project")
parser.add_argument("-P", "--PATH-ROOT",
                    action="store",
                    default="./",
                    help="Specifies the root directory relative to which files will be created.")

parser.add_argument("-F", "--folders",
                    action="store",
                    nargs="+",
                    default=["src/template/", "src/style/sass/", "src/img/"])

parser.add_argument("-f", "--files",
                    action="store",
                    nargs="+",
                    default=["index.pug", "style.sass"])

parser.add_argument("-r", "--root-files",
                    action="store",
                    nargs="+",
                    default=["gulpfile.js"])

parser.add_argument("-b", "--base-canon",
                    action="store_true")

args = parser.parse_args()



def createFile(filePath):
    return open(filePath, "tw", encoding="utf-8").close()

def createDir(folder):
    path = os.path.join(PATH_ROOT, folder)
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

    return path


PATH_ROOT = args.PATH_ROOT
baseCanon = args.base_canon


if baseCanon:
    foldersArgs = args.folders
    filesArgs = args.files
    rootFilesArgs = args.root_files

    folders = ["src/template/", "src/style/sass/", "src/img/"]
    files = ["index.pug", "style.sass"]
    rootFiles = ["gulpfile.js"]

    folders.extend(foldersArgs)
    files.extend(filesArgs)
    rootFiles.extend(rootFilesArgs)

else:
    folders = args.folders

    files = args.files

    rootFiles = args.root_files



foldersDict = {}
j=0
for directory in folders:
    try:
        filesList = [files[j]]
    except IndexError:
        filesList = None

    foldersDict[directory] = filesList
    j+=1

folderDictKeys = list(foldersDict.keys())





for folder in folderDictKeys:
    pathDir = createDir(folder)
    try:
        for file in foldersDict[folder]:
            pathFile = file

            path = pathDir + pathFile
            createFile(path)
    except TypeError:
        pass



for file in rootFiles:
    createFile(file)