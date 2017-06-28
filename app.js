(function(){

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

    var childRef = rootRef.child('object');
    const obj = document.getElementById("obj");

    rootRef.on("value", function(snapshot) {
        console.log(snapshot.val());
        obj.innerText = JSON.stringify(snapshot.val());
    }, function (error) {
        console.log("Error: " + error.code);
    });

}());