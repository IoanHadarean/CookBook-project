/* global countRecipes */


// Get HTML elements
var searchButton = document.getElementById('submit_search');

searchButton.addEventListener('click', loadResults);


var countResults = countRecipes;

function loadResults(e) {
    let xhr = new XMLHttpRequest();
    var searchInputValue = document.getElementById('search_input').value;
    console.log(searchInputValue);
    xhr.onload = function() {
        if (this.readyState === 4 && this.status === 200) {
            
            console.log(countResults);
        }
        else {
            console.log("Error");
        }
    };
    xhr.open("POST", "/search_results", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send();
    e.preventDefault();
}

