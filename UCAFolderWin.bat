@echo off
:: UCAFolder.bat: Creates a standardized folder structure for animation/VFX projects
:: in the local Documents folder with project_folder as container for Windows.
setlocal

:: Set the root directory
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

:: Create root directory
mkdir "%root%" 2>nul || (
    echo Failed to create %root%
    exit /b 1
)

:: Create first layer folders
mkdir "%root%\assets" || (echo Failed to create %root%\assets & exit /b 1)
mkdir "%root%\common" || (echo Failed to create %root%\common & exit /b 1)
mkdir "%root%\editorial" || (echo Failed to create %root%\editorial & exit /b 1)
mkdir "%root%\io" || (echo Failed to create %root%\io & exit /b 1)
mkdir "%root%\reference" || (echo Failed to create %root%\reference & exit /b 1)
mkdir "%root%\sandbox" || (echo Failed to create %root%\sandbox & exit /b 1)
mkdir "%root%\sequence" || (echo Failed to create %root%\sequence & exit /b 1)

:: Create asset folder structure with SampleAsset
mkdir "%root%\assets\SampleAsset\publish\lookdev\maya_file" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\publish\model\alembic_geometry" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\publish\model\maya_file" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\publish\rig\alembic_geometry" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\publish\rig\maya_file" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\publish\texture\texture_image" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\reference\documents" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\reference\images" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\reference\videos" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\work\lookdev\maya_file" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\work\model\maya" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\work\model\zbrush" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\work\rig\maya" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\work\texture\maya" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\work\texture\photoshop" || (echo Failed to create asset subdirectories & exit /b 1)
mkdir "%root%\assets\SampleAsset\work\texture\substance" || (echo Failed to create asset subdirectories & exit /b 1)

