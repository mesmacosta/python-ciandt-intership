import json

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

            lender = parameters['lender']
            lender_dict = [u for u in self.database['users']
                           if u['name'] == lender][0]
            borrower = parameters['borrower']
            borrower_dict = [u for u in self.database['users']
                             if u['name'] == borrower][0]
            amount = parameters['amount']

            if borrower in lender:
                due = lender_dict['owes'][borrower]
                if amount < due:
                    lender_dict['owes'][borrower] -= amount
                    lender_dict['balance'] += amount
                    borrower_dict['owed_by'][lender] -= amount
                    borrower_dict['balance'] -= amount
                    amount = 0
                else:
                    del lender_dict['owes'][borrower]
                    lender_dict['balance'] += due
                    del borrower_dict['owed_by'][lender]
                    borrower_dict['balance'] -= due
                    amount = amount - due
