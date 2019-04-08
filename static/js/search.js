// Get HTML elements
let searchButton = document.getElementById('submit_search');
console.log(searchButton);

searchButton.addEventListener('click', loadResults);


function loadResults() {
    var xhr = new XMLHttpRequest();
    xhr.onload = function() {
        if (this.readyState === 4 && this.status === 200) {
            let response = xhr.responseText;
            console.log(response);
        }
    };
    xhr.open("POST", "/search_results", true);
    xhr.send();
}