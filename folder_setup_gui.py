#!/usr/bin/env python3
"""GUI application for creating and managing 3D Animation & VFX project folder structures."""

import os
import platform
import re
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

class FolderSetupGUI:
    """Class to manage the folder setup GUI for 3D Animation & VFX projects."""
    
    def __init__(self, root):
        """Initialize the GUI with a Tkinter window and setup UI elements."""
        self.root = root
        self.root.title("3D Animation & VFX Folder Setup")
        self.root.geometry("550x450")
        self.root.configure(bg="#FFE869")
        self.is_windows = platform.system() == "Windows"
        self.home_dir = os.path.expanduser("~")
        self.root_dir = os.path.join(self.home_dir, "Documents", "project_folder")
        self.script_ext = ".bat" if self.is_windows else ".sh"
        self.thesis_server = r"\\ucaprod\thesis" if self.is_windows else "/Volumes/thesis"
        self.project_id = None

        # Main frame for centering
        self.main_frame = tk.Frame(self.root, bg="#FFE869")
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title labels
        tk.Label(
            self.main_frame,
            text="3D ANIMATION & VFX",
            font=("Arial", 24, "bold"),
            fg="#FF3716",
            bg="#FFE869"
        ).pack(pady=2)
        tk.Label(
            self.main_frame,
            text="Folder Setup",
            font=("Arial", 24, "bold"),
            fg="black",
            bg="#FFE869"
        ).pack(pady=2)
            
        # Root directory label
        self.root_label = tk.Label(
            self.main_frame,
            text=f"Root Directory: {self.root_dir}",
            font=("Arial", 14),
            bg="#FFE869",
            fg="black"
        )
        self.root_label.pack(pady=10)

        # Button dimensions and colors
        button_width = 240
        button_height = 40
        edge_buffer_color = "#FFF9A3"

        # Select Root Directory button
        self.canvas1 = tk.Canvas(
            self.main_frame,
            width=button_width+4,
            height=button_height+4,
            bg=edge_buffer_color,
            highlightthickness=0
        )
        self.canvas1.pack(pady=5)
        self.canvas1.create_rectangle(2, 2, button_width+2, button_height+2, fill="#F77969", outline="#F77969")
        self.canvas1.create_text(button_width//2, button_height//2, text="Select Root Directory", font=("Arial", 16), fill="black")
        self.canvas1.bind("<Button-1>", lambda e: self.select_root_dir())

        # Create Folder Structure button
        self.canvas2 = tk.Canvas(
            self.main_frame,
            width=button_width+4,
            height=button_height+4,
            bg=edge_buffer_color,
            highlightthickness=0
        )
        self.canvas2.pack(pady=5)
        self.canvas2.create_rectangle(2, 2, button_width+2, button_height+2, fill="white", outline="white")
        self.canvas2.create_text(button_width//2, button_height//2, text="Create Folder Structure", font=("Arial", 16), fill="black")
        self.canvas2.bind("<Button-1>", lambda e: self.create_folder_structure())

        # Add New Asset button
        self.canvas3 = tk.Canvas(
            self.main_frame,
            width=button_width+4,
            height=button_height+4,
            bg=edge_buffer_color,
            highlightthickness=0
        )
        self.canvas3.pack(pady=5)
        self.canvas3.create_rectangle(2, 2, button_width+2, button_height+2, fill="#2CB0C8", outline="#2CB0C8")
        self.canvas3.create_text(button_width//2, button_height//2, text="Add New Asset", font=("Arial", 16), fill="black")
        self.canvas3.bind("<Button-1>", lambda e: self.add_asset())

        # Add New Shot button
        self.canvas4 = tk.Canvas(
            self.main_frame,
            width=button_width+4,
            height=button_height+4,
            bg=edge_buffer_color,
            highlightthickness=0
        )
        self.canvas4.pack(pady=5)
        self.canvas4.create_rectangle(2, 2, button_width+2, button_height+2, fill="#C2C0C0", outline="#C2C0C0")
        self.canvas4.create_text(button_width//2, button_height//2, text="Add New Shot", font=("Arial", 16), fill="black")
        self.canvas4.bind("<Button-1>", lambda e: self.add_shot())

        # Status label
        self.status_label = tk.Label(
            self.main_frame,
            text="",
            wraplength=450,
            font=("Arial", 14),
            bg="#FFE869",
            fg="black"
        )
        self.status_label.pack(pady=10)

    def select_root_dir(self):
        """Open a dialog to select the root directory and update the UI."""
        selected_dir = filedialog.askdirectory(title="Select Root Directory")
        if selected_dir:
            self.root_dir = os.path.normpath(selected_dir)
            self.project_id = None
            self.root_label.config(text=f"Root Directory: {self.root_dir}")
            self.status_label.config(text=f"Root directory updated to: {self.root_dir}")

    def is_thesis_server(self, root_dir):
        """Check if the root directory is the thesis server."""
        return os.path.normpath(root_dir).lower() == os.path.normpath(self.thesis_server).lower()

    def validate_project_code(self, project_code):
        """Validate project code format (3 letters, 4 numbers)."""
        return bool(re.match(r"^[a-zA-Z]{3}\d{4}$", project_code))

    def create_folder_structure(self):
        """Create the project folder structure based on the root directory."""
        try:
            if self.is_thesis_server(self.root_dir):
                project_id = simpledialog.askstring(
                    "Input", "Enter project code (e.g., ABC1234):", parent=self.root
                )
                if project_id is None:
                    return
                if not project_id:
                    project_id = "ABC1234"
                if not self.validate_project_code(project_id):
                    messagebox.showerror(
                        "Error",
                        "Invalid project code format! It must be 3 letters followed by 4 numbers "
                        "(e.g., ABC1234). Please contact your tech advisor to obtain a valid project code."
                    )
                    return
            else:
                project_id = simpledialog.askstring(
                    "Input", "Enter project name or code (e.g., MyProject, ABC1234):", parent=self.root
                )
                if project_id is None:
                    return
                if not project_id:
                    project_id = "MyProject"

            project_dir = os.path.join(self.root_dir, project_id)
            if self.is_thesis_server(self.root_dir):
                if not os.path.exists(project_dir):
                    messagebox.showerror(
                        "Error",
                        f"Project code {project_id} does not exist on the network server. "
                        "Please contact your tech advisor to obtain a valid project code."
                    )
                    return
            else:
                os.makedirs(project_dir, exist_ok=True)

            self.project_id = project_id
            parent_dir = os.path.dirname(project_dir)
            if not os.access(parent_dir, os.W_OK):
                raise PermissionError(f"No write permission for {parent_dir}")

            folders = ["assets", "common", "editorial", "io", "reference", "sandbox", "sequence"]
            for folder in folders:
                os.makedirs(os.path.join(project_dir, folder), exist_ok=True)

            asset_path = os.path.join(project_dir, "assets", "SampleAsset")
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

            asset_script_path = os.path.join(project_dir, "assets", f"add_asset{self.script_ext}")
            if self.is_windows:
                with open(asset_script_path, "w", encoding="utf-8", newline="\r\n") as f:
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
                    f.write('set "asset_dir=%~dp0%asset_name%"\n')
                    f.write('if exist "%asset_dir%" (echo Error: Asset \'%asset_name%\' already exists at %asset_dir% & exit /b 1)\n')
                    f.write('mkdir "%asset_dir%\\publish\\lookdev\\maya_file"\n')
                    f.write('mkdir "%asset_dir%\\publish\\model\\alembic_geometry"\n')
                    f.write('mkdir "%asset_dir%\\publish\\model\\maya_file"\n')
                    f.write('mkdir "%asset_dir%\\publish\\rig\\alembic_geometry"\n')
                    f.write('mkdir "%asset_dir%\\publish\\rig\\maya_file"\n')
                    f.write('mkdir "%asset_dir%\\publish\\texture\\texture_image"\n')
                    f.write('mkdir "%asset_dir%\\reference\\documents"\n')
                    f.write('mkdir "%asset_dir%\\reference\\images"\n')
                    f.write('mkdir "%asset_dir%\\reference\\videos"\n')
                    f.write('mkdir "%asset_dir%\\work\\lookdev\\maya_file"\n')
                    f.write('mkdir "%asset_dir%\\work\\model\\maya"\n')
                    f.write('mkdir "%asset_dir%\\work\\model\\zbrush"\n')
                    f.write('mkdir "%asset_dir%\\work\\rig\\maya"\n')
                    f.write('mkdir "%asset_dir%\\work\\texture\\maya"\n')
                    f.write('mkdir "%asset_dir%\\work\\texture\\photoshop"\n')
                    f.write('mkdir "%asset_dir%\\work\\texture\\substance"\n')
                    f.write('echo Asset \'%asset_name%\' created at: %asset_dir%\n')
                    f.write('if "%~1"=="" pause\n')
            else:
                with open(asset_script_path, "w", encoding="utf-8", newline="\n") as f:
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
                    f.write('asset_dir="$(dirname "$0")/$asset_name"\n')
                    f.write('if [ -d "$asset_dir" ]; then\n')
                    f.write('    echo "Error: Asset \'$asset_name\' already exists at $asset_dir"\n')
                    f.write('    exit 1\n')
                    f.write('fi\n')
                    f.write('mkdir -p "$asset_dir/publish/lookdev/maya_file"\n')
                    f.write('mkdir -p "$asset_dir/publish/model/alembic_geometry"\n')
                    f.write('mkdir -p "$asset_dir/publish/model/maya_file"\n')
                    f.write('mkdir -p "$asset_dir/publish/rig/alembic_geometry"\n')
                    f.write('mkdir -p "$asset_dir/publish/rig/maya_file"\n')
                    f.write('mkdir -p "$asset_dir/publish/texture/texture_image"\n')
                    f.write('mkdir -p "$asset_dir/reference/documents"\n')
                    f.write('mkdir -p "$asset_dir/reference/images"\n')
                    f.write('mkdir -p "$asset_dir/reference/videos"\n')
                    f.write('mkdir -p "$asset_dir/work/lookdev/maya_file"\n')
                    f.write('mkdir -p "$asset_dir/work/model/maya"\n')
                    f.write('mkdir -p "$asset_dir/work/model/zbrush"\n')
                    f.write('mkdir -p "$asset_dir/work/rig/maya"\n')
                    f.write('mkdir -p "$asset_dir/work/texture/maya"\n')
                    f.write('mkdir -p "$asset_dir/work/texture/photoshop"\n')
                    f.write('mkdir -p "$asset_dir/work/texture/substance"\n')
                    f.write('echo "Asset \'$asset_name\' created at: $asset_dir"\n')
                    f.write('[ $# -eq 0 ] && read -p "Press Enter to continue..."\n')
                os.chmod(asset_script_path, 0o755)

            os.makedirs(os.path.join(project_dir, "common", "scripts"), exist_ok=True)
            for subfolder in ["audio", "edits", "edls", "exports", "footage", "stills", "storyboards"]:
                os.makedirs(os.path.join(project_dir, "editorial", subfolder), exist_ok=True)
            os.makedirs(os.path.join(project_dir, "io", "in", "YYYY_MM_DD_in_folderName"), exist_ok=True)
            os.makedirs(os.path.join(project_dir, "io", "out", "YYYY_MM_DD_out_folderName"), exist_ok=True)
            for subfolder in ["documents", "images", "videos"]:
                os.makedirs(os.path.join(project_dir, "reference", subfolder), exist_ok=True)

            sandbox_path = os.path.join(project_dir, "sandbox", "userName")
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

            sequence_path = os.path.join(project_dir, "sequence", "seq010", "seq010_0010")
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

            shot_script_path = os.path.join(project_dir, "sequence", f"add_shot{self.script_ext}")
            if self.is_windows:
                with open(shot_script_path, "w", encoding="utf-8", newline="\r\n") as f:
                    f.write("@echo off\n")
                    f.write("setlocal\n")
                    f.write('if "%~1"=="" (\n')
                    f.write('    set /p shot_name=Enter new shot name (e.g., seq020_0010): \n')
                    f.write('    if "%shot_name%"=="" (\n')
                    f.write('        dir "%~dp0" | find "seq" > temp.txt\n')
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
                    f.write('set "shot_dir=%~dp0%shot_name%"\n')
                    f.write('if exist "%shot_dir%" (echo Error: Shot \'%shot_name%\' already exists at %shot_dir% & exit /b 1)\n')
                    f.write('mkdir "%shot_dir%\\publish\\anim\\alembic_camera"\n')
                    f.write('mkdir "%shot_dir%\\publish\\anim\\alembic_geometry"\n')
                    f.write('mkdir "%shot_dir%\\publish\\audio"\n')
                    f.write('mkdir "%shot_dir%\\publish\\comp\\composited_image"\n')
                    f.write('mkdir "%shot_dir%\\publish\\design\\composited_image"\n')
                    f.write('mkdir "%shot_dir%\\publish\\fx\\alembic_geometry"\n')
                    f.write('mkdir "%shot_dir%\\publish\\lighting\\composited_image"\n')
                    f.write('mkdir "%shot_dir%\\publish\\lighting\\rendered_image"\n')
                    f.write('mkdir "%shot_dir%\\publish\\plates\\anim_plate"\n')
                    f.write('mkdir "%shot_dir%\\publish\\plates\\lighting_plate"\n')
                    f.write('mkdir "%shot_dir%\\publish\\plates\\source_plate"\n')
                    f.write('mkdir "%shot_dir%\\reference\\documents"\n')
                    f.write('mkdir "%shot_dir%\\reference\\images"\n')
                    f.write('mkdir "%shot_dir%\\reference\\videos"\n')
                    f.write('mkdir "%shot_dir%\\work\\anim\\maya"\n')
                    f.write('mkdir "%shot_dir%\\work\\comp\\nuke"\n')
                    f.write('mkdir "%shot_dir%\\work\\design\\ae"\n')
                    f.write('mkdir "%shot_dir%\\work\\design\\photoshop"\n')
                    f.write('mkdir "%shot_dir%\\work\\fx\\houdini"\n')
                    f.write('mkdir "%shot_dir%\\work\\fx\\maya"\n')
                    f.write('mkdir "%shot_dir%\\work\\lighting\\houdini"\n')
                    f.write('mkdir "%shot_dir%\\work\\lighting\\maya"\n')
                    f.write('echo Shot \'%shot_name%\' created at: %shot_dir%\n')
                    f.write('if "%~1"=="" pause\n')
            else:
                with open(shot_script_path, "w", encoding="utf-8", newline="\n") as f:
                    f.write("#!/bin/bash\n")
                    f.write('if [ $# -eq 1 ]; then\n')
                    f.write('    shot_name="$1"\n')
                    f.write('else\n')
                    f.write('    read -p "Enter new shot name (e.g., seq020_0010): " shot_name\n')
                    f.write('    if [ -z "$shot_name" ]; then\n')
                    f.write('        last_seq=$(ls "$(dirname "$0")" | grep "seq" | tail -n 1)\n')
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
                    f.write('shot_dir="$(dirname "$0")/$shot_name"\n')
                    f.write('if [ -d "$shot_dir" ]; then\n')
                    f.write('    echo "Error: Shot \'$shot_name\' already exists at $shot_dir"\n')
                    f.write('    exit 1\n')
                    f.write('fi\n')
                    f.write('mkdir -p "$shot_dir/publish/anim/alembic_camera"\n')
                    f.write('mkdir -p "$shot_dir/publish/anim/alembic_geometry"\n')
                    f.write('mkdir -p "$shot_dir/publish/audio"\n')
                    f.write('mkdir -p "$shot_dir/publish/comp/composited_image"\n')
                    f.write('mkdir -p "$shot_dir/publish/design/composited_image"\n')
                    f.write('mkdir -p "$shot_dir/publish/fx/alembic_geometry"\n')
                    f.write('mkdir -p "$shot_dir/publish/lighting/composited_image"\n')
                    f.write('mkdir -p "$shot_dir/publish/lighting/rendered_image"\n')
                    f.write('mkdir -p "$shot_dir/publish/plates/anim_plate"\n')
                    f.write('mkdir -p "$shot_dir/publish/plates/lighting_plate"\n')
                    f.write('mkdir -p "$shot_dir/publish/plates/source_plate"\n')
                    f.write('mkdir -p "$shot_dir/reference/documents"\n')
                    f.write('mkdir -p "$shot_dir/reference/images"\n')
                    f.write('mkdir -p "$shot_dir/reference/videos"\n')
                    f.write('mkdir -p "$shot_dir/work/anim/maya"\n')
                    f.write('mkdir -p "$shot_dir/work/comp/nuke"\n')
                    f.write('mkdir -p "$shot_dir/work/design/ae"\n')
                    f.write('mkdir -p "$shot_dir/work/design/photoshop"\n')
                    f.write('mkdir -p "$shot_dir/work/fx/houdini"\n')
                    f.write('mkdir -p "$shot_dir/work/fx/maya"\n')
                    f.write('mkdir -p "$shot_dir/work/lighting/houdini"\n')
                    f.write('mkdir -p "$shot_dir/work/lighting/maya"\n')
                    f.write('echo "Shot \'$shot_name\' created at: $shot_dir"\n')
                    f.write('[ $# -eq 0 ] && read -p "Press Enter to continue..."\n')
                os.chmod(shot_script_path, 0o755)

            # Update root_dir to the new project directory
            self.root_dir = project_dir
            self.root_label.config(text=f"Root Directory: {self.root_dir}")
            self.status_label.config(
                text=f"Folder structure created at: {project_dir}\n",
            )
            
            
        except PermissionError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create folders: {str(e)}")

    def add_asset(self):
        """Add a new asset to the assets folder in the selected root directory."""
        try:
            assets_dir = os.path.join(self.root_dir, "assets")
            if not os.path.exists(assets_dir):
                messagebox.showerror(
                    "Error",
                    f"No Assets folder found in {self.root_dir}. "
                    "Please select a project folder containing an Assets folder or "
                    "click 'Create Folder Structure' to create one."
                )
                return

            asset_name = simpledialog.askstring(
                "Input", "Enter new asset name (e.g., Gecko, Office):", parent=self.root
            )
            if asset_name is None:
                return
            if not asset_name:
                asset_name = "SampleAsset"
            if re.search(r"\s", asset_name):
                messagebox.showerror("Error", "Asset name cannot contain spaces.")
                return

            asset_dir = os.path.join(assets_dir, asset_name)
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
        """Add a new shot to the sequence folder in the selected root directory."""
        try:
            sequence_dir = os.path.join(self.root_dir, "sequence")
            if not os.path.exists(sequence_dir):
                messagebox.showerror(
                    "Error",
                    f"No Sequence folder found in {self.root_dir}. "
                    "Please select a project folder containing a Sequence folder or "
                    "click 'Create Folder Structure' to create one."
                )
                return

            shot_name = simpledialog.askstring(
                "Input", "Enter new shot name (e.g., seq020_0010):", parent=self.root
            )
            if shot_name is None:
                return
            if not shot_name:
                last_seq = None
                if os.path.exists(sequence_dir):
                    seq_folders = [f for f in os.listdir(sequence_dir) if f.startswith("seq")]
                    if seq_folders:
                        last_seq = max(seq_folders, key=lambda x: int(re.search(r"seq(\d+)", x).group(1)) if re.search(r"seq(\d+)", x) else 0)
                seq_num = 10
                if last_seq and re.search(r"seq(\d+)", last_seq):
                    seq_num = int(re.search(r"seq(\d+)", last_seq).group(1)) + 10
                shot_name = f"seq{seq_num:03d}_0010"

            if re.search(r"\s", shot_name):
                messagebox.showerror("Error", "Shot name cannot contain spaces.")
                return

            shot_dir = os.path.join(sequence_dir, shot_name)
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