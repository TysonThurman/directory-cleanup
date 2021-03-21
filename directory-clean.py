import os
import argparse

parser = argparse.ArgumentParser(
    description="Clean up directory and put files into according folders."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Directory path of the directory to be cleaned"
)

#parse the arguments given by the user and extract the path
args = parser.parse_args()
path = args.path

print(f"Cleaning up directory {path}")

#get all files from given directory
dir_content = os.listdir(path)

#create a relative path from path to the file and the document name
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

#filter our directory content into a documents and folders list
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

#counter to keep track of amount of moved files
#and list of already created folders to avoid multiple creations
moved = 0
created_folders = []

print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")