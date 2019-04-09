/* global countRecipes */


// Get HTML elements
var searchButton = document.getElementById('submit_search');
var form = document.getElementById('search_form');
var input = document.getElementById('search_input');


// Load the search results
input.addEventListener('keyup', function loadResults(e) {
    let inputValue = document.getElementById('search_input').value;
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/search_results", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(inputValue);
    xhr.onload =  displayData;
    function displayData() {
        if (this.readyState === 4 && this.status === 200) {
            let response = xhr.responseText;
            console.log(response);
            if (response == 0) {
                document.getElementById('search_input').innerHTML = 'No recipes were found';
            }
            else {
                document.getElementById('search_input').innerHTML = response + " matches were found";
            }
        }
        else {
            alert("Response not received");
        }
    }
    e.preventDefault();
});
