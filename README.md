# Extract Clicker Media

A standalone script to extract embedded media (images, sounds, etc.) from `.clkx` (Clicker Grids) files. This tool decodes base64-encoded media and saves them as standalone files.

## Requirements

- A `.clkx` file to process.
- Supported operating systems:
  - **Windows** for the `.exe` version.
  - **macOS** for the macOS binary version.

## Downloading the Script

1. Go to the **Releases** section of this repository on GitHub.
2. Download the appropriate version for your operating system:
   - **Windows**: `extract_clicker_media-windows-latest.exe`
   - **macOS**: `extract_clicker_media-macos-latest`
3. Save the downloaded file to a convenient location.

## Using the Script

### For Windows Users:

1. Save the `.clkx` file in the same directory as the downloaded script or note its full path.
2. Open a Command Prompt:
   - Press `Win + R`, type `cmd`, and press Enter.
3. Navigate to the directory where the script is saved:
   ```cmd
   cd path\to\directory
4. Run the script with the path to the `.clkx` file as an argument:
   ```cmd
   extract_clicker_media-windows-latest.exe path\to\file.clkx
   ```
5.	The extracted files will be saved in a new folder, named <filename>_extracted, in the same directory as the .clkx file.

### For macOS Users:

1. Save the `.clkx` file in the same directory as the downloaded script or note its full path.  
2. Open a Terminal:
   - Press `Cmd + Space`, type `Terminal`, and press Enter.
3. Navigate to the directory where the script is saved:
   ```bash
    cd path/to/directory
    ```
4. Run the script with the path to the `.clkx` file as an argument:
    ```bash
    ./extract_clicker_media-macos-latest path/to/file.clkx
    ```
5. The extracted files will be saved in a new folder, named <filename>_extracted, in the same directory as the .clkx file.

## Notes

- The script will create a new folder in the same directory as the `.clkx` file to store the extracted media.
- The extracted media files will retain their original file names.
- The script will overwrite any existing files with the same name in the extraction folder.
- The script does not modify the original `.clkx` file.

