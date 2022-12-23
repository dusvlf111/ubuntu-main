import os
import shutil
import datetime as d


in_list=["/home/u/문서/BackupProgame/","0000000000000","000000000000000000000"]
type_list=[".zip","000000000","00000000000"]
up_list=["/media/u/외장하드 1t/","0000000000 ","0000000000000000"]




#보낼 파일의 위치
file_in = in_list[0]

#파일의 종류
file_type = type_list[0]

#저장할 위치
backup_in = up_list[0]



for row in in_list:
    print("\n",row, "\n 보낼 파일 위치 순서대로 0부터 \n", input(in_list[0]))
    

for row in type_list:
    print("\n",row, "\n 파일 종류 순서대로 0부터 \n", input(type_list[0]))

for row in up_list:
    print("\n",row, "\n 저장할 위치 순서대로 0부터 \n", input(up_list[0]))






#---------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------




#-----------------------------------------------------------
file_list = os.listdir(file_in)
# 전체 파일 리스트
print ("전체파일리스트: \n{}".format(file_list),"\n")
# zip 파일 리스트
file_list_zip = [file for file in file_list if file.endswith(file_type)]


print (file_type,"파일리스트:\n {}".format(file_list_zip),"\n------->\n",backup_in,"\n")


    


try:
    
    i = 0 
    while i < len(file_list_zip) and len(file_list_zip)!=0:
            
                filename = file_list_zip[i]
            
                isCurrentPathFileExist = os.path.isfile(file_in+ filename)
               #현재경로에 옮기려는 파일이 존재하는지 확인

                isDestinationFileExist = os.path.isfile(backup_in + filename)

               #도착경로에 동일한 파일이 존재하는지 확인
                if isDestinationFileExist:
                    shutil.move(file_in+ filename, backup_in + filename)
                    print(i+1,"번째<"+filename+"> ------------백업을 완료했습니다")
                    i+=1
                   


                elif isCurrentPathFileExist:
               	#도착경로에 동일한 파일이 존재하지 않는 경우에는 옮긴다.
                    shutil.move(file_in+ filename, backup_in + filename)
                    print(i+1,"번째<"+filename+"> ------------백업을 완료했습니다",":도착경로중복")
                    i+=1        





                   #도착경로에 동일한 파일이 존재하는 경우
                else:
                   print("중복파일의 이름을 바꿉니다")
                   break
                   # file_oldname = os.path(file_in, filename)
                   # file_newname_newfile = os.path (file_in,(d.datetime+file_type))    
                   # os.rename(file_oldname, file_newname_newfile)
            

                    
    

      
except Exception as e:
    print(e)

    
    
    
