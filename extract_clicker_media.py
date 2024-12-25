import os
import base64
import sys
from xml.etree.ElementTree import ElementTree


def extract_clicker_media(file_path):
    """
    Extract embedded media (images, sounds) from a .clkx Clicker file.

    :param file_path: Path to the .clkx file.
    """
    try:
        base_name, ext = os.path.splitext(file_path)
        ext = ext.lower()

        if ext not in ['.clkx', '.clkk', '.clkt']:
            print("Error: The file does not appear to be a valid Clicker file.")
            return

        print(f"Opening {file_path}...")
        tree = ElementTree()
        tree.parse(file_path)

        output_dir = f"{base_name}_extracted"
        os.makedirs(output_dir, exist_ok=True)
        print(f"Extracting to directory: {output_dir}")

        media_counter = 1

        # Extract sounds
        for sound in tree.findall("crickdata/sound"):
            if sound.get("link") == "Embed":
                file_name = sound.get("name", str(media_counter))
                file_type = sound.get("filetype", "unknown")
                output_file = os.path.join(output_dir, f"{file_name}.{file_type}")

                print(f"Writing sound: {output_file}")
                with open(output_file, "wb") as f:
                    f.write(base64.b64decode(sound.find("base64").text))
                media_counter += 1

        # Extract images
        for pic in tree.findall("crickdata/pic"):
            pic_name = pic.get("name", "None")
            for picdata in pic.findall("picdata"):
                if picdata.get("link") == "Embed":
                    file_name = pic_name or picdata.get("state", "Unknown")
                    file_type = picdata.get("filetype", "unknown")
                    output_file = os.path.join(
                        output_dir, f"{file_name}_{media_counter}.{file_type}"
                    )

                    print(f"Writing image: {output_file}")
                    with open(output_file, "wb") as f:
                        f.write(base64.b64decode(picdata.find("base64").text))
                    media_counter += 1

        print(f"Extraction completed. Media saved to: {output_dir}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file.clkx>")
    else:
        extract_clicker_media(sys.argv[1])