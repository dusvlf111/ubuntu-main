import os
import shutil
import pprint as pp


file_in="/home/u/문서/BackupProgame/" #==============옮길 폴더
file_type=".zip"                      #==============파일형태
backup_in="/media/u/외장하드 1t/"     #==============저장할 위치








#---------------------------------------------------------------------------------------------------------------





file_list = os.listdir(file_in)
# 전체 파일 리스트
print("-------------------------------------------------------------------")
print("전체파일리스트:")
pp.pprint (file_list)
# zip 파일 리스트
print("-------------------------------------------------------------------")
file_list_zip = [file for file in file_list if file.endswith(file_type)]

print("파일리스트:")
pp.pprint (file_list_zip)
print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n",backup_in,"\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
print("-------------------------------------------------------------------")

print("확인하셨습니까?")
input()

    



try:
    
    i = 0 
    if len(file_list_zip)>0:
        while i < len(file_list_zip):
                
            filename = file_list_zip[i]
                
            shutil.move(file_in+ filename, backup_in + filename)
            print("(",i+1,"번째)   "+filename+"\n===============백업을 완료했습니다================")
            i+=1

        i = len(file_list_zip)-1
        print("################################################전체 이동하였습니다################################################")

        
    elif len(file_list_zip)==0:
        print("===============================이동할 파일이 없습니다==============================")

      
except Exception as e:
    print("===========================",e,"======================================")

    
    
    
