#pip install pymongo#

import pymongo

from pymongo import MongoClient
url ="mongodb+srv://shyed2001:shyed2001@edrpymongdb1.ujuxe.mongodb.net/PyMongoDB1?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client['emp_details']
collection = db['customer_information']
collection.insert_many([{"id":204, "name":"SHYED24"},{"id":205, "name":"SHAH25"},{"id":206, "name":"SHYED246"},{"id":207, "name":"SHAH257"}, {"id":208, "name":"SHYED248"},{"id":209, "name":"SHAH2589"}])
import pprint
pprint.pprint(collection.find_one())

for i in collection.find():
    pprint.pprint(i)


    