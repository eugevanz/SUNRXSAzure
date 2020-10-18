# import pyrebase
# import json

# fireconfig = {
#     "apiKey": "AIzaSyCPexi8M8FFjmqjtoBTp3HJJiHwyk03S5M",
#     "authDomain": "report-manager-e3067.firebaseapp.com",
#     "databaseURL": "https://report-manager-e3067.firebaseio.com",
#     "projectId": "report-manager-e3067",
#     "storageBucket": "report-manager-e3067.appspot.com",
#     "messagingSenderId": "957180191625"
# }

# firebase = pyrebase.initialize_app(fireconfig)

# # auth = firebase.auth()

# db = firebase.database()
# response = db.child("incidents").get()
# parseDict = dict(response.val())

# app_json = json.dumps(parseDict)
# print(app_json)
