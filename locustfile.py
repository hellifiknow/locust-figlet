import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def index_page(self):
        self.client.post(
            "/function/figlet", "Software is a child that never goes to sleep. Always needing something.", name="/software")
        self.client.post(
            "/function/figlet", "Young women going through the hippie stage of putting their mattress on the floor.", name="/women")
