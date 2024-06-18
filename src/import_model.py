import ellipsis as el
import os


class ImportModel:
    def __init__(self):
        pass

    def import_model(self):
        # log in
        token = el.account.logIn('REMLA13', 'REMLAEllipsis')

        folderId = 'c7894e6f-1a2f-40b2-ab48-01e01e915790'


        #check if the filePath not exists else create it
        if not os.path.exists('./output'):
            os.makedirs('./output')

            
        # download the model.joblib file
        el.path.file.download(pathId = folderId, token = token, filePath='./output/model.joblib')


if __name__ == '__main__':
    ImportModel().import_model()