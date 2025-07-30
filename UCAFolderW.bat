@echo off
setlocal enabledelayedexpansion

:: Set the root directory to the location you want the folder to be created, eg, root set to local DOC use (root="%USERPROFILE%\Documents\ProjectFolder") to ucaprod (\\ucaprod\thesis\old\folderBox)
set "root=%USERPROFILE%\Documents\project_folder"

:: Check if parent directory exists and is writable
if not exist "%USERPROFILE%\Documents" (
    echo Error: Parent directory %USERPROFILE%\Documents does not exist
    exit /b 1
)
echo nul > "%USERPROFILE%\Documents\testfile.txt" 2>nul || (
    echo Error: No write permission for %USERPROFILE%\Documents
    exit /b 1
)
del "%USERPROFILE%\Documents\testfile.txt" 2>nul

:: Create root directory if it doesn't exist
mkdir "%root%" 2>nul || (
    echo Failed to create %root%
    exit /b 1
)


:: Create first layer folders
mkdir "%root%\asset"
mkdir "%root%\editorial"
mkdir "%root%\io"
mkdir "%root%\reference"

:: Create asset folder structure
mkdir "%root%\asset\sample_asset"
mkdir "%root%\asset\sample_asset\publish"
mkdir "%root%\asset\sample_asset\publish\lookdev"
mkdir "%root%\asset\sample_asset\publish\model"
mkdir "%root%\asset\sample_asset\publish\rig"
mkdir "%root%\asset\sample_asset\publish\texture"
mkdir "%root%\asset\sample_asset\reference"
mkdir "%root%\asset\sample_asset\work"
mkdir "%root%\asset\sample_asset\work\lookdev"
mkdir "%root%\asset\sample_asset\work\model"
mkdir "%root%\asset\sample_asset\work\rig"
mkdir "%root%\asset\sample_asset\work\texture"

:: Create editorial folder structure
mkdir "%root%\editorial\premiere"
mkdir "%root%\editorial\hiero"
mkdir "%root%\editorial\export"

:: Create io folder structure
mkdir "%root%\io\in"
mkdir "%root%\io\in\YYYY_MM_DD_in_folderName"
mkdir "%root%\io\out"
mkdir "%root%\io\out\YYYY_MM_DD_out_folderName"

:: Create sequence folder structure
mkdir "%root%\sequence"
mkdir "%root%\sequence\seq010_0000"
mkdir "%root%\sequence\seq010_0000\publish"
mkdir "%root%\sequence\seq010_0000\publish\anim"
mkdir "%root%\sequence\seq010_0000\publish\comp"
mkdir "%root%\sequence\seq010_0000\publish\fx"
mkdir "%root%\sequence\seq010_0000\publish\lighting"
mkdir "%root%\sequence\seq010_0000\reference"
mkdir "%root%\sequence\seq010_0000\source"
mkdir "%root%\sequence\seq010_0000\source\audio"
mkdir "%root%\sequence\seq010_0000\source\plates"

mkdir "%root%\sequence\seq010_0000\work"
mkdir "%root%\sequence\seq010_0000\work\anim"
mkdir "%root%\sequence\seq010_0000\work\anim\maya"
mkdir "%root%\sequence\seq010_0000\work\comp"
mkdir "%root%\sequence\seq010_0000\work\comp\nuke"
mkdir "%root%\sequence\seq010_0000\work\fx"
mkdir "%root%\sequence\seq010_0000\work\lighting"
mkdir "%root%\sequence\seq010_0000\work\lighting\maya"

:: Display completion message
echo.
echo The folders have been successfully created at:
echo %root%
echo Note: Duplicate 'sample_asset' for new assets (e.g., 'Gecko', 'Office') and 'shot_template' for new shots (e.g., 'seq020_0010').
echo.

pause