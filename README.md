# FirebaseApp
IoT Open Innovation Lab - FireBase App

# Problem 1 - (Work In Progress)
Create a simple login page using Node.js, ExpressJS and a template engine of your choice.
The login page should integrate with a sample firebase application given below, and authenticate the user using email and password in the backend, i.e the sign-in process should get completed on the server side (in NodeJS) and not on the client side (using Javascript).

The email-password pair that you can use to test your login are:

1. sample@gmail.com — 123456789 
2. sample2@gmail.com — qwertyuiop

# Problem 2 - (Work In Progress)
Create a simple HTML web page using NodeJS, ExpressJS and a template engine of your choice.
The web page should display information stored in the database of the sample firebase application given below. The web page should also have a button that exports the displayed information to a pdf file.

# Problem 3 - (Completed)
Create a python script that extracts the information from the database stored in the sample firebase application given below, and return the following in any format:
  1. The total number of users that have “1” in the count array
  2. The name of the users (user1,user2,user3, etc.) who have the “string”:”hello world”, as a key:value pair 3. The total   number of users that have the “boolean” value as false
     
```javascript
  var config = {
     apiKey: "AIzaSyDHnvGOavbHG9Z2sJIqIECX7ZGqGez3hYw",
     authDomain: "rpdies-sample-app.firebaseapp.com",
     databaseURL: "https://rpdies-sample-app.firebaseio.com",
     projectId: "rpdies-sample-app",
     storageBucket: "rpdies-sample-app.appspot.com",
     messagingSenderId: "569042443468"
   };
  var defaultApp = firebase.initializeApp(config);
  var rootRef = firebase.database().ref();
 ```

This the sample of the database stored in the Firebase app you’ve been assigned.
 
```javascript
{
 "user1" :{
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
     } 
  },
  "user3" : {
    "boolean" : true,
    "count" : [ 4 ],
    "object" : {
        "a" : "b",
        "c" : "d",
        "e" : "f"
     }
  }
}
```
 
