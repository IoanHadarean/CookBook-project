/* global fetch */


// Get HTML elements
let input = document.getElementById('search_input');
let footerTag = document.getElementsByTagName('footer')[0];
let results = document.getElementsByClassName('container')[0];
let recipes = document.getElementsByClassName('recipes')[0];
let searchMessage = document.getElementById('search_message');
let searchBtn = document.getElementById('btnSearch');
let btnContainer = document.getElementById('btn-container');
let searchForm = document.getElementById('search_form');
var searchText;


// Load the search results
if (input) {
    input.addEventListener('input', function loadResults() {
        if (searchMessage) {
            searchMessage.innerHTML = '';
        }
        if (input.value.length >= 3) {
            searchBtn.disabled = false;
        }
        else {
            searchBtn.disabled = true;
        }
        document.getElementsByClassName('container')[0].innerHTML = '';
        footerTag.style.position = 'absolute';
    });
}

// Get search text from input
var getSearchText = searchText;
console.log(typeof (getSearchText));



if (searchBtn) {
    searchBtn.addEventListener('click', getResults);
}


// Get search results on click
function getResults() {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/search_results", true);
    xhr.onload = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = this.responseText;
            console.log(response);
            document.getElementById('search_message').innerHTML = response;
        }
        else {
            console.log("Response not received");
        }
    };
    xhr.onerror = function() {
        console.log('Request error...');
    };
    xhr.send();
}


if(input) {
    input.addEventListener('input', getInputResults);
}

// Get search results on input
function getInputResults() {
    let xhr = new XMLHttpRequest();
    console.log(input.value);
    xhr.open("POST", "/search_results/" + input.value, true);
    xhr.onload = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = this.responseText;
            console.log(response);
            document.getElementById('search_message').innerHTML = response;
        }
        else {
            console.log("Response not received");
        }
    };
    xhr.onerror = function() {
        console.log('Request error...');
    };
    xhr.send();
}


if (searchBtn) {
    searchBtn.addEventListener('click', searchState);
}

function searchState() {
    if (input.value.length >= 3) {
        searchBtn.disabled = false;
        document.getElementById('search_form').submit();
    }
    else {
        searchBtn.disabled = true;
    }
}





if (results) {
    if (results.contains(recipes)) {
        footerTag.style.position = 'relative';
    }
}

document.addEventListener('click', function(e) {
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
});