:: Create add_asset.bat in assets folder
echo @echo off > "%root%\assets\add_asset.bat"
echo setlocal >> "%root%\assets\add_asset.bat"
echo if "%%~1"=="" ( >> "%root%\assets\add_asset.bat"
echo     set /p asset_name=Enter new asset name (e.g., Gecko, Office): >> "%root%\assets\add_asset.bat"
echo ) else ( >> "%root%\assets\add_asset.bat"
echo     set "asset_name=%%~1" >> "%root%\assets\add_asset.bat"
echo ) >> "%root%\assets\add_asset.bat"
echo if "%%asset_name%%"=="" (echo Error: Asset name cannot be empty. ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo echo %%asset_name%% ^| find " " ^>nul ^&^& (echo Error: Asset name cannot contain spaces. ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo set "asset_dir=%%~dp0..\assets\%%asset_name%%" >> "%root%\assets\add_asset.bat"
echo if exist "%%asset_dir%%" (echo Error: Asset '%%asset_name%%' already exists at %%asset_dir%% ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\publish\lookdev\maya_file" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\publish\model\alembic_geometry" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\publish\model\maya_file" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\publish\rig\alembic_geometry" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\publish\rig\maya_file" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\publish\texture\texture_image" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\reference\documents" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\reference\images" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\reference\videos" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\work\lookdev\maya_file" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\work\model\maya" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\work\model\zbrush" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\work\rig\maya" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\work\texture\maya" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\work\texture\photoshop" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo mkdir "%%asset_dir%%\work\texture\substance" ^|^| (echo Failed to create asset subdirectories ^& exit /b 1) >> "%root%\assets\add_asset.bat"
echo echo Asset '%%asset_name%%' created at: %%asset_dir%% >> "%root%\assets\add_asset.bat"
echo if "%%~1"=="" pause >> "%root%\assets\add_asset.bat"

:: Create common folder structure
mkdir "%root%\common\scripts" || (echo Failed to create %root%\common\scripts & exit /b 1)

:: Create editorial folder structure
mkdir "%root%\editorial\audio" || (echo Failed to create %root%\editorial\audio & exit /b 1)
mkdir "%root%\editorial\edits" || (echo Failed to create %root%\editorial\edits & exit /b 1)
mkdir "%root%\editorial\edls" || (echo Failed to create %root%\editorial\edls & exit /b 1)
mkdir "%root%\editorial\exports" || (echo Failed to create %root%\editorial\exports & exit /b 1)
mkdir "%root%\editorial\footage" || (echo Failed to create %root%\editorial\footage & exit /b 1)
mkdir "%root%\editorial\stills" || (echo Failed to create %root%\editorial\stills & exit /b 1)
mkdir "%root%\editorial\storyboards" || (echo Failed to create %root%\editorial\storyboards & exit /b 1)

:: Create io folder structure
mkdir "%root%\io\in\YYYY_MM_DD_in_folderName" || (echo Failed to create io subdirectories & exit /b 1)
mkdir "%root%\io\out\YYYY_MM_DD_out_folderName" || (echo Failed to create io subdirectories & exit /b 1)

:: Create reference folder structure
mkdir "%root%\reference\documents" || (echo Failed to create %root%\reference\documents & exit /b 1)
mkdir "%root%\reference\images" || (echo Failed to create %root%\reference\images & exit /b 1)
mkdir "%root%\reference\videos" || (echo Failed to create %root%\reference\videos & exit /b 1)

:: Create sandbox folder structure
mkdir "%root%\sandbox\userName\publish\anim\alembic_camera" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\publish\anim\alembic_geometry" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\publish\comp\composited_image" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\publish\design\composited_image" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\publish\fx\alembic_geometry" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\publish\lighting\composited_image" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\publish\lighting\rendered_image" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\reference\documents" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\reference\images" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\reference\videos" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\work\anim\maya" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\work\comp\nuke" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\work\design\ae" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\work\design\photoshop" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\work\fx\houdini" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\work\fx\maya" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\work\lighting\houdini" || (echo Failed to create sandbox subdirectories & exit /b 1)
mkdir "%root%\sandbox\userName\work\lighting\maya" || (echo Failed to create sandbox subdirectories & exit /b 1)

:: Create sequence folder structure
mkdir "%root%\sequence\seq010\seq010_0010\publish\anim\alembic_camera" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\anim\alembic_geometry" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\audio" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\comp\composited_image" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\design\composited_image" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\fx\alembic_geometry" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\lighting\composited_image" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\lighting\rendered_image" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\plates\anim_plate" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\plates\lighting_plate" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\publish\plates\source_plate" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\reference\documents" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\reference\images" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\reference\videos" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\work\anim\maya" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\work\comp\nuke" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\work\design\ae" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\work\design\photoshop" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\work\fx\houdini" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\work\fx\maya" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\work\lighting\houdini" || (echo Failed to create sequence subdirectories & exit /b 1)
mkdir "%root%\sequence\seq010\seq010_0010\work\lighting\maya" || (echo Failed to create sequence subdirectories & exit /b 1)

:: Create add_shot.bat in sequence folder
echo @echo off > "%root%\sequence\add_shot.bat"
echo setlocal >> "%root%\sequence\add_shot.bat"
echo if "%%~1"=="" ( >> "%root%\sequence\add_shot.bat"
echo     set /p shot_name=Enter new shot name (e.g., seq020_0010): >> "%root%\sequence\add_shot.bat"
echo     if "%%shot_name%%"=="" ( >> "%root%\sequence\add_shot.bat"
echo         dir "%%~dp0..\sequence" ^| find "seq" ^> temp.txt >> "%root%\sequence\add_shot.bat"
echo         for /f "tokens=*" %%%%i in (temp.txt) do set "last_seq=%%%%i" >> "%root%\sequence\add_shot.bat"
echo         set /a "seq_num=10" >> "%root%\sequence\add_shot.bat"
echo         if defined last_seq ( >> "%root%\sequence\add_shot.bat"
echo             for /f "tokens=2 delims=seq" %%%%j in ("%%last_seq%%") do set /a "seq_num=%%%%j+10" >> "%root%\sequence\add_shot.bat"
echo         ) >> "%root%\sequence\add_shot.bat"
echo         set "shot_name=seq%%seq_num%%_0010" >> "%root%\sequence\add_shot.bat"
echo         del temp.txt >> "%root%\sequence\add_shot.bat"
echo     ) >> "%root%\sequence\add_shot.bat"
echo ) else ( >> "%root%\sequence\add_shot.bat"
echo     set "shot_name=%%~1" >> "%root%\sequence\add_shot.bat"
echo ) >> "%root%\sequence\add_shot.bat"
echo if "%%shot_name%%"=="" (echo Error: Shot name cannot be empty. ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo echo %%shot_name%% ^| find " " ^>nul ^&^& (echo Error: Shot name cannot contain spaces. ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo set "shot_dir=%%~dp0..\sequence\%%shot_name%%" >> "%root%\sequence\add_shot.bat"
echo if exist "%%shot_dir%%" (echo Error: Shot '%%shot_name%%' already exists at %%shot_dir%% ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\anim\alembic_camera" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\anim\alembic_geometry" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\audio" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\comp\composited_image" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\design\composited_image" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\fx\alembic_geometry" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\lighting\composited_image" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\lighting\rendered_image" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\plates\anim_plate" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\plates\lighting_plate" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\publish\plates\source_plate" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\reference\documents" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\reference\images" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\reference\videos" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\work\anim\maya" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\work\comp\nuke" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\work\design\ae" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\work\design\photoshop" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\work\fx\houdini" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\work\fx\maya" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\work\lighting\houdini" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo mkdir "%%shot_dir%%\work\lighting\maya" ^|^| (echo Failed to create sequence subdirectories ^& exit /b 1) >> "%root%\sequence\add_shot.bat"
echo echo Shot '%%shot_name%%' created at: %%shot_dir%% >> "%root%\sequence\add_shot.bat"
echo if "%%~1"=="" pause >> "%root%\sequence\add_shot.bat"

:: Display completion message
echo.
echo The folders have been successfully created at:
echo %root%
echo Note: Duplicate 'SampleAsset' for new assets (e.g., 'Gecko', 'Office') and 'seq010' for new shots (e.g., 'seq020_0010').
echo Use 'add_asset.bat' in 'assets' or 'add_shot.bat' in 'sequence' to create new assets or shots.
echo.

pause