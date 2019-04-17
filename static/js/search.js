// Get HTML elements
let input = document.getElementById('search_input');
let footerTag = document.getElementsByTagName('footer')[0];
let results = document.getElementsByClassName('container')[0];
let recipes = document.getElementsByClassName('recipes')[0];
let searchMessage = document.getElementById('search_message');


// Load the search results
if (input) {
    input.addEventListener('input', function loadResults(e) {
        if (searchMessage) {
            searchMessage.innerHTML = '';
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
