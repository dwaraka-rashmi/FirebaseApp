# FirebaseApp
IoT Open Innovation Lab - FireBase App

Create a python script that extracts the information from the database stored in the sample firebase application given below, and return the following in any format:
  1. The total number of users that have “1” in the count array
  2. The name of the users (user1,user2,user3, etc.) who have the “string”:”hello world”, as a key:value pair 3. The total   number of users that have the “boolean” value as false
     
     ```var config = {
    apiKey: "AIzaSyDHnvGOavbHG9Z2sJIqIECX7ZGqGez3hYw",
    authDomain: "rpdies-sample-app.firebaseapp.com",
    databaseURL: "https://rpdies-sample-app.firebaseio.com",
    projectId: "rpdies-sample-app",
    storageBucket: "rpdies-sample-app.appspot.com",
    messagingSenderId: "569042443468"
  };
var defaultApp = firebase.initializeApp(config);
var rootRef = firebase.database().ref();```

This the sample of the database stored in the Firebase app you’ve been assigned.
``` {
"user1" :
   {
    "boolean" : true,
        "count" : [ 1, 2, 3 ],
        "object" : {
          "a" : "b",
          "c" : "d",
          "e" : "f"
},
    "string" : "Hello World"
  },
  "user2" : {
    "boolean" : false,
    "count" : [ 1, 3 ],
    "object" : {
      "a" : "b",
      "c" : "d",
      "e" : "f"
} },
  "user3" : {
    "boolean" : true,
    "count" : [ 4 ],
    "object" : {
"a" : "b",
"c" : "d",
"e" : "f"
}
}
}```
 
