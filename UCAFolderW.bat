@echo off
setlocal enabledelayedexpansion

:: Set the root directory to the location you want the folder to be created, eg, root set to local DOC use (root="%USERPROFILE%\Documents\ProjectFolder") to ucaprod (\\ucaprod\thesis\old\folderBox)
set "root=%USERPROFILE%\Documents\ProjectFolder"

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
mkdir "%root%\asset\Assets"
mkdir "%root%\asset\Assets\publish"
mkdir "%root%\asset\Assets\publish\lookdev"
mkdir "%root%\asset\Assets\publish\model"
mkdir "%root%\asset\Assets\publish\rig"
mkdir "%root%\asset\Assets\publish\texture"
mkdir "%root%\asset\Assets\reference"
mkdir "%root%\asset\Assets\work"
mkdir "%root%\asset\Assets\work\lookdev"
mkdir "%root%\asset\Assets\work\model"
mkdir "%root%\asset\Assets\work\rig"
mkdir "%root%\asset\Assets\work\texture"

:: Create editorial folder structure
mkdir "%root%\editorial\VideoEditingFolder"

:: Create io folder structure
mkdir "%root%\io\In"
mkdir "%root%\io\In\YYYY_MM_DD_inFolderName"
mkdir "%root%\io\Out"
mkdir "%root%\io\Out\YYYY_MM_DD_inFolderName"

:: Create sequence folder structure
mkdir "%root%\sequence"
mkdir "%root%\sequence\seq010_0000"
mkdir "%root%\sequence\seq010_0000\Publish"
mkdir "%root%\sequence\seq010_0000\Publish\anim"
mkdir "%root%\sequence\seq010_0000\Publish\comp"
mkdir "%root%\sequence\seq010_0000\Publish\fx"
mkdir "%root%\sequence\seq010_0000\Publish\lighting"
mkdir "%root%\sequence\seq010_0000\Reference"
mkdir "%root%\sequence\seq010_0000\source"
mkdir "%root%\sequence\seq010_0000\source\audio"
mkdir "%root%\sequence\seq010_0000\source\plates"
mkdir "%root%\sequence\seq010_0000\source\anim"
mkdir "%root%\sequence\seq010_0000\source\graded"
mkdir "%root%\sequence\seq010_0000\source\lighting"
mkdir "%root%\sequence\seq010_0000\source\raw"
mkdir "%root%\sequence\seq010_0000\work"
mkdir "%root%\sequence\seq010_0000\work\anim"
mkdir "%root%\sequence\seq010_0000\work\comp"
mkdir "%root%\sequence\seq010_0000\work\fx"
mkdir "%root%\sequence\seq010_0000\work\lighting"

:: Display completion message
echo.
echo The folders have been successfully created at:
echo %root%
echo.

pause