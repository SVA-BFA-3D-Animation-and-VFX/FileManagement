#!/bin/bash

# Set the root directory to the location you want the folder to be created, eg, root set to local DOC use (root="$HOME/Documents") to UCAprod (/Volumes/thesis/old/folderBox)
root="$HOME/Documents/project_folder"

# Check if parent directory is writable
if [ ! -w "$(dirname "$root")" ]; then
    echo "Error: No write permission for $(dirname "$root")"
    exit 1
fi

# Create root directory if it doesn't exist
mkdir -p "$root" || { echo "Failed to create $root"; exit 1; }

# Create first layer folders
mkdir -p "${root}/asset" || { echo "Failed to create ${root}/asset"; exit 1; }
mkdir -p "${root}/editorial" || { echo "Failed to create ${root}/editorial"; exit 1; }
mkdir -p "${root}/io" || { echo "Failed to create ${root}/io"; exit 1; }
mkdir -p "${root}/reference" || { echo "Failed to create ${root}/reference"; exit 1; }

# Create asset folder structure
mkdir -p "${root}/asset/sample_asset/publish/lookdev" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/sample_asset/publish/model" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/sample_asset/publish/rig" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/sample_asset/publish/texture" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/sample_asset/reference" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/sample_asset/work/lookdev" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/sample_asset/work/model" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/sample_asset/work/rig" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/asset/sample_asset/work/texture" || { echo "Failed to create asset subdirectories"; exit 1; }

# Create editorial folder structure
mkdir -p "${root}/editorial/premiere" || { echo "Failed to create ${root}/editorial/premiere"; exit 1; }
mkdir -p "${root}/editorial/hiero" || { echo "Failed to create ${root}/editorial/premiere"; exit 1; }
mkdir -p "${root}/editorial/export" || { echo "Failed to create ${root}/editorial/export"; exit 1; }

# Create io folder structure
mkdir -p "${root}/io/in/YYYY_MM_DD_in_folderName" || { echo "Failed to create io subdirectories"; exit 1; }
mkdir -p "${root}/io/out/YYYY_MM_DD_out_folderName" || { echo "Failed to create io subdirectories"; exit 1; }

# Create sequence folder structure
mkdir -p "${root}/sequence/seq010_0000/publish/anim" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/publish/comp" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/publish/fx" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/publish/lighting" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/reference" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/source/audio" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/source/plates" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/work/anim/maya" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/work/comp/nuke" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/work/fx" || { echo "Failed to create sequence subdirectories"; exit 1; }
mkdir -p "${root}/sequence/seq010_0000/work/lighting/maya" || { echo "Failed to create sequence subdirectories"; exit 1; }

# Display completion message
echo ""
echo "The folders have been successfully created at:"
echo "${root}"
echo "Note: Duplicate 'sample_asset' for new assets (e.g., 'Gecko', 'Office') and 'shot_template' for new shots (e.g., 'seq020_0010')."
echo ""


# Pause
read -p "Press Enter to continue..."