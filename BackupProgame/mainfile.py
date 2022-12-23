import os
import shutil


#-------------------------------------------<ex1pass>-------------------------------------------------


# 백업할 파일의 위치
path = "/home/u/문서/BackupProgame" 
file_list = os.listdir(path)
print ("file_list: {}".format(file_list))
# 전체 파일 리스트
file_list_zip = [file for file in file_list if file.endswith(".zip")]
# 보낼 파일의 종류의 리스트


# 코드는 매우 간단하다.

# 현재 디렉토리에 있는 모든 파일(디렉토리) 리스트를 가져온다.

# 실행 결과는 다음과 같다.

#-------------------------------------------<ex2pass>-------------------------------------------------

filename = 'moveTest'
fileFormat = '.zip'
src = "/home/u/바탕화면/backupfile"  #현재 파일 위치
destination = "F:/media/u/외장하드 1t"  #옮겨지는 파일 위치
shutil.move(src + filename, dir + filename)
#-------------------------------------------<ex3>-------------------------------------------------





#-------------------------------------------<ex4>-------------------------------------------------



# 파일 이름 변경


file_oldname = os.path.join("c:\\Folder-1", "OldFileName.txt")
file_newname_newfile = os.path.join("c:\\Folder-1", "NewFileName.NewExtension")

os.rename(file_oldname, file_newname_newfile)





#-------------------------------------------<ex5>-------------------------------------------------





try:
	
    isCurrentPathFileExist = os.path.isfile(src + filename + fileFormat)
    #현재경로에 옮기려는 파일이 존재하는지 확인
    isDestinationFileExist = os.path.isfile(destination + filename + fileFormat)
    #도착경로에 동일한 파일이 존재하는지 확인
    if isCurrentPathFileExist:
    	#도착경로에 동일한 파일이 존재하지 않는 경우에는 옮긴다.
        if not isDestinationFileExist:
            shutil.move(src + filename + fileFormat, destination + filename + fileFormat)
        #도착경로에 동일한 파일이 존재하는 경우
        else:
            i = 1
            while True:
                if os.path.isfile(destination + filename + " ({})".format(i) + fileFormat):
                    i += 1
                else:
                    break
            shutil.move(src + filename + fileFormat, destination + filename + " ({})".format(i) + fileFormat)




except Exception as e:
    print(e)