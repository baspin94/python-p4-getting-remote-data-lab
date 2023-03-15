import requests
import json

url =  'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        people = json.loads(self.get_response_body())
        people_list = [person for person in people]
        return people_list

# import ipdb; ipdb.set_trace()