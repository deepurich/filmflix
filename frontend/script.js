var xhr = null;

getXmlHttpRequestObject = function () {
    if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
    }
    return xhr;
};

function dataCallback() {
    // Check response is ready or not
    if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("User data received!");
        getDate();
        dataDiv = document.getElementById('result-container');
        // Set current data text
        dataDiv.innerHTML = render(xhr.responseText);
    }
}

function render(films) {
    myObj = JSON.parse(films);
    text = "<table border='1'>";
    text += "<tr><th>Film ID</th><th>Title</th><th>Genre</th><th>Year Released</th><th>Duration</th><th>Rating</th></tr>"
    for (x in myObj) {
        text += "<tr>"
            + "<td>" + myObj[x].filmID + "</td>"
            + "<td>" + myObj[x].title + "</td>"
            + "<td>" + myObj[x].genre + "</td>"
            + "<td>" + myObj[x].yearReleased + "</td>"
            + "<td>" + myObj[x].duration + "</td>"
            + "<td>" + myObj[x].rating + "</td>"
            + "</tr>"
    }
    text += "</table>";
    return text;
}

function getUsers() {
    console.log("Get users...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    xhr.open("GET", "https://filmflixapi.ratnabollapalli.repl.co/users", true);
    // Send the request over the network
    xhr.send(null);
}
function getFilms() {
    console.log("Get films...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    xhr.open("GET", "https://filmflixapi.ratnabollapalli.repl.co/films", true);
    // Send the request over the network
    xhr.send(null);
}

function getDate() {
    date = new Date().toString();

    document.getElementById('time-container').textContent
        = date;
}

function postFilms() {
    filmID = document.getElementById('filmID').value;
    title = document.getElementById('title').value;
    yearReleased = document.getElementById('yearReleased').value;
    rating = document.getElementById('rating').value;
    duration = document.getElementById('duration').value;
    genre = document.getElementById('genre').value;
    dataToSend = {
        "duration": duration,
        "filmID": filmID,
        "genre": genre,
        "rating": rating,
        "title": title,
        "yearReleased": yearReleased
    }
    console.log("post films...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    xhr.open("POST", "https://filmflixapi.ratnabollapalli.repl.co/films", true);
    // Send the request over the network
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(dataToSend));

}
function putFilms() {
    filmID = document.getElementById('filmID').value;
    title = document.getElementById('title').value;
    yearReleased = document.getElementById('yearReleased').value;
    rating = document.getElementById('rating').value;
    duration = document.getElementById('duration').value;
    genre = document.getElementById('genre').value;
    dataToSend = {
        "duration": duration,
        "filmID": filmID,
        "genre": genre,
        "rating": rating,
        "title": title,
        "yearReleased": yearReleased
    }
    console.log("post films...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    xhr.open("PUT", "https://filmflixapi.ratnabollapalli.repl.co/films", true);
    // Send the request over the network
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(dataToSend));

}
function deleteFilms() {
    filmID = document.getElementById('filmID').value;
    dataToSend = {
        "filmID": filmID
    }
    console.log("delete films...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    xhr.open("DELETE", "https://filmflixapi.ratnabollapalli.repl.co/films", true);
    // Send the request over the network
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(dataToSend));
}
function Addfilms() {
    document.getElementById("loginAddfilms").style.display = "block";
}
function closeFilms() {
    document.getElementById("loginAddfilms").style.display = "none";
}
window.onclick = function (event) {
    let modal = document.getElementById('loginAddfilms');
    if (event.target == modal) {
        closeForm();
    }
}