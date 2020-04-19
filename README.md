# PuppyBuddy

<기획안>

강아지 산책 친구찾기 PuppyBuddy

1. 프로젝트 이름/설명

-이름 : PuppyBuddy (강아지 산책 친구를 찾아요)

-설명 : 산책하려는 강아지의 기본정보, 산책장소와 시간을 등록하면 그걸 보고 원하는 친구가 찾아갈 수 있어요. 산책장소의 위치와 사진, 후기평을 보고 작성하면서 서로 정보를 교환할 수 있어요.


 

2. 기획의도

- 강아지를 키우는 견주입장에서 시간과 장소만 맞으면 새로운 강아지친구를 만나서 같이 산책시키면 좋겠다는 취지에서 기획하게 되었습니다. 쾌적한 산책을 위해 우선 오늘의 날씨와 미세먼지 정보를 알아봅니다. 그리고 애견동반 장소(공원,카페,음식점 등)에 대한 정보(사진,위치,가격,후기 등)를 직접 작성해서 교류하면 강아지를 동네에서 어디로 산책시키러 가야할지 결정하는데 도움이 될 거라 생각했습니다.

3. 구상도
(사진)


4. 개발해야하는 기능

- Front-end : 메인에서 버튼클릭시 날씨or장소 정보페이지로 이동, 날씨페이지(오늘의 날씨 반영해서 CSS로 보여주기), 강아지 산책정보 등록버튼(openclose), 장소 후기comment남기는 input // UI기능(커서 올렸을 때 사진뜨게)

- Back-end : 날씨페이지(기후API- 지역구별로 미세먼지 정보 가져오기, 오늘 기후 정보 가져오기), DB에 리스트 작성, 새로운 강아지정보 저장, 장소에 대한 후기 작성(like), 지도&검색API

5. 개발 계획 - FLOWCHART 만들어서 순서대로 진행해보기

# 5,6 주차 

carousel jquery : owl / slick /

** slick시에 사라지는 텍스트 해결

slide1: main , slide2: 날씨 (기후, 미세먼지api) , slide3: 강아지등록&맵api

<<slide 2 : 날씨>>


서울시 실시간 미세먼지(구별로 나옴)

http://openapi.seoul.go.kr:8088/(인증키)/json/RealtimeCityAir/1/99

서울시 실시간 대기환경 평균 현황

http://openapi.seoul.go.kr:8088/(인증키)/xml/ListAvgOfSeoulAirQualityService/1/5

<openweathermap api

api : http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=(인증키)a&lang=kr

weather icon  

01d : clear sky   main(Clear) ID(800)     ==== clear

02d : few clouds  scattered clouds  main(Clouds) ID(801-804)   ====mostlysunny

03d 04d : broken clouds    ===== cloudy

09d 10d shower rain  rain   main(Drizzle) ID(300-321)  main(Rain) ID(500-531) === rain

11d : thunderstorm    main(Thunderstorm) ID(200-232)   ==== tstorms

13d snow   main(Snow) ID(600-622)     ====snow

50d mist  main(Mist, Smoke, Haze, Dust, Fog, Sand, Dust, Ash, Squall, Tornado) ID(701-781) === fog


((Q. 해결해야할 점 : api ajax에서 json타입말로 xml타입인 경우 어떻게?
                    slick 적용시 텍스트 사라지는 문제
                    날씨페이지에서 미세먼지 불러올때 기존 정보는 지우는 방법 + 아래 날씨그림이 내려가지않게 하는 방법))


# 7주차

<<slide 3 : 강아지정보등록 & 장소리뷰>>
slide 3 레이아웃 정하기 (정보등록 input box)

강아지 친구정보 : db 저장하기

지도, 리뷰 API

