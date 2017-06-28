(function(){

    let config = {
        apiKey: "AIzaSyDHnvGOavbHG9Z2sJIqIECX7ZGqGez3hYw",
        authDomain: "rpdies-sample-app.firebaseapp.com",
        databaseURL: "https://rpdies-sample-app.firebaseio.com",
        projectId: "rpdies-sample-app",
        storageBucket: "rpdies-sample-app.appspot.com",
        messagingSenderId: "569042443468"
    };

    let defaultApp = firebase.initializeApp(config);
    let rootRef = firebase.database().ref();

    let childRef = rootRef.child('object');
    const obj = document.getElementById("obj");

    rootRef.on("value", data => {
        console.log(data.val());
        obj.innerText = JSON.stringify(data.val());
    }, error => {
        console.log("Error: " + error.code);
    });

}());