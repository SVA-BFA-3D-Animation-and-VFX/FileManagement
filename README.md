# Automated Project Folder Structure Creation

This batch script automates the creation of a standardized folder hierarchy for a project. It is designed to quickly set up directories needed for asset management, editorial work, I/O operations, and sequence organization within a specified root directory.

## What the Script Does

- **Sets a Root Directory:**  
UCAFolderMac.sh: Creates the folder structure on macOS in "~/Documents/ProjectFolder".
UCAFolderW.bat: Creates the same structure on Windows in "%USERPROFILE%\Documents\ProjectFolder" (e.g., C:\Users\YourUsername\Documents\ProjectFolder).

- **Folder Structure:**  
- **Top-Level Folders:**  
  It generates four main folders:  
  - `asset`
  - `editorial`
  - `io`
  - `reference`

- **Subfolder:**  
  - **Asset:**  
      Organizes assets into `Assets`, with further subdivisions.
    -  `publish`: (lookdev, model, rig, texture),
    -  `reference`
    -  `work`: (lookdev, model, rig, texture).

  - **Editorial Folder:**  
    - Creates a `VideoEditingFolder` for editorial tasks.
  - **I/O Folder:**  
    - Sets up `In` and `Out` folders, each with a placeholder for dated subfolders (`YYYY_MM_DD_inFolderName`).
  - **Sequence Folder:**  
    Establishes a `sequence` directory containing a sample sequence (`seq010_0000`) with subfolders.
    - `Publish` (anim, comp, fx, lighting),
    - `Reference`,
    - `source` (audio, plates, anim, graded, lighting, raw)
    - `work` (anim, comp, fx, lighting).

- **Completion Message:**  
  After creating all directories, the script displays a message indicating successful completion and the root location.

## How to Use
**Windows (UCAFolderW.bat)**
1. **Save the Script:**  
   Copy the script into a text editor and save it with a `.bat` extension (e.g., `UCAFolderW.bat`).
2. **Run the Script:**  
   Double-click the `.bat` file or execute it from the command prompt.  
   The folders will be created automatically at the specified root location.
   
**macOS (UCAFolderMac.sh)**

1. **Save the Script:**  
   Copy the script into a text editor and save it with a `.bat` extension (e.g., `UCAFolderW.bat`).
2. **Make the script executable** <br />
   chmod +x UCAFolderMac.sh
3. **Run the Script:** <br />
   cd to the script folder and enter ./UCAFolderMac.sh (this is the script file name)

**Change Root Directory**

Example for a network server:
Windows: Edit root in UCAFolder.bat, line 5 (e.g., set "root=\\ucaprod\thesis\ProjectFolder"). <br />
macOS: Edit root in UCAFolderMac.sh line 4 (e.g., root="/Volumes/thesis/ProjectFolder").<br />
For network servers on macOS, mount the server first.<br />



