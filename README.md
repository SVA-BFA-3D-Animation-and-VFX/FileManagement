# Automated Project Folder Structure Creation

This tool automates the creation of a standardized folder hierarchy for 3D animation and VFX projects. It is designed to quickly set up directories needed for asset management, editorial work, I/O operations, and sequence organization within a specified root directory.

Folder Structure Documentation made by Shayne Ryan [Link] (https://docs.google.com/document/d/1Xee4Wr14S8Rny-xosLolQS5RyLA3agvIuVNA5MqsC9g/edit?usp=sharing)

# GUI Application: 
folder_setup_gui.app (macOS) and folder_setup_gui.exe (Windows) provide a user-friendly interface to create the full folder structure in the selected **root directory**. It includes buttons to add assets (e.g., Gecko) and shots (e.g., seq020_0010) to the assets and sequence folders.

The GUI generates command-line scripts (add_asset.sh/add_asset.bat and add_shot.sh/add_shot.bat) for manual asset and shot creation. Drag it into the terminal or command line to run it.

## How to use the GUI.APP / GUI.exe
Beta executables may trigger Windows Defender or Chrome warnings.

**GUI.app macOS**: Download FolderSetupGUI.app 
- Move to Applications and double-click to run. 
- Allow in System Settings > Privacy & Security if prompted.
  
**GUI.exe Windows**: Download FolderSetupGUI.exe
- Double-click to run. 
- If Windows Defender flags it when you try to open the .exe, an exception needs to be added:
  Settings > Update & Security > Windows Security > Virus & Threat Protection > Manage Settings > Add an exclusion (select FolderSetupGUI.exe).

**Functionality** 
- "Select Root Directory": Choose where to create the project folder. Works with USB drives, network servers, and local drives.
- "Create Folder Structure": Create the file structure in the selected root directory. If the root is set to //ucaprod/thesis, a project folder with a project code must be set up beforehand.
- “Add New Asset”: to create assets (e.g., desk) in the assets folder. 
- “Add New Shot”: to create shots (e.g., seq020_0010) in the sequence folder.
- Scripts: When the file structure is made, the add_asset.bat/add_asset.sh in assets/ and add_shot.bat/add_shot.sh in sequence/ will be created for manual asset or sequence folder creation.
- Status Label: Will displays the root directory and the location where the folder was created.

## Folder Structure
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
    - Organizes user-specific work in userName with subfolders:
     - publish:
       - anim (alembic_camera, alembic_geometry),
       - comp (composited_image),
       - design (composited_image),
       - fx (alembic_geometry),
       - lighting (composited_image, rendered_image)
    - reference: documents, images, videos
    - work: anim (maya), comp (nuke),design (ae, photoshop), fx (houdini, maya),lighting (houdini, maya)
  
  - **Sequence Folder:**  
    Establishes a `sequence` directory containing a sample sequence `seq010/seq010_0010` (template, duplicate for new shots) with subfolders.
    - `Publish`: anim (alembic_camera, alembic_geometry), audio, comp (composited_image), design (composited_image), fx (alembic_geometry), lighting (composited_image, rendered_image), plates (anim_plate, lighting_plate, source_plate)
    - `Reference`: documents, images, videos
    - `source` (audio, plates),
    - `work`: anim (maya), comp (nuke), design (ae, photoshop), fx (houdini, maya), lighting (houdini, maya)
