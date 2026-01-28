# locustfile.py  (или любое имя, но тогда -f обязательно)

from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)           # пауза между задачами 1–5 сек

    @task(3)                            # вес задачи — будет выполняться в 3 раза чаще
    def check_home(self):
        self.client.get("/")            # главная страница

    @task(1)
    def check_some_endpoint(self):
        self.client.get("/some/path")   # если у тебя есть конкретные эндпоинты