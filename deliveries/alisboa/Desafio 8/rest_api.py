import json


class RestAPI:
    def __init__(self, database=None):
        self.database = database

    def get(self, url, payload=None):
        if url == "/users":
            if payload is None:
                return json.dumps(self.database)
            payload = json.loads(payload)
            users_return = {"users": []}
            for user in payload["users"]:
                for users_database in self.database["users"]:
                    if users_database["name"] == user:
                        users_return["users"].append(users_database)
            return json.dumps(users_return)

    def post(self, url, payload=None):
        if url == '/add':
            new_user_dict = json.loads(payload)
            new_user_to_append = {
                'name': new_user_dict['user'],
                'owes': {},
                'owed_by': {},
                'balance': 0.0
            }
            self.database['users'].append(new_user_to_append)
            return json.dumps(new_user_to_append)

        elif url == "/iou":
            lends = json.loads(payload)
            result = {"users": []}
            for user in self.database["users"]:
                # Borrower
                if user["name"] == lends["lender"]:
                    total_value = lends["amount"]
                    if lends["borrower"] in user["owes"]:
                        user["owes"][lends["borrower"]] -= total_value
                        if user["owes"][lends["borrower"]] <= 0:
                            total_value = - user["owes"][lends["borrower"]]
                            user["owes"].pop(lends["borrower"])
                        else:
                            user["balance"] += lends["amount"]
                            result["users"].append(user)
                            continue
                    if total_value > 0:
                        if lends["lender"] in user["owed_by"]:
                            user["owed_by"][lends["borrower"]] += total_value
                        else:
                            user["owed_by"][lends["borrower"]] = total_value
                    user["balance"] += lends["amount"]
                    result["users"].append(user)

                # Lender
                elif user["name"] == lends["borrower"]:
                    total_value = lends["amount"]
                    if lends["lender"] in user["owed_by"]:
                        user["owed_by"][lends["lender"]] -= total_value
                        if user["owed_by"][lends["lender"]] <= 0:
                            total_value = - user["owed_by"][lends["lender"]]
                            user["owed_by"].pop(lends["lender"])
                        else:
                            user["balance"] -= lends["amount"]
                            result["users"].append(user)
                            continue
                    if total_value > 0:
                        if lends["borrower"] in user["owes"]:
                            user["owes"][lends["lender"]] += total_value
                        else:
                            user["owes"][lends["lender"]] = total_value
                    user["balance"] -= lends["amount"]
                    result["users"].append(user)
            return json.dumps(result)
