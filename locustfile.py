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
