# convert to file in zip file

import zipfile

def create_zip(file_names, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_names:
            zipf.write(file)
    print(f"Zipped files into {zip_name}")

# Example usage:
files_to_zip = ['file1.txt', 'file2.txt']
create_zip(files_to_zip, 'my_archive.zip')
