document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#form').onsubmit = () => {

        const base = document.querySelector('#base').value;
        const other = document.querySelector('#other').value;

        const request = new XMLHttpRequest();

        request.open('POST', '/');

        request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        request.responseType = 'json';
        
        request.onload = () => {
            const data = request.response;
            if (data.success) {
                const contents = `1 ${data.base} is equal to ${data.rates} ${data.other}.`;
                document.querySelector('#result').innerHTML = contents;
            }
            else {
                document.querySelector('#result').innerHTML = "There was an error.";
            }
        }
        
        data = JSON.stringify({"base": base, "other": other})
        request.send(data);
        
        return false;

    };
})

/* This AJAX example both sends and gets JSON data */