from locust import task, HttpUser
import random


class Object(HttpUser):


    @task(1)
    def get_all_objects(self):
        self.client.get("/object")


    @task(3)
    def get_one_object(self):
        self.client.get(f"object/{random.choice([1, 578, 579, 580, 581, 583, 584, 585, 586, 587, 588, 589, 590, 591])}")
