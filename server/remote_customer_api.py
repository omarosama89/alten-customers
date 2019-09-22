import requests

REMOTE_URL = 'http://localhost:8000/server/customers/'


class RemoteCustomerApi:
    @staticmethod
    def create(customer):
        data = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'remote_id': customer.id
        }
        res = requests.post(url=REMOTE_URL, data=data)
        remote_id = res.json()['id']
        customer.remote_id = remote_id
        customer.save()

    @staticmethod
    def update(customer):
        id = customer.remote_id
        data = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
        }
        requests.put(url=REMOTE_URL + '%d/' % id, data=data)

