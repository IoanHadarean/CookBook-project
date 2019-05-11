// Get HTML elements
let input = document.getElementById('search_input');
let footerTag = document.getElementsByTagName('footer')[0];
let results = document.getElementsByClassName('container')[0];
let recipes = document.getElementsByClassName('recipes')[0];
let searchMessage = document.getElementById('search_message');
let searchBtn = document.getElementById('btnSearch');
let btnSearchContainer = document.getElementById('search-btn-container');
let recipesContainer = document.getElementsByClassName('container')[0];
let countResults = document.getElementById('count_results');


// Load all event listeners
loadEventListeners();


// Add Event Listeners
function loadEventListeners() {
    if (input) {
        input.addEventListener('input', loadResults);
        input.addEventListener('keyup', removeCountResults);
        input.addEventListener('input', getInputResults);
    }
    if (searchBtn) {
        searchBtn.addEventListener('click', searchState);
    }
    document.addEventListener('click', styleDisabledButton);
}


// Remove count results when deleting input value
function removeCountResults() {
    if (countResults) {
       countResults.innerHTML = '';
    }
}



// Load the search results
function loadResults() {
    if (searchMessage) {
        searchMessage.innerHTML = '';
    }
    let trimmedInput = input.value.replace(/\s/g, "", true);
    if (trimmedInput.length >= 3) {
        searchBtn.disabled = false;
    }
    else if (trimmedInput.length < 3) {
        searchBtn.disabled = true;
    }
    recipesContainer.innerHTML = '';
    footerTag.style.position = 'absolute';
}



// Get number of search results on input
var getInputResults = function() {
    let xhr = new XMLHttpRequest();
    var searchRequest = null;
    let searchText = input.value;
    if (searchText.length >= 3) {
        searchRequest = xhr.open("POST", "/search_results/" + searchText, true);
        // Abort old pending requests
        if (searchRequest) {
            searchRequest.abort();
        }
        xhr.onload = function() {
            if (this.readyState == 4 && this.status == 200) {
                let results = xhr.responseText;
                if (results == "0") {
                    if (countResults) {
                        countResults.innerHTML = '';
                    }
                    document.getElementById('search_message').innerHTML = 'No recipes found';
                }
                else {
                    if (results == "1") {
                        if (countResults) {
                            countResults.innerHTML = '';
                        }
                        document.getElementById('search_message').innerHTML = results + ' recipe was found';
                    }
                    else if (results != "1") {
                        if (countResults) {
                           countResults.innerHTML = '';
                        }
                        document.getElementById('search_message').innerHTML = results + ' recipes were found';
                    }
                }
                if (input.value == '') {
                    if (countResults) {
                        countResults.innerHTML = '';
                    }
                    document.getElementById('search_message').innerHTML = '';
                }
            }
        };
        xhr.onerror = function() {
            console.log('Request error...');
        };
        xhr.send();
    }
};



// Set the state of the search button
function searchState() {
    if (input.value.length >= 3) {
        searchBtn.disabled = false;
    }
    else {
        searchBtn.disabled = true;
    }
}



// Set the footer position to relative when there are results
if (results) {
    if (results.contains(recipes)) {
        footerTag.style.position = 'relative';
    }
}

// Style the search button when it's disabled
function styleDisabledButton() {
    if (btnSearchContainer) {
        let clickInside = btnSearchContainer.contains(event.target);
        if (clickInside) {
            searchBtn.style.borderColor = 'black';
            searchBtn.style.borderWidth = 'thin';
        }
        else {
            searchBtn.style.borderColor = 'white';
        }
    }
}



// Performed debouncing to avoid unnecessary requests on input change
var debounceTimeout = null;

input.addEventListener('input', function(event) {
    clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout(getInputResults, 500);
});
