import pyrebase

config = {
    "apiKey": "AIzaSyDHnvGOavbHG9Z2sJIqIECX7ZGqGez3hYw",
    "authDomain": "rpdies-sample-app.firebaseapp.com",
    "databaseURL": "https://rpdies-sample-app.firebaseio.com",
    "projectId": "rpdies-sample-app",
    "storageBucket": "rpdies-sample-app.appspot.com",
    "messagingSenderId": "569042443468"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()