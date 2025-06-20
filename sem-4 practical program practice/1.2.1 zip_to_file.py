# convert to zip file in file

import zipfile

def unzip_file(zip_name, extract_to='.'):
    with zipfile.ZipFile(zip_name, 'r') as zipf:
        zipf.extractall(path=extract_to)
    print(f"Extracted files to {extract_to}")
# Example usage:
unzip_file('my_archive.zip')    
