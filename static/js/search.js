// Get HTML elements
var searchButton = document.getElementById('submit_search');
var form = document.getElementById('search_form');
var input = document.getElementById('search_input');
var footerTag = document.getElementsByTagName('footer')[0];
var results = document.getElementsByClassName('container')[0];
var recipes = document.getElementsByClassName('recipes')[0];
var inputValue = document.getElementById('search_input').value;
var countSpan = document.getElementById('search_message');

// searchButton.addEventListener('click', resetInput);
// input.addEventListener('input', resetInput);

// function resetInput() {
//     let inputValue = document.getElementById('search_input').value;
//     inputValue = '';
//     results = '';
// }



// Load the search results
if (input) {
    input.addEventListener('input', function loadResults() {
        let xhr = new XMLHttpRequest();
        // var inputValue = document.getElementById('search_input').value;
        document.getElementById('search_message').innerHTML = '';
        document.getElementsByClassName('container')[0].innerHTML = '';
        footerTag.style.position = 'absolute';
        inputValue = '';
        document.getElementsByClassName('container')[0].innerHTML = '';
        xhr.onload = function() {
            inputValue = '';
            if (this.readyState === 4 && this.status === 200) {
                let response = xhr.responseText;
                document.getElementById('search_message').innerHTML = '';
                inputValue = '';
                document.getElementsByClassName('container')[0].innerHTML = '';
            }
            else {
                console.log("Response not received");
                document.getElementById('search_message').innerHTML = '';
                inputValue = '';
                document.getElementsByClassName('container')[0].innerHTML = '';
            }
        };
        xhr.open("POST", "/search_results", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send();
    });
}

if (results) {
    if (results.contains(recipes) || input.value != '') {
        footerTag.style.position = 'relative';
    }
}
