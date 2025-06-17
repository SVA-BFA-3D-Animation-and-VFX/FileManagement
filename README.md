# Batch Script: Automated Project Folder Structure Creation

This batch script automates the creation of a standardized folder hierarchy for a project. It is designed to quickly set up directories needed for asset management, editorial work, I/O operations, and sequence organization within a specified root directory.

## What the Script Does

- **Sets a Root Directory:**  
  The script defines a root folder location (`\\ucaprod\thesis\old\folderBox`) where all new folders will be created.

- **Creates Top-Level Folders:**  
  It generates four main folders:  
  - `asset`
  - `editorial`
  - `io`
  - `reference`

- **Builds Subfolder Structures:**  
  - **Asset Folder:**  
    - Organizes assets into `Assets`, with further subdivisions for `publish` (lookdev, model, rig, texture), `reference`, and `work` (lookdev, model, rig, texture).
  - **Editorial Folder:**  
    - Creates a `VideoEditingFolder` for editorial tasks.
  - **I/O Folder:**  
    - Sets up `In` and `Out` folders, each with a placeholder for dated subfolders (`YYYY_MM_DD_inFolderName`).
  - **Sequence Folder:**  
    - Establishes a `sequence` directory containing a sample sequence (`seq010_0000`) with subfolders for `Publish` (anim, comp, fx, lighting), `Reference`, `source` (audio, plates, anim, graded, lighting, raw), and `work` (anim, comp, fx, lighting).

- **Completion Message:**  
  After creating all directories, the script displays a message indicating successful completion and the root location.

## How to Use

1. **Edit the Root Path (Optional):**  
   If you want to use a different root directory, change the `root` variable at the top of the script.
2. **Save the Script:**  
   Copy the script into a text editor and save it with a `.bat` extension (e.g., `create_folders.bat`).
3. **Run the Script:**  
   Double-click the `.bat` file or execute it from the command prompt.  
   The folders will be created automatically at the specified root location.

