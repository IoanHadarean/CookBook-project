/* global countRecipes */


// Get HTML elements
var searchButton = document.getElementById('submit_search');
var form = document.getElementById('search_form');
var input = document.getElementById('search_input');
console.log(input);


// Load the search results
input.addEventListener('input', function loadResults() {
    let xhr = new XMLHttpRequest();
    let inputValue = document.getElementById('search_input').value;
    console.log(inputValue);
    document.getElementById('search_message').innerHTML = '';
    inputValue = '';
    xhr.onload = function() {
        inputValue = '';
        if (this.readyState === 4 && this.status === 200) {
            let response = JSON.parse(xhr.responseText);
            console.log(response);
            var countResults = response;
            document.getElementById('search_message').innerHTML = '';
            console.log(countResults);
            if (countResults == 0) {
                document.getElementById('search_message').innerHTML = 'No recipes were found';
                inputValue = '';
            }
            else {
                document.getElementById('search_message').innerHTML = countResults + " matches were found";
                inputValue = '';
            }
        }
        else {
            console.log("Response not received");
            document.getElementById('search_message').innerHTML = '';
        }
    };
    xhr.open("POST", "/search_results", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send();
});



