/* global countRecipes */


// Get HTML elements
var searchButton = document.getElementById('submit_search');

// Add click event listener for search button
searchButton.addEventListener('click', loadResults);

// Get countRecipes variable from Jinja template in recipes.html
var countResults = countRecipes;


// Load the search results
function loadResults(e) {
    let xhr = new XMLHttpRequest();
    xhr.onload = function() {
        if (this.readyState === 4 && this.status === 200) {
            let response = xhr.responseText;
            document.getElementById('search_input').value = '';
            if (countResults == 0) {
                document.getElementById('search_input').placeholder = 'No recipes were found';
            }
            else {
                document.getElementById('search_input').placeholder = countResults + " matches were found";
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
}

