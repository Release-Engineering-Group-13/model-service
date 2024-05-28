import os
import ellipsis as el

def fetch_model():
    """Downloads pretrained model from remote drive."""

    # Ensure the directory exists
    directory = 'model'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Download pretrained model
    el.path.file.download(pathId='c7894e6f-1a2f-40b2-ab48-01e01e915790', filePath=directory+'/model.joblib')

if __name__ == "__main__":
    fetch_model()
