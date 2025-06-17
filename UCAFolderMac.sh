#!/bin/bash

# Set the root directory to the location you want the folder to be created, eg, to local DOC use (root="$HOME/Documents") to UCAprod (/Volumes/thesis/old/folderBox)
root="$HOME/Documents"

# Check if root directory is writable
if [ ! -w "$root" ]; then
    echo "Error: No write permission for $root or directory does not exist"
    exit 1
fi

# Create first layer folders
mkdir -p "${root}/asset" || { echo "Failed to create ${root}/asset"; exit 1; }
mkdir -p "${root}/editorial" || { echo "Failed to create ${root}/editorial"; exit 1; }
mkdir -p "${root}/io" || { echo "Failed to create ${root}/io"; exit 1; }
mkdir -p "${root}/reference" || { echo "Failed to create ${root}/reference"; exit 1; }

# Create asset folder structure
mkdir -p "${root}/asset/Assets/publish/lookdev" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/Assets/publish/model" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/Assets/publish/rig" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/Assets/publish/texture" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/Assets/reference" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/Assets/work/lookdev" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/Assets/work/model" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/Assets/work/rig" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/Assets/work/texture" || { echo "Failed to create asset subdirectories"; exit 1; }

# Create editorial folder structure
mkdir -p "${root}/editorial/VideoEditingFolder" || { echo "Failed to create ${root}/editorial/VideoEditingFolder"; exit 1; }

# Create io folder structure
mkdir -p "${root}/io/In/YYYY_MM_DD_inFolderName" || { echo "Failed to create io subdirectories"; exit 1; }
mkdir -p "${root}/io/Out/YYYY_MM_DD_inFolderName" || { echo "Failed to create io subdirectories"; exit 1; }

# Create sequence folder structure
mkdir -p "${root}/sequence/seq010_0000/Publish/anim" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/Publish/comp" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/Publish/fx" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/Publish/lighting" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/Reference" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/source/audio" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/source/plates" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/source/anim" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/source/graded" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/source/lighting" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/source/raw" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/work/anim" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/work/comp" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/work/fx" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/work/lighting" || { echo "Failed to create sequence subdirectories"; exit 1; }

# Display completion message
echo ""
echo "The folders have been successfully created at:"
echo "${root}"
echo ""

# Pause
read -p "Press Enter to continue..."
