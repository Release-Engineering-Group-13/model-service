import os
import ellipsis as el


def fetch_model():
    """Downloads pretrained model from remote drive."""

    # Ensure the directory exists
    directory = 'model'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Download pretrained model
    folderId='12b2838a-fa7e-4215-bb50-069df2879311'
    listFolder = el.path.folder.listFolder(pathId=folderId)
    for file in listFolder['result']:
        el.path.file.download(pathId=file['id'], filePath='model/'+file['name'])
    

if __name__ == "__main__":
    fetch_model()
