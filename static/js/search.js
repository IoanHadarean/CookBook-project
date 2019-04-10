/* global countRecipes */


// Get HTML elements
var searchButton = document.getElementById('submit_search');
var form = document.getElementById('search_form');
var input = document.getElementById('search_input');


// Load the search results
input.addEventListener('input', function loadResults(e) {
    let inputValue = document.getElementById('search_input').value;
    console.log(inputValue);
    let xhr = new XMLHttpRequest();
    xhr.onload = function() {
        if (this.readyState === 4 && this.status === 200) {
            let response = JSON.parse(xhr.responseText);
            var countResults = response;
            console.log(countResults);
            if (countResults == "0") {
                document.getElementById('search_message').innerHTML = 'No recipes were found';
            }
            else {
                document.getElementById('search_message').innerHTML = countResults + " matches were found";
            }
        }
        else {
            console.log("Response not received");
        }
    };
    xhr.open("POST", "/search_results", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send();
    e.preventDefault();
});
