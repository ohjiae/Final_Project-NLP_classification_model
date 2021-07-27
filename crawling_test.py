#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
final_project

1. data crawling


"""

import urllib.request
import urllib.parse
import requests
from bs4 import BeautifulSoup

res = requests.get("http://google.com")
res.raise_for_status()
print('웹 연결 성공...')
#문제 생기면 여기서 바로 끝남! 쓸데없는 시간 낭비를 줄여줌



# 지은
# -*- coding: utf-8 -*-
"""
Final project : complaints analysis

1. crawling - data load
2. data preprocessing
3. metadata analysis
4. modeling
5. evaluating
"""

#찬영(2021.07.27 pm 18:00 추가)
from selenium import webdriver

#크롬 드라이버 load(각자 설치해놓으신 위치에 맞게!)
#driver = webdriver.Chrome("D:\\Naver MYBOX\\Bigdata visualization course\\ITWILL/5.Tensorflow/workspace/chap07_Face_detection/lecture00_web_crawling/chromedriver.exe")
driver.get("https://www.epeople.go.kr/nep/pttn/gnrlPttn/pttnSmlrCaseList.npaid") # 자동화 제어 사이트(크롤링 대상 사이트) open

#원하는 페이지를 여는 코드
driver.find_element_by_xpath('//*[@id="frm"]/div[1]/div[2]/a[2]/span').click()#상세 검색으로 늘려줍니다
driver.find_element_by_xpath('//*[@id="searchInstType"]').click()
driver.find_element_by_xpath('')# 여기서 콤보 박스를 우리가 고를 수 있도록 코드를 짜보죠
driver.find_element_by_xpath('')
driver.find_element_by_xpath('//*[@id="frm"]/div[1]/div[1]/div[4]/button[1]').click#검색을 누릅니다

driver.close() #자동화 제어 사이트 종료


# selenum 사용
from selenium import webdriver # 라이브러리에서 사용하는 모듈만 호출
import os 

pwd = os.getcwd() # 현재 경로 
print(pwd)
    

def complain_crawler(name) : 
    # 1. dirver 경로/파일 지정
    # 각자 컴터에 맞게 수정!
    # driver = webdriver.Chrome("E:/ITWILL/5_Tensorflow/workspace/Final_chap/chromedriver_win32/chromedriver.exe") #
    
    # 2. 민원 검색 url 
    driver.get("https://www.epeople.go.kr/nep/pttn/gnrlPttn/pttnSmlrCaseList.npaid") # 민원을 검색할 수 있는 페이지
    
    # 이부분은 검색 조건문으로 수정하면 어떨까 의견제안!
    # 3. 검색 입력상자 tag -> 검색조건 입력
    search_Nm = driver.find_element_by_name('pttnTypeNm')       # 전체, 민원유사사례, 민원질의응답, 정책질의응답
    search_Type = driver.find_element_by_name('searchInstType') # 중앙행정기관, 지방자치단체, 교육기관, 공공기관 
    search_Cd = driver.find_element_by_name('searchInstCd')     # 세부기관(element 이름 찾기)
 
    #find_element_by_name('name') : 이름으로 element 찾기 
    #find_element_by_id('id') : 아이디로 element 찾기 

    #search_box.send_keys(name) # 검색어(name) 키보드 입력
    driver.implicitly_wait(3)  # 3초 대기(자원 loading)

    # 데이터를 가져오기 위한 함수 
    mydata = driver.find_element_by class_name('tit') # class명이tit인 모든 것을 리스트로 가져와 mydata에 할당
    
    # 여기부터는 celub crawling 코드를 복붙해온 상태! 아직 수정 전!
    # 4. [검색] 버튼 클릭 ("//tag[@attr='value']/sub element")
    driver.find_elements_by_xpath("//div[@id='sbtc']/button").click() #@id='sbtc라는 상위 element, button 하위 element입력 
 
    image_url = []
     
    i=0 # 첫번째 이미지    
    base = f"//div[@data-ri='{i}']"
    driver.find_element_by_xpath(base).click() # image click
    # click image url 
    src = driver.page_source # 현재 page html source
    html = BeautifulSoup(src, "html.parser")
    img_tag = html.select("img[class='rg_i Q4LuWd']") # list
    #print(img_tag)
    
    for tag in img_tag : 
        if 'data-src' in str(tag) :
            url = tag['data-src'] # dict
            image_url.append(url)
    
    # image url 생성   
    image_url = np.unique(image_url) # 중복 url  삭제 
    print(image_url)
    
    # url -> image save (혹시, 오류가 발생하면 SKIP하고 넘어가라~ )
    for i in range(len(image_url)) :
        try : # 예외처리 : server file 없음 예외처리 
            file_name = "test"+str(i+1)+".jpg" # test1.jsp
            # server image -> file save
            urlretrieve(image_url[i], filename=file_name)
        except :
            print('해당 url에 image 없음 : ', i+1)        
            
    driver.close()
    


# 함수 호출 : 셀럼 이미지 저장  
namelist = ["한소희","채영","김선호",'준호','채령']

for name in namelist :
    pwd = os.getcwd() # 현재 경로 
    os.mkdir(name) # 현재 위치에 폴더 생성 
    os.chdir(pwd+"/"+name) # 검색어 이용 하위폴더 생성 
    celeb_crawler(name) # image crawling
    os.chdir(pwd) # 원래 위치 이동 
    


