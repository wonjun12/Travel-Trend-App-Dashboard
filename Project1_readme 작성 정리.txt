https://github.com/HJ-Rich/java-baseball-precourse/tree/as#%EC%A0%95%EB%8B%B5-%EC%9D%B4%ED%9B%84-%EC%B2%98%EB%A6%AC
https://www.freecodecamp.org/korean/news/gisheobeu-peurojegteue-rideumi-paileul-jal-jagseonghaneun-bangbeob/
https://shields.io/

 - 기능 들
  - github CI/CD action를 통해 자동 배포 설정
   - about
     - 간략하게 어떤 앱인지에 대해 설명을 해줍니다.
     - 사용한 데이터의 출처를 보여줍니다.
     - 사용한 데이터가 무엇인지 보여줍니다.
   - 해외 여행
     - 지정한 날짜를 기준으로 검색된 해외 여행 순위를 알려줍니다.
     - 모바일, PC 검색량을 보여주며, 전체 검색량도 같이 보여줍니다.
     - 여행지에 따라서 검색어 종류와 비율에 대해 확인 할수 있습니다.
   - 국내 여행
     - 지정한 날짜를 기준으로 검색된 국내 여행 순위를 알려줍니다.
     - 모바일, PC 검색량을 보여주며, 전체 검색량도 같이 보여줍니다.
     - 여행지에 따라서 검색어 종류와 비율에 대해 확인 할수 있습니다.
   - ml
     - Prophet 라이브러리를 이용해 미래 예측 학습을 진행.
     - 원하는 날짜 범위의 해외, 국내 여행의 검색량을 예측하고, 순위를 나타냅니다.
   - Data Upload
     - 최신 데이터가 추가 되거나, 과거 없는 데이터가 존재할 시 쉽게 정보 추가가 가능합니다.

Please commit your changes or stash them before you merge.
 : https://goddaehee.tistory.com/253

https://sundries-in-myidea.tistory.com/102
    
프로젝트 문제들의 해결
1. 저장된 csv파일을 불러오니 날짜데이터가 String으로 되있더라
1. 예측 모델 Prophet를 사용한 이유 (다른것들은 안되더라)
1. 다운 받은 파일들이 일별로 나와있다보니 합쳐야 했다.(os.path.join, glob.glob, pd.concat)
2. 모델 학습할때 순위로 학습을 할려했지만, 같은 여행 장소가 중복되어 여러번 나오다보니 제대로 학습이 되지않았다.
3. joblib를 통해 모델을 파일화 할때, 여러가지 넣어서 파일화 시킴
4. 기본 라이브러리 plot, seaborn의 방식보다 plotly를 사용하고 싶었다.
5. 데이터 추가를 할때 알아서 전처리 후 csv파일에 넣는데, 파일 업로드 전에 올린 파일도 중복 체크를 한다.
6. 원래는 해외, 국내 여행에 있어서 다르게 csv파일을 저장했으나 같은 코드를 이용해 출력되다보니 csv파일을 합쳤고, 코드들도 하나의 함수로 만들어 출력했다.
