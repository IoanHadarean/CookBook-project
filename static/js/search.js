// Get HTML elements
let input = document.getElementById('search_input');
let footerTag = document.getElementsByTagName('footer')[0];
let results = document.getElementsByClassName('container')[0];
let recipes = document.getElementsByClassName('recipes')[0];
let searchMessage = document.getElementById('search_message');
let searchBtn = document.getElementById('btnSearch');
let btnContainer = document.getElementById('btn-container');
let recipesContainer = document.getElementsByClassName('container')[0];



loadEventListeners();


// Add Event Listeners
function loadEventListeners() {
    if (input) {
        input.addEventListener('input', loadResults);
        input.addEventListener('input', getInputResults);
    }
    if (searchBtn) {
        searchBtn.addEventListener('click', searchState);
    }
    document.addEventListener('click', styleDisabledButton);
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
function getInputResults() {
    let xhr = new XMLHttpRequest();
    document.getElementById('search_message').innerHTML = '';
    let trimmedInput = input.value.replace(/\s/g, "", true);
    if (trimmedInput.length >= 3) {
        xhr.open("POST", "/search_results/" + trimmedInput);
        xhr.onload = function() {
            if (this.readyState == 4 && this.status == 200) {
                let results = this.responseText;
                if (results === "0" && input.value != '') {
                    document.getElementById('search_message').innerHTML = 'No recipes found';
                }
                else {
                    if (results === "1" && input.value != '') {
                        document.getElementById('search_message').innerHTML = results + ' recipe was found';
                    }
                    else if (results !== "1" && input.value != '') {
                        document.getElementById('search_message').innerHTML = results + ' recipes were found';
                    }
                }
                if (input.value === '') {
                    document.getElementById('search_message').innerHTML = '';
                }
            }
        };
        xhr.onerror = function() {
            console.log('Request error...');
        };
        xhr.send();
    }
}



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
    if (btnContainer) {
        let clickInside = btnContainer.contains(event.target);
        if (clickInside) {
            searchBtn.style.borderColor = 'black';
            searchBtn.style.borderWidth = 'thin';
        }
        else {
            searchBtn.style.borderColor = 'white';
        }
    }
}
