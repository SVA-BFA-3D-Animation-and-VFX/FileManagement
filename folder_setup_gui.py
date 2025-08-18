#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os
import platform
import re

class FolderSetupGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Folder Setup")
        self.root.geometry("400x300")

        # Determine OS and root directory
        self.is_windows = platform.system() == "Windows"
        self.home_dir = os.path.expanduser("~")
        self.root_dir = os.path.join(self.home_dir, "Documents", "project_folder")
        self.script_ext = ".bat" if self.is_windows else ".sh"

        # Create GUI elements
        tk.Label(root, text="Animation/VFX Folder Setup", font=("Arial", 14)).pack(pady=10)
        tk.Button(root, text="Create Folder Structure", command=self.create_folder_structure).pack(pady=10)
        tk.Button(root, text="Add New Asset", command=self.add_asset).pack(pady=10)
        tk.Button(root, text="Add New Shot", command=self.add_shot).pack(pady=10)
        self.status_label = tk.Label(root, text="", wraplength=350)
        self.status_label.pack(pady=10)

    def create_folder_structure(self):
        try:
            # Check if parent directory is writable
            parent_dir = os.path.dirname(self.root_dir)
            if not os.access(parent_dir, os.W_OK):
                raise PermissionError(f"No write permission for {parent_dir}")

            # Create root directory
            os.makedirs(self.root_dir, exist_ok=True)

            # First layer folders
            folders = ["assets", "common", "editorial", "io", "reference", "sandbox", "sequence"]
            for folder in folders:
                os.makedirs(os.path.join(self.root_dir, folder), exist_ok=True)

            # Assets: SampleAsset
            asset_path = os.path.join(self.root_dir, "assets", "SampleAsset")
            for subfolder in ["publish", "work"]:
                for item in ["lookdev", "model", "rig", "texture"]:
                    if subfolder == "publish":
                        if item == "lookdev":
                            os.makedirs(os.path.join(asset_path, subfolder, item, "maya_file"), exist_ok=True)
                        elif item in ["model", "rig"]:
                            os.makedirs(os.path.join(asset_path, subfolder, item, "alembic_geometry"), exist_ok=True)
                            os.makedirs(os.path.join(asset_path, subfolder, item, "maya_file"), exist_ok=True)
                        elif item == "texture":
                            os.makedirs(os.path.join(asset_path, subfolder, item, "texture_image"), exist_ok=True)
                    elif subfolder == "work":
                        if item == "lookdev":
                            os.makedirs(os.path.join(asset_path, subfolder, item, "maya_file"), exist_ok=True)
                        elif item == "model":
                            os.makedirs(os.path.join(asset_path, subfolder, item, "maya"), exist_ok=True)
                            os.makedirs(os.path.join(asset_path, subfolder, item, "zbrush"), exist_ok=True)
                        elif item == "rig":
                            os.makedirs(os.path.join(asset_path, subfolder, item, "maya"), exist_ok=True)
                        elif item == "texture":
                            os.makedirs(os.path.join(asset_path, subfolder, item, "maya"), exist_ok=True)
                            os.makedirs(os.path.join(asset_path, subfolder, item, "photoshop"), exist_ok=True)
                            os.makedirs(os.path.join(asset_path, subfolder, item, "substance"), exist_ok=True)
            for subfolder in ["documents", "images", "videos"]:
                os.makedirs(os.path.join(asset_path, "reference", subfolder), exist_ok=True)

            # Create add_asset script
            asset_script_path = os.path.join(self.root_dir, "assets", f"add_asset{self.script_ext}")
            if self.is_windows:
                with open(asset_script_path, "w", newline="\r\n") as f:
                    f.write("@echo off\n")
                    f.write("setlocal\n")
                    f.write('if "%~1"=="" (\n')
                    f.write('    set /p asset_name=Enter new asset name (e.g., Gecko, Office): \n')
                    f.write('    if "%asset_name%"=="" set "asset_name=SampleAsset"\n')
                    f.write(') else (\n')
                    f.write('    set "asset_name=%~1"\n')
                    f.write(')\n')
                    f.write('if "%asset_name%"=="" (echo Error: Asset name cannot be empty. & exit /b 1)\n')
                    f.write('echo %asset_name% | find " " >nul && (echo Error: Asset name cannot contain spaces. & exit /b 1)\n')
                    f.write('set "asset_dir=%~dp0..\\assets\\%asset_name%"\n')
                    f.write('if exist "%asset_dir%" (echo Error: Asset \'%asset_name%\' already exists at %asset_dir% & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\publish\\lookdev\\maya_file" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\publish\\model\\alembic_geometry" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\publish\\model\\maya_file" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\publish\\rig\\alembic_geometry" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\publish\\rig\\maya_file" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\publish\\texture\\texture_image" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\reference\\documents" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\reference\\images" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\reference\\videos" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\work\\lookdev\\maya_file" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\work\\model\\maya" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\work\\model\\zbrush" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\work\\rig\\maya" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\work\\texture\\maya" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\work\\texture\\photoshop" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\work\\texture\\substance" || (echo Failed to create asset subdirectories & exit /b 1)\n')
                    f.write('echo Asset \'%asset_name%\' created at: %asset_dir%\n')
                    f.write('if "%~1"=="" pause\n')
            else:
                with open(asset_script_path, "w", newline="\n") as f:
                    f.write("#!/bin/bash\n")
                    f.write('if [ $# -eq 1 ]; then\n')
                    f.write('    asset_name="$1"\n')
                    f.write('else\n')
                    f.write('    read -p "Enter new asset name (e.g., Gecko, Office): " asset_name\n')
                    f.write('    [ -z "$asset_name" ] && asset_name="SampleAsset"\n')
                    f.write('fi\n')
                    f.write('if [ -z "$asset_name" ]; then\n')
                    f.write('    echo "Error: Asset name cannot be empty."\n')
                    f.write('    exit 1\n')
                    f.write('fi\n')
                    f.write('if [[ "$asset_name" =~ \\s ]]; then\n')
                    f.write('    echo "Error: Asset name cannot contain spaces."\n')
                    f.write('    exit 1\n')
                    f.write('fi\n')
                    f.write('asset_dir="$(dirname "$(dirname "$0")")/assets/$asset_name"\n')
                    f.write('if [ -d "$asset_dir" ]; then\n')
                    f.write('    echo "Error: Asset \'$asset_name\' already exists at $asset_dir"\n')
                    f.write('    exit 1\n')
                    f.write('fi\n')
                    f.write('mkdir -p "${asset_dir}/publish/lookdev/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/publish/model/alembic_geometry" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/publish/model/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/publish/rig/alembic_geometry" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/publish/rig/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/publish/texture/texture_image" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/reference/documents" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/reference/images" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/reference/videos" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/work/lookdev/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/work/model/maya" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/work/model/zbrush" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/work/rig/maya" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/work/texture/maya" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/work/texture/photoshop" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${asset_dir}/work/texture/substance" || { echo "Failed to create asset subdirectories"; exit 1; }\n')
                    f.write('echo "Asset \'$asset_name\' created at: $asset_dir"\n')
                    f.write('[ $# -eq 0 ] && read -p "Press Enter to continue..."\n')
                os.chmod(asset_script_path, 0o755)

            # Common
            os.makedirs(os.path.join(self.root_dir, "common", "scripts"), exist_ok=True)

            # Editorial
            for subfolder in ["audio", "edits", "edls", "exports", "footage", "stills", "storyboards"]:
                os.makedirs(os.path.join(self.root_dir, "editorial", subfolder), exist_ok=True)

            # I/O
            os.makedirs(os.path.join(self.root_dir, "io", "in", "YYYY_MM_DD_in_folderName"), exist_ok=True)
            os.makedirs(os.path.join(self.root_dir, "io", "out", "YYYY_MM_DD_out_folderName"), exist_ok=True)

            # Reference
            for subfolder in ["documents", "images", "videos"]:
                os.makedirs(os.path.join(self.root_dir, "reference", subfolder), exist_ok=True)

            # Sandbox
            sandbox_path = os.path.join(self.root_dir, "sandbox", "userName")
            for subfolder in ["publish", "work"]:
                for item in ["anim", "comp", "design", "fx", "lighting"]:
                    if subfolder == "publish":
                        if item == "anim":
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "alembic_camera"), exist_ok=True)
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "alembic_geometry"), exist_ok=True)
                        elif item in ["comp", "design", "lighting"]:
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "composited_image"), exist_ok=True)
                            if item == "lighting":
                                os.makedirs(os.path.join(sandbox_path, subfolder, item, "rendered_image"), exist_ok=True)
                        elif item == "fx":
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "alembic_geometry"), exist_ok=True)
                    elif subfolder == "work":
                        if item == "anim":
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "maya"), exist_ok=True)
                        elif item == "comp":
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "nuke"), exist_ok=True)
                        elif item == "design":
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "ae"), exist_ok=True)
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "photoshop"), exist_ok=True)
                        elif item in ["fx", "lighting"]:
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "houdini"), exist_ok=True)
                            os.makedirs(os.path.join(sandbox_path, subfolder, item, "maya"), exist_ok=True)
            for subfolder in ["documents", "images", "videos"]:
                os.makedirs(os.path.join(sandbox_path, "reference", subfolder), exist_ok=True)

            # Sequence: seq010/seq010_0010
            sequence_path = os.path.join(self.root_dir, "sequence", "seq010", "seq010_0010")
            for subfolder in ["publish", "work"]:
                for item in ["anim", "comp", "design", "fx", "lighting"]:
                    if subfolder == "publish":
                        if item == "anim":
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "alembic_camera"), exist_ok=True)
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "alembic_geometry"), exist_ok=True)
                        elif item in ["comp", "design", "lighting"]:
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "composited_image"), exist_ok=True)
                            if item == "lighting":
                                os.makedirs(os.path.join(sequence_path, subfolder, item, "rendered_image"), exist_ok=True)
                        elif item == "fx":
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "alembic_geometry"), exist_ok=True)
                    elif subfolder == "work":
                        if item == "anim":
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "maya"), exist_ok=True)
                        elif item == "comp":
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "nuke"), exist_ok=True)
                        elif item == "design":
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "ae"), exist_ok=True)
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "photoshop"), exist_ok=True)
                        elif item in ["fx", "lighting"]:
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "houdini"), exist_ok=True)
                            os.makedirs(os.path.join(sequence_path, subfolder, item, "maya"), exist_ok=True)
            os.makedirs(os.path.join(sequence_path, "publish", "audio"), exist_ok=True)
            for subfolder in ["anim_plate", "lighting_plate", "source_plate"]:
                os.makedirs(os.path.join(sequence_path, "publish", "plates", subfolder), exist_ok=True)
            for subfolder in ["documents", "images", "videos"]:
                os.makedirs(os.path.join(sequence_path, "reference", subfolder), exist_ok=True)

            # Create add_shot script
            shot_script_path = os.path.join(self.root_dir, "sequence", f"add_shot{self.script_ext}")
            if self.is_windows:
                with open(shot_script_path, "w", newline="\r\n") as f:
                    f.write("@echo off\n")
                    f.write("setlocal\n")
                    f.write('if "%~1"=="" (\n')
                    f.write('    set /p shot_name=Enter new shot name (e.g., seq020_0010): \n')
                    f.write('    if "%shot_name%"=="" (\n')
                    f.write('        dir "%~dp0..\\sequence" | find "seq" > temp.txt\n')
                    f.write('        for /f "tokens=*" %%i in (temp.txt) do set "last_seq=%%i"\n')
                    f.write('        set /a "seq_num=10"\n')
                    f.write('        if defined last_seq (\n')
                    f.write('            for /f "tokens=2 delims=seq" %%j in ("%%last_seq%%") do set /a "seq_num=%%j+10"\n')
                    f.write('        )\n')
                    f.write('        set "shot_name=seq%%seq_num%%_0010"\n')
                    f.write('        del temp.txt\n')
                    f.write('    )\n')
                    f.write(') else (\n')
                    f.write('    set "shot_name=%~1"\n')
                    f.write(')\n')
                    f.write('if "%shot_name%"=="" (echo Error: Shot name cannot be empty. & exit /b 1)\n')
                    f.write('echo %shot_name% | find " " >nul && (echo Error: Shot name cannot contain spaces. & exit /b 1)\n')
                    f.write('set "shot_dir=%~dp0..\\sequence\\%shot_name%"\n')
                    f.write('if exist "%shot_dir%" (echo Error: Shot \'%shot_name%\' already exists at %shot_dir% & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\anim\\alembic_camera" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\anim\\alembic_geometry" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\audio" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\comp\\composited_image" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\design\\composited_image" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\fx\\alembic_geometry" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\lighting\\composited_image" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\lighting\\rendered_image" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\plates\\anim_plate" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\plates\\lighting_plate" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\plates\\source_plate" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\reference\\documents" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\reference\\images" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\reference\\videos" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\work\\anim\\maya" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\work\\comp\\nuke" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\work\\design\\ae" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\work\\design\\photoshop" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\work\\fx\\houdini" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\work\\fx\\maya" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\work\\lighting\\houdini" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\work\\lighting\\maya" || (echo Failed to create sequence subdirectories & exit /b 1)\n')
                    f.write('echo Shot \'%shot_name%\' created at: %shot_dir%\n')
                    f.write('if "%~1"=="" pause\n')
            else:
                with open(shot_script_path, "w", newline="\n") as f:
                    f.write("#!/bin/bash\n")
                    f.write('if [ $# -eq 1 ]; then\n')
                    f.write('    shot_name="$1"\n')
                    f.write('else\n')
                    f.write('    read -p "Enter new shot name (e.g., seq020_0010): " shot_name\n')
                    f.write('    if [ -z "$shot_name" ]; then\n')
                    f.write('        last_seq=$(ls "$(dirname "$(dirname "$0")")/sequence" | grep "seq" | tail -n 1)\n')
                    f.write('        seq_num=10\n')
                    f.write('        if [ -n "$last_seq" ]; then\n')
                    f.write('            seq_num=$(echo "$last_seq" | sed -E "s/seq([0-9]+).*/\\1/" | awk "{print $1 + 10}")\n')
                    f.write('        fi\n')
                    f.write('        shot_name="seq$(printf "%03d" $seq_num)_0010"\n')
                    f.write('    fi\n')
                    f.write('fi\n')
                    f.write('if [ -z "$shot_name" ]; then\n')
                    f.write('    echo "Error: Shot name cannot be empty."\n')
                    f.write('    exit 1\n')
                    f.write('fi\n')
                    f.write('if [[ "$shot_name" =~ \\s ]]; then\n')
                    f.write('    echo "Error: Shot name cannot contain spaces."\n')
                    f.write('    exit 1\n')
                    f.write('fi\n')
                    f.write('shot_dir="$(dirname "$(dirname "$0")")/sequence/$shot_name"\n')
                    f.write('if [ -d "$shot_dir" ]; then\n')
                    f.write('    echo "Error: Shot \'$shot_name\' already exists at $shot_dir"\n')
                    f.write('    exit 1\n')
                    f.write('fi\n')
                    f.write('mkdir -p "${shot_dir}/publish/anim/alembic_camera" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/anim/alembic_geometry" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/audio" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/comp/composited_image" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/design/composited_image" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/fx/alembic_geometry" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/lighting/composited_image" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/lighting/rendered_image" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/plates/anim_plate" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/plates/lighting_plate" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/publish/plates/source_plate" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/reference/documents" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/reference/images" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/reference/videos" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/work/anim/maya" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/work/comp/nuke" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/work/design/ae" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/work/design/photoshop" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/work/fx/houdini" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/work/fx/maya" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/work/lighting/houdini" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('mkdir -p "${shot_dir}/work/lighting/maya" || { echo "Failed to create sequence subdirectories"; exit 1; }\n')
                    f.write('echo "Shot \'$shot_name\' created at: $shot_dir"\n')
                    f.write('[ $# -eq 0 ] && read -p "Press Enter to continue..."\n')
                os.chmod(shot_script_path, 0o755)

            self.status_label.config(text=f"Folder structure created at: {self.root_dir}\nUse 'Add New Asset' or 'Add New Shot' buttons, or run scripts in 'assets' and 'sequence'.")
        except PermissionError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create folders: {str(e)}")

    def add_asset(self):
        try:
            asset_name = simpledialog.askstring("Input", "Enter new asset name (e.g., Gecko, Office):", parent=self.root)
            if asset_name is None:  # User cancelled the dialog
                return
            if not asset_name:
                asset_name = "SampleAsset"
            if re.search(r"\s", asset_name):
                messagebox.showerror("Error", "Asset name cannot contain spaces.")
                return

            asset_dir = os.path.join(self.root_dir, "assets", asset_name)
            if os.path.exists(asset_dir):
                messagebox.showerror("Error", f"Asset '{asset_name}' already exists at {asset_dir}")
                return

            for subfolder in ["publish", "work"]:
                for item in ["lookdev", "model", "rig", "texture"]:
                    if subfolder == "publish":
                        if item == "lookdev":
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "maya_file"), exist_ok=True)
                        elif item in ["model", "rig"]:
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "alembic_geometry"), exist_ok=True)
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "maya_file"), exist_ok=True)
                        elif item == "texture":
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "texture_image"), exist_ok=True)
                    elif subfolder == "work":
                        if item == "lookdev":
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "maya_file"), exist_ok=True)
                        elif item == "model":
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "maya"), exist_ok=True)
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "zbrush"), exist_ok=True)
                        elif item == "rig":
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "maya"), exist_ok=True)
                        elif item == "texture":
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "maya"), exist_ok=True)
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "photoshop"), exist_ok=True)
                            os.makedirs(os.path.join(asset_dir, subfolder, item, "substance"), exist_ok=True)
            for subfolder in ["documents", "images", "videos"]:
                os.makedirs(os.path.join(asset_dir, "reference", subfolder), exist_ok=True)
            self.status_label.config(text=f"Asset '{asset_name}' created at: {asset_dir}")
        except PermissionError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create asset: {str(e)}")

    def add_shot(self):
        try:
            shot_name = simpledialog.askstring("Input", "Enter new shot name (e.g., seq020_0010):", parent=self.root)
            if shot_name is None:  # User cancelled the dialog
                return
            if not shot_name:
                sequence_dir = os.path.join(self.root_dir, "sequence")
                last_seq = None
                if os.path.exists(sequence_dir):
                    seq_folders = [f for f in os.listdir(sequence_dir) if f.startswith("seq")]
                    if seq_folders:
                        last_seq = max(seq_folders, key=lambda x: int(re.search(r"seq(\d+)", x).group(1)))
                seq_num = 10
                if last_seq:
                    seq_num = int(re.search(r"seq(\d+)", last_seq).group(1)) + 10
                shot_name = f"seq{seq_num:03d}_0010"

            if re.search(r"\s", shot_name):
                messagebox.showerror("Error", "Shot name cannot contain spaces.")
                return

            shot_dir = os.path.join(self.root_dir, "sequence", shot_name)
            if os.path.exists(shot_dir):
                messagebox.showerror("Error", f"Shot '{shot_name}' already exists at {shot_dir}")
                return

            for subfolder in ["publish", "work"]:
                for item in ["anim", "comp", "design", "fx", "lighting"]:
                    if subfolder == "publish":
                        if item == "anim":
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "alembic_camera"), exist_ok=True)
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "alembic_geometry"), exist_ok=True)
                        elif item in ["comp", "design", "lighting"]:
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "composited_image"), exist_ok=True)
                            if item == "lighting":
                                os.makedirs(os.path.join(shot_dir, subfolder, item, "rendered_image"), exist_ok=True)
                        elif item == "fx":
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "alembic_geometry"), exist_ok=True)
                    elif subfolder == "work":
                        if item == "anim":
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "maya"), exist_ok=True)
                        elif item == "comp":
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "nuke"), exist_ok=True)
                        elif item == "design":
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "ae"), exist_ok=True)
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "photoshop"), exist_ok=True)
                        elif item in ["fx", "lighting"]:
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "houdini"), exist_ok=True)
                            os.makedirs(os.path.join(shot_dir, subfolder, item, "maya"), exist_ok=True)
            os.makedirs(os.path.join(shot_dir, "publish", "audio"), exist_ok=True)
            for subfolder in ["anim_plate", "lighting_plate", "source_plate"]:
                os.makedirs(os.path.join(shot_dir, "publish", "plates", subfolder), exist_ok=True)
            for subfolder in ["documents", "images", "videos"]:
                os.makedirs(os.path.join(shot_dir, "reference", subfolder), exist_ok=True)
            self.status_label.config(text=f"Shot '{shot_name}' created at: {shot_dir}")
        except PermissionError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create shot: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderSetupGUI(root)
    root.mainloop()