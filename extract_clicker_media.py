import os
import base64
import sys
from xml.etree.ElementTree import ElementTree

def extract_clicker_media(file_path, base_output_dir=None):
    """
    Extract embedded media (images, sounds, videos) from a .clkx Clicker file.
    
    Args:
        file_path: Path to the .clkx file
        base_output_dir: Optional base directory for output. If None, creates directory next to source file
    """
    try:
        base_name, ext = os.path.splitext(file_path)
        ext = ext.lower()
        if ext not in ['.clkx', '.clkk', '.clkt']:
            print(f"Error: {file_path} does not appear to be a valid Clicker file.")
            return

        # Create output directory based on clicker document name
        if base_output_dir:
            doc_name = os.path.splitext(os.path.basename(file_path))[0]
            output_dir = os.path.join(base_output_dir, doc_name)
        else:
            output_dir = f"{base_name}_extracted"
            
        os.makedirs(output_dir, exist_ok=True)
        print(f"\nProcessing: {file_path}")
        print(f"Extracting to directory: {output_dir}")

        tree = ElementTree()
        tree.parse(file_path)
        media_counter = 1

        # Extract sounds
        for sound in tree.findall(".//sound"):
            if sound.get("link") == "Embed":
                file_name = sound.get("name", f"sound_{media_counter}")
                file_type = sound.get("filetype", "unknown")
                output_file = os.path.join(output_dir, f"{file_name}.{file_type}")
                print(f"Writing sound: {output_file}")
                with open(output_file, "wb") as f:
                    f.write(base64.b64decode(sound.find("base64").text))
                media_counter += 1

        # Extract images
        for pic in tree.findall(".//pic"):
            pic_name = pic.get("name", "None")
            for picdata in pic.findall("picdata"):
                if picdata.get("link") == "Embed":
                    file_name = pic_name or picdata.get("state", f"image_{media_counter}")
                    file_type = picdata.get("filetype", "unknown")
                    output_file = os.path.join(
                        output_dir, f"{file_name}_{media_counter}.{file_type}"
                    )
                    print(f"Writing image: {output_file}")
                    with open(output_file, "wb") as f:
                        f.write(base64.b64decode(picdata.find("base64").text))
                    media_counter += 1

        # Extract videos
        for video in tree.findall(".//video"):
            if video.get("link") == "Embed":
                file_name = video.get("name", f"video_{media_counter}")
                file_type = video.get("filetype", "unknown")
                output_file = os.path.join(output_dir, f"{file_name}.{file_type}")
                print(f"Writing video: {output_file}")
                with open(output_file, "wb") as f:
                    f.write(base64.b64decode(video.find("base64").text))
                media_counter += 1

        print(f"Extraction completed. Media saved to: {output_dir}")
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def process_directory(path):
    """
    Recursively process a directory for Clicker files.
    
    Args:
        path: Directory path to process
    """
    if os.path.isfile(path):
        extract_clicker_media(path)
        return

    base_output_dir = os.path.join(path, "extracted_media")
    os.makedirs(base_output_dir, exist_ok=True)
    
    success_count = 0
    fail_count = 0
    
    for root, _, files in os.walk(path):
        for file in files:
            if file.lower().endswith(('.clkx', '.clkk', '.clkt')):
                file_path = os.path.join(root, file)
                if extract_clicker_media(file_path, base_output_dir):
                    success_count += 1
                else:
                    fail_count += 1
    
    print(f"\nProcessing complete!")
    print(f"Successfully processed: {success_count} files")
    if fail_count > 0:
        print(f"Failed to process: {fail_count} files")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.clkx or directory>")
    else:
        process_directory(sys.argv[1])