
import requests
import zipfile
from time import sleep
import os

def download_file_from_google_drive(file_id, dest_path):
    URL = "https://drive.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    
    # Save the file
    with open(dest_path, "wb") as f:
        for chunk in response.iter_content(1024):
            if chunk:
                f.write(chunk)
    print(f"Downloaded {dest_path}")

# Download PyBullet assets if they don't exist
if not os.path.exists("ur5e/ur5e.urdf"):
    os.makedirs("ur5e", exist_ok=True)
    
    files_to_download = {
        "ur5e.zip": "1Cc_fDSBL6QiDvNT4dpfAEbhbALSVoWcc",
        "robotiq_2f_85.zip": "1yOMEm-Zp_DL3nItG9RozPeJAmeOldekX",
        "bowl.zip": "1GsqNLhEl9dd4Mc3BM0dX3MibOI1FVWNM"
    }
    
    for filename, file_id in files_to_download.items():
        download_file_from_google_drive(file_id, filename)
        
        # Unzip the files
        with zipfile.ZipFile(filename, "r") as zip_ref:
            zip_ref.extractall(".")
        os.remove(filename)
        print(f"Extracted {filename}")

os.system("nvidia-smi")

print("Setup complete.")