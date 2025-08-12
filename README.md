# Automated Project Folder Structure Creation

This batch script automates the creation of a standardized folder hierarchy for a project. It is designed to quickly set up directories needed for asset management, editorial work, I/O operations, and sequence organization within a specified root directory.

# GUI Application: 
FolderSetupGUI.app (macOS) and FolderSetupGUI.exe (Windows) provide a user-friendly interface to create the full folder structure in ~/Documents/project_folder, add new assets (using SampleAsset as a template), and add new shots (using seq010/seq010_0010 with incremental naming, e.g., seq020_0010). 

The GUI generates command-line scripts (add_asset.sh/add_asset.bat and add_shot.sh/add_shot.bat) for manual asset and shot creation.

## What the Script Does

- **Sets a Root Directory:**  
UCAFolderMac.sh: Creates the folder structure on macOS in "~/Documents/ProjectFolder". <br />
UCAFolderW.bat: Creates the same structure on Windows in "%USERPROFILE%\Documents\ProjectFolder" (e.g., C:\Users\YourUsername\Documents\ProjectFolder).

 **Folder Structure**  
- **Top-Level Folders:**  
  It generates five main folders:  
  - `asset`
  - `common`
  - `editorial`
  - `io`
  - `reference`
  - `sandbox`
  - `sequence`

- **Subfolder:**  
  - **Asset:**  
      Organizes assets into `SampleAsset` (template, duplicate for new assets), with further subdivisions.
    -  `publish`: lookdev (maya_file), model (alembic_geometry, maya_file), rig (alembic_geometry, maya_file), texture (texture_image),
    -  `reference`: documents, images, videos,
    -  `work`: lookdev (maya_file), model (maya, zbrush), rig (maya), texture (maya, photoshop, substance).
    -  Includes add_asset.sh/add_asset.bat for creating new assets.
    -  
 - **Common:**  
    - Contains a scripts subfolder for shared scripts.
      
  - **Editorial Folder:**
    - audio, edits, edls, exports, footage, stills, storyboards
      
  - **I/O Folder:**  
    - Sets up `In` and `Out` folders, each with a placeholder for dated subfolders (`YYYY_MM_DD_in/out_FolderName`).

  - **Refference:**  
    - documents, images, videos
      
  - **Sandbox:**  
    -Organizes user-specific work in userName with subfolders:
    publish: anim (alembic_camera, alembic_geometry), comp (composited_image), design (composited_image), fx (alembic_geometry),lighting (composited_image, rendered_image)
    reference: documents, images, videos
    work: anim (maya), comp (nuke),design (ae, photoshop), fx (houdini, maya),lighting (houdini, maya)
  
  - **Sequence Folder:**  
    Establishes a `sequence` directory containing a sample sequence `seq010/seq010_0010` (template, duplicate for new shots) with subfolders.
    - `Publish`: anim (alembic_camera, alembic_geometry), audio, comp (composited_image), design (composited_image), fx (alembic_geometry), lighting (composited_image, rendered_image), plates (anim_plate, lighting_plate, source_plate)
    - `Reference`: documents, images, videos
    - `source` (audio, plates),
    - `work`: anim (maya), comp (nuke), design (ae, photoshop), fx (houdini, maya), lighting (houdini, maya)
    - Includes add_shot.sh/add_shot.bat for creating new shots.

- **Completion Message:**  
  - The GUI displays a status message indicating successful folder creation and the root location.
  - Command-line scripts display a message confirming the creation of the folder structure, new assets, or new shots.

## How to Use

**GUI.app macOS**: Download FolderSetupGUI.app 
Move to Applications and double-click to run. 
Allow in System Settings > Privacy & Security if prompted. 
**GUI.exe Windows**: Download FolderSetupGUI.exe from GitHub or Google Drive. Double-click to run. 
Click “Run anyway” if prompted by Windows Defender. 

**GUI Usage** 
Click “Create Folder Structure” to set up project_folder. 
Use “Add New Asset” to create assets (e.g., Gecko). 
Use “Add New Shot” to create shots (e.g., seq020_0010).

**Windows (UCAFolderW.bat)**
1. **Save the Script:**  
   Copy the script into a text editor and save it with a `.bat` extension (e.g., `UCAFolderW.bat`).
2. **Run the Script:**  
   Double-click the `.bat` file or execute it from the command prompt.  
   The folders will be created automatically at the specified root location.
   
**macOS (UCAFolderMac.sh)**

1. **Save the Script:**  
   Copy the script into a text editor and save it with a `.sh` extension (e.g., `UCAFolderMac.sh`).
2. **Make the script executable** <br />
   chmod +x UCAFolderMac.sh
3. **Run the Script:** <br />
   cd to the script folder and enter ./UCAFolderMac.sh (this is the script file name)

**Change Root Directory**  <br />
Example for a network server:<br />
Windows: Edit root in UCAFolder.bat, line 5 (e.g., set "root=\\ucaprod\thesis\ProjectFolder"). <br />
macOS: Edit root in UCAFolderMac.sh line 4 (e.g., root="/Volumes/thesis/ProjectFolder").<br />
For network servers on macOS, mount the server first.<br />



