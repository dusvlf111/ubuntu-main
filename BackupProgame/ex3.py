import os
import shutil



#보낼 파일의 위치
file_in = "/home/u/문서/BackupProgame/"
#파일의 종류
file_type = ".zip"
#저장할 위치
backup_in = "/media/u/외장하드 1t/"





#--------------------------------------------------------------
path = file_in
dir = backup_in
#
file_list = os.listdir(path)
# 전체 파일 리스트
print ("전체파일리스트: \n{}".format(file_list),"\n")
# zip 파일 리스트
file_list_zip = [file for file in file_list if file.endswith(".zip")]

print (file_type,"파일리스트:\n {}".format(file_list_zip),"\n------->",path,"\n")

try:
    i = 0 
    while i < len(file_list_zip):
        
            filename = file_list_zip[i]
            fileFormat = file_type
            src = file_in
            dir = backup_in
            shutil.move(src + filename, dir + filename)
            print(i,"번째<"+filename+"> ------------백업을 완료했습니다")
            i+=1
            
            
    print("성공적으로 완료했습니다")
        

      
except Exception as e:
    print(e)

    