from __future__ import print_function
import logging
# import the module
import aerospike
from aerospike import exception


import sys

# Configure the client
store = {
    'hosts': [
        ('127.0.0.1', 3000)
    ],
}

# Create a client and connect it to the cluster
try:
    client = aerospike.client(store).connect()
except ex.ClientError as e:
    print("Error: {0} [{1}]".format(e.msg, e.code))
    sys.exit(1)


def add_customer(customer_id, phone_number, lifetime_value):
    store[customer_id] = {'phone': phone_number, 'ltv': lifetime_value}
    return store[customer_id]

def get_ltv_by_id(customer_id):
    item = store.get(customer_id, {})
    if item == {}:
        logging.error('Requested non-existent customer ' + str(customer_id))
    else:
        return item.get('ltv')


def get_ltv_by_phone(phone_number):
    for v in store.values():
        if v['phone'] == phone_number:
            return v['ltv']
    logging.error('Requested phone number is not found ' + str(phone_number))


# x = add_customer('two', '29991', 7)



# print(x)
key = 'test', 'demo', 1
get_ltv_by_id(key)
# record = {'some': 'thing'}
# try:
#   client.put(key, x)
# except AerospikeError as exc:
#   print("The in doubt nature of the operation is: {}".format(exc.args[4]))


client.close()
