import os
import requests


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def download_image(url, filepath):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(filepath, 'wb') as f:
            f.write(response.content)
        return True
    except Exception:
        return False


def get_file_extension(url):
    _, ext = os.path.splitext(url.split("/")[-1])
    return ext.lower() if ext else ".jpg"