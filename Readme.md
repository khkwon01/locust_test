## 1. locust 설치
```
python3 -m venv locust      # virtual 환경 생성

cd locust
source bin/activate

pip install locust
```

## 2. 테스트 수행

- 테스트용 api 서버 구성
  python3 -m http.server 8090

- locust 테스트 수행

  - locust 기본 파일 생성 (locustfile.py)
  ```
  from locust import HttpUser, task, between

  class WebsiteUser(HttpUser):
    wait_time = between(0.5, 2.5)
    # 직접 IPv4 주소를 명시하여 해당 IP로 요청을 보냅니다.
    # DNS에 의존하지 않고 특정 IP로만 통신하고 싶을 때 유용합니다.
    host = "http://0.0.0.0:8090" # ✨ 여기에 테스트 대상 서버의 IPv4 주소를 입력하세요.

    @task
    def view_homepage(self):
        self.client.get("/")
        print("Accessed homepage via IPv4")
  ```
  - locust 시작
    locust -f locustfile.py --web-host 0.0.0.0 --web-port 8080

- load 테스트 수행

  위에 locust를 시작하면 GUI가 시작되고 해당 웹인터페이스 접속후 아래 셋팅을 통해 부하 테스트 수행
  
  <img width="1245" height="794" alt="image" src="https://github.com/user-attachments/assets/9d6f1615-7bb3-46c9-97bc-253c4c2df4dc" />

- load 테스트 결과 확인

  부하 테스트 후 아래와 같이 결과를 확인
  
  <img width="1229" height="688" alt="image" src="https://github.com/user-attachments/assets/e53579b1-af7d-4076-88f5-e92d7cb3b36d" />


