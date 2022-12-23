
import os




path = "/home/u/문서/BackupProgame"
file_list = os.listdir(path)
print ("file_list: {}".format(file_list))
# 전체 파일 리스트
file_list_zip = [file for file in file_list if file.endswith(".zip")]

print ("file_list: {}".format(file_list_zip))

