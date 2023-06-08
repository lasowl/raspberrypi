# raspberrypi 라즈베리파이를 활용한 미니 프로젝트

## 제목: 온습도 시계

## 작품 개요
python으로 만든 시계를 통해 시간을 볼 수 있고,mqtt에 실시간 온습도 정보가 나타납니다.
물체가 일정 온도 이상이면 LED가 켜지고 일정 온도 이하로 내려가면 LED가 꺼집니다.

## 작품 제작에 사용한 센서와 엑추에이터와 역할
- LED: 온도에 따라 LED가 켜지고 꺼집니다.
- 온습도 센서:온습도를 측정하고 온습도 정보를 보여줍니다.  
## 완성 작품

### 작품회로도
![image](https://github.com/lasowl/raspberrypi/assets/116951813/6e5ba0d3-8f69-4c41-bc45-e225aa9b2ebc)

### 작품 사진
![20230608_140142](https://github.com/lasowl/raspberrypi/assets/116951813/144f2ea7-9757-4dd4-8d46-81f75f809995)

## 동작 시나리오 및 예시
현재 시간을 화면에 표시-> 온습도 센서가 온습도를 측정하여 화면에 표시-> 측정한 온습도가 26도 이상인 경우 LED가 켜지면서 "overheated"라는 문구를 출력
-> 측정한 온습도가 26도 이하라면LED가 꺼지면서 "not overheated"라는 문구를 출력
## 기대 효과
- 온도를 정해 일정온도 이상이 되면 LED 빛이 켜져 물체의 과열 여부를 알 수 있습니다. 
- 물체의 온습도 정보를 알 수 있습니다.
- 현재 시간을 알 수 있습니다.


참고자료:
- https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=dlwjddns5&logNo=220717760126
- https://www.daleseo.com/python-time/
- [11주차] 라즈베리파이와 GPIO#1
