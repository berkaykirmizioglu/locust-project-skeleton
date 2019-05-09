from locust import HttpLocust, TaskSet, task, events
import sys
import os
from pathlib import Path
import random
sys.path.append(str(Path(os.getcwd()).parent))
from lib.utils.csv_utils import read_from_csv


class UserBehavior(TaskSet):
    @task
    def search(self):
        try:
            city = str(random.choice(read_from_csv("resource/cities.csv")))
        except IndexError as index_error:
            print("No data found in .csv file. See: ".format(index_error))

        r = self.client.get("/find?q={}".format(city),
                            name="Searching {} weather".format(city))

        assert r.status_code is 200, "Unexpected response code:" + str(r.status_code)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = "https://openweathermap.org"
    min_wait = 100
    max_wait = 500


def track_success(**kwargs):
    print(kwargs)


events.request_success += track_success