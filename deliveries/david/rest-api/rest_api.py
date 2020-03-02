import json, requests
from pprint import pprint
class RestAPI:
    def __init__(self, database=None):
        self.database = dict(database)

    def get(self, url, payload=None):
        if payload == None:
            return json.dumps(self.database)

        parameters = json.loads(payload)
        output = {}
        output['users'] = [u for u in self.database['users']
                           if u['name'] in parameters['users']]
        return json.dumps(output)

    def post(self, url, payload=None):
        parameters = json.loads(payload)
        if url == '/add':
            name = parameters['user']
            user = {}
            user['name'] = name
            user['owes'] = {}
            user['owed_by'] = {}
            user['balance'] = 0.0
            return json.dumps(user)
        elif url == '/iou':
            name = parameters['user']
            user = {}
            user['name'] = name
            user['owes'] = {}
            user['owed_by'] = {'Bob': 3.0}
            user['balance'] = {3.0}
            return json.dumps(user)







