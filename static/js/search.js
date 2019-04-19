// Get HTML elements
let input = document.getElementById('search_input');
let footerTag = document.getElementsByTagName('footer')[0];
let results = document.getElementsByClassName('container')[0];
let recipes = document.getElementsByClassName('recipes')[0];
let searchMessage = document.getElementById('search_message');
let searchBtn = document.getElementById('submit_search');
let btnContainer = document.getElementById('btn-container');


// Load the search results
if (input) {
    input.addEventListener('input', function loadResults(e) {
        if (searchMessage) {
            searchMessage.innerHTML = '';
        }
        if (input.value.length >= 3) {
            searchBtn.disabled = false;
        }
        else {
            searchBtn.disabled =  true;
        }
        document.getElementsByClassName('container')[0].innerHTML = '';
        footerTag.style.position = 'absolute';
    });
}

if (results) {
    if (results.contains(recipes)) {
        footerTag.style.position = 'relative';
    }
}

document.addEventListener('click', function(e) {
     let clickInside = btnContainer.contains(event.target);
     if (clickInside) {
        searchBtn.style.borderColor = 'black';
        searchBtn.style.borderWidth = 'thin';
     }
     else {
         searchBtn.style.borderColor = 'white';
     }
});
