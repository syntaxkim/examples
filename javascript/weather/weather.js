// This script does not work.
// Refer to https://darksky.net/dev/docs/faq#cross-origin

const API_KEY = '';
const url = `https://api.darksky.net/forecast/${API_KEY}`

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#get').onclick = get;
})

function get(){
    // Create an Ajax object
    navigator.geolocation.getCurrentPosition(success, error);
}

function success(position) {
    const lat = position.coords.latitude
    const long = position.coords.longitude

    // Create an Ajax object
    const request = new XMLHttpRequest();

    request.open('GET', `${url}/${lat},${long}`);

    request.onload = () => {
        // Extract JSON data from request
        const data = JSON.parse(request.responseText);

        if (data) {
            document.querySelector('#weather').innerHTML = data.summary;
        } else {
            document.querySelector('#weather').innerHTML = 'No data.';
        };  
    };

    // Add data to send with request
    request.send();
    return false;
};

function error() {
    
};