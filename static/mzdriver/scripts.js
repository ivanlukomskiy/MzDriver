const URL = '/api/servo/y/velocity';

const setVelocity = function (value) {
    fetch(URL, {
        method: 'PUT',
        body: JSON.stringify({
            value: value
        })
    }).then(resp => resp.json())
        .then(resp => {
            document.getElementById("currentVY").innerHTML = resp.value;
        });
};