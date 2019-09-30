import requests
from requests.exceptions import ConnectionError
# import pdb
from django.conf import settings

CUSTOMER_API_URL = settings.REMOTE_CUSTOMER_API_HOST


REMOTE_URL = CUSTOMER_API_URL + '/server/customers/'

class RemoteCustomerApi:
    @staticmethod
    def create(customer):
        data = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'remote_id': customer.id
        }
        try:
            res = requests.post(url=REMOTE_URL, data=data)
            remote_id = res.json()['id']
            customer.remote_id = remote_id
            customer.save()
        except ConnectionError:
            pass

    @staticmethod
    def update(customer):
        id = customer.remote_id
        data = {
            'first_name': customer.first_name,
            'last_name': customer.last_name,
        }
        # pdb.set_trace()
        requests.put(url=REMOTE_URL + '%d/' % id, data=data)
        # try:
        #     requests.put(url=REMOTE_URL + '%d/' % id, data=data)
        # except ConnectionError:
        #     pass
