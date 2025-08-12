#!/bin/bash

# Set the root directory to the local Documents folder with project_folder as container
root="$HOME/Documents/project_folder"

# Check if parent directory is writable
if [ ! -w "$(dirname "$root")" ]; then
    echo "Error: No write permission for $(dirname "$root")"
    exit 1
fi

# Create root directory if it doesn't exist
mkdir -p "$root" || { echo "Failed to create $root"; exit 1; }

# Create first layer folders
mkdir -p "${root}/assets" || { echo "Failed to create ${root}/assets"; exit 1; }
mkdir -p "${root}/common" || { echo "Failed to create ${root}/common"; exit 1; }
mkdir -p "${root}/editorial" || { echo "Failed to create ${root}/editorial"; exit 1; }
mkdir -p "${root}/io" || { echo "Failed to create ${root}/io"; exit 1; }
mkdir -p "${root}/reference" || { echo "Failed to create ${root}/reference"; exit 1; }
mkdir -p "${root}/sandbox" || { echo "Failed to create ${root}/sandbox"; exit 1; }
mkdir -p "${root}/sequence" || { echo "Failed to create ${root}/sequence"; exit 1; }

# Create asset folder structure
mkdir -p "${root}/assets/SampleAsset/publish/lookdev/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/publish/model/alembic_geometry" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/publish/model/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/publish/rig/alembic_geometry" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/publish/rig/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/publish/texture/texture_image" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/reference/documents" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/reference/images" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/reference/videos" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/work/lookdev/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/work/model/maya" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/work/model/zbrush" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/work/rig/maya" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/work/texture/maya" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/work/texture/photoshop" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${root}/assets/SampleAsset/work/texture/substance" || { echo "Failed to create asset subdirectories"; exit 1; }

# Create add_asset.sh in assets folder
cat > "${root}/assets/add_asset.sh" << 'EOF'
#!/bin/bash

# Use command-line argument or prompt for asset name
if [ $# -eq 1 ]; then
    asset_name="$1"
else
    read -p "Enter new asset name (e.g., Gecko, Office): " asset_name
    [ -z "$asset_name" ] && asset_name="SampleAsset"
fi

# Validate input
if [ -z "$asset_name" ]; then
    echo "Error: Asset name cannot be empty."
    exit 1
fi
if [[ "$asset_name" =~ \  ]]; then
    echo "Error: Asset name cannot contain spaces."
    exit 1
fi

# Set asset directory
asset_dir="$(dirname "$(dirname "$0")")/assets/$asset_name"

# Check if asset already exists
if [ -d "$asset_dir" ]; then
    echo "Error: Asset '$asset_name' already exists at $asset_dir"
    exit 1
fi

# Create asset folder structure
mkdir -p "${asset_dir}/publish/lookdev/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/publish/model/alembic_geometry" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/publish/model/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/publish/rig/alembic_geometry" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/publish/rig/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/publish/texture/texture_image" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/reference/documents" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/reference/images" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/reference/videos" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/work/lookdev/maya_file" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/work/model/maya" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/work/model/zbrush" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/work/rig/maya" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/work/texture/maya" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/work/texture/photoshop" || { echo "Failed to create asset subdirectories"; exit 1; }
mkdir -p "${asset_dir}/work/texture/substance" || { echo "Failed to create asset subdirectories"; exit 1; }

echo "Asset '$asset_name' created at: $asset_dir"
[ $# -eq 0 ] && read -p "Press Enter to continue..."
EOF
chmod +x "${root}/assets/add_asset.sh" || { echo "Failed to make add_asset.sh executable"; exit 1; }

# Create common folder structure
mkdir -p "${root}/common/scripts" || { echo "Failed to create ${root}/common/scripts"; exit 1; }

# Create editorial folder structure
mkdir -p "${root}/editorial/audio" || { echo "Failed to create ${root}/editorial/audio"; exit 1; }
mkdir -p "${root}/editorial/edits" || { echo "Failed to create ${root}/editorial/edits"; exit 1; }
mkdir -p "${root}/editorial/edls" || { echo "Failed to create ${root}/editorial/edls"; exit 1; }
mkdir -p "${root}/editorial/exports" || { echo "Failed to create ${root}/editorial/exports"; exit 1; }
mkdir -p "${root}/editorial/footage" || { echo "Failed to create ${root}/editorial/footage"; exit 1; }
mkdir -p "${root}/editorial/stills" || { echo "Failed to create ${root}/editorial/stills"; exit 1; }
mkdir -p "${root}/editorial/storyboards" || { echo "Failed to create ${root}/editorial/storyboards"; exit 1; }

# Create io folder structure
mkdir -p "${root}/io/in/YYYY_MM_DD_in_folderName" || { echo "Failed to create io subdirectories"; exit 1; }
mkdir -p "${root}/io/out/YYYY_MM_DD_out_folderName" || { echo "Failed to create io subdirectories"; exit 1; }

# Create reference structure
mkdir -p "${root}/reference/documents" || { echo "Failed to create ${root}/reference/documents"; exit 1; }
mkdir -p "${root}/reference/images" || { echo "Failed to create ${root}/reference/images"; exit 1; }
mkdir -p "${root}/reference/videos" || { echo "Failed to create ${root}/reference/videos"; exit 1; }

# Create sandbox structure
mkdir -p "${root}/sandbox/userName/publish/anim/alembic_camera" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/publish/anim/alembic_geometry" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/publish/comp/composited_image" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/publish/design/composited_image" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/publish/fx/alembic_geometry" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/publish/lighting/composited_image" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/publish/lighting/rendered_image" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/reference/documents" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/reference/images" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/reference/videos" || { echo "Failed to create sandbox subdirectories"; exit 1; }
mkdir -p "${root}/sandbox/userName/work/anim/maya" || { echo "Failed to create