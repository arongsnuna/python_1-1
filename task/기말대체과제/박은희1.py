#1. 사용자로부터 파일 이름 입력받기
#1-1. 만약 사용자가 빈 문자열을 입력한다면 빈 문자열이 안될때까지 파일이름을 입력받도록하기
#2. 사용자로부터 검색할 문자열 입력받기
#2-1. 만약 사용자가 빈 문자열을 입력한다면 빈 문자열이 안될때까지 검색할 문자열을 입력받도라록 하기

#3. 파일의 모든 내용을 리스트로 구성하는 함수 (makeFileList)
#3-1. readlines 함수를 이용해 파일의 모든 내용을 리스트로 만들고 rstrip함수를 이용해 줄바꿈문자를 제거해준다
#3-2. 이때 예외처리를 통해서 UnicodeDecodeError가 날때 utf-8로 인코딩하여 리스트를 만들도록 한다.
#3-3. 파일이 없을때는 예외처리를 통해 파일이 없음을 출력하고 스크립트 종료

#4. 한줄의 문자열과 검색할 문자열의 위치를 튜플로 구성해서 반환하는 함수 (makeLocationTuple)
#4-1. 빈튜플하나와 i=0를 만든다. 이때 i는 한줄의 문자열부터 슬라이싱하기전까지의 길이이다.
#4-2. 한줄에서 검색할 문자열의 위치(=num)를 찾는다
#4-2. 그 문자열이 한줄에서 없을때까지
#4-3-1. 튜플에 num+1+i을 추가하고
#4-3-2. 한줄을 num부터 끝까지 슬라이싱하고
#4-3-3. i += (num+검색할문자열의길이)를 구하고
#4-2-3. 그 슬라이싱한 한줄에서 검색할 문자열의 위치(=num)를 찾는 과정을 반복한다
#4-3. 튜플을 반환한다

#5. 반환되는 튜플과 한줄의 문자열을 묶어서 리스트를 만드는 함수 (tupleAndStrList)

#6. 빈 딕셔너리를 만들고
#6-1. 만약 검색할 문자열이 있으면 인덱스+1값를 키로 설정하고 tupleAndStrList의 값을 값으로 설정하여 딕셔너리에 넣는다.
#6-2. 이 과정을 fileList길이만큼 반복한다.
#딕셔너리가 만들어짐

#7-1. 키와 값이 있으면 키와 값을 ':'으로 연결하여 출력한다.
#8-2. 키와 값이 없으면 검색할 문자열이 파일에서 찾을수없다고 출력한다.

import sys

filename = input("파일 이름을 입력하세요: ")
if filename == '':
    while filename == '':
        filename = input("파일 이름을 입력하세요: ")

searchStr = input("검색할 문자열을 입력하세요: ")
if searchStr == '':
    while searchStr == '':
        searchStr = input("검색할 문자열을 입력하세요: ")



def makeFileList(filename):
    try:
        f = open(filename)
        fileList = f.readlines()
        for i in range(len(fileList)):
            fileList[i] = fileList[i].rstrip()
        return fileList   
    except UnicodeDecodeError:
        f = open(filename, encoding="utf-8")
        fileList = f.readlines()
        for i in range(len(fileList)):
            fileList[i]=fileList[i].rstrip()
        return fileList
    except FileNotFoundError:
        print("파일이 없음")
        sys.exit()

fileList = makeFileList(filename)

def makeLocationTuple(line):
    locationTuple = ()
    i=0
    num = line.find(searchStr)
    while num != -1:
        locationTuple = locationTuple + (num+1+i,)
        line = line[num+len(searchStr):]
        i += (num+len(searchStr))
        num = line.find(searchStr)
    return locationTuple

def tupleAndStrList(line):
    return [makeLocationTuple(line)] + [line]

d={}
for t in range(len(fileList)):
    if len(makeLocationTuple(fileList[t])) != 0:
        d[t+1] = tupleAndStrList(fileList[t])

if len(d) != 0:
    for k, v in d.items():
        print(k,v[0],v[1],sep=' : ')
        
else:
    print(searchStr,"을(를) 파일에서 찾을 수 없습니다.")
