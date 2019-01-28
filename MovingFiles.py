# This file splits dogs and cats in different folders

import os
import shutil

# Declare directories to be used

srcpath = "/Users/marcogdepinto/PycharmProjects/DogOrCat/data/train"
destPathDogs = "/Users/marcogdepinto/PycharmProjects/DogOrCat/data/train/Dogs"
destPathCats = "/Users/marcogdepinto/PycharmProjects/DogOrCat/data/train/Cats"

count = 0

# Create directories if they not exist

if not os.path.exists(destPathDogs):
    os.makedirs(destPathDogs)

if not os.path.exists(destPathCats):
    os.makedirs(destPathCats)

# Move files from data/train to data/train/Dogs and data/train/Cats

for root, subFolders, files in os.walk(srcpath):
    for file in files:
        if file.startswith('dog'):
            shutil.move(os.path.join(root, file), destPathDogs)
            print("Moved file", file, "into directory", destPathDogs)
        elif file.startswith('cat'):
            shutil.move(os.path.join(root, file), destPathCats)
            print("Moved file", file, "into directory", destPathCats)
        else:
            print("Skipping file", file)
            continue