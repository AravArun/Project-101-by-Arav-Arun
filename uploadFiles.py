import os 
import dropbox
from dropbox.files import WriteMode

class TransferData :
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self,dropbox_path,file_to, file_from, local_path,relative_path):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)

        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.Ax-JPcE2Isl8bbmruOrJjU4YKOyBs5fmF3qmbtndGg2V4MqTfpraeZF5lbP2x8HIDHU61wqKQbJ28TeLe2P9nWfZkmcle_V9OhLtb1oJenxwRt-zDO1cPTSxhnKTwi0I5SjW9JVSNCG1'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main() 

                



