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
    input.addEventListener('input', function loadResults(e) {
        let xhr = new XMLHttpRequest();
        // var inputValue = document.getElementById('search_input').value;
        document.getElementById('search_message').innerHTML = '';
        document.getElementsByClassName('container')[0].innerHTML = '';
        footerTag.style.position = 'absolute';
        document.getElementsByClassName('container')[0].innerHTML = '';
        xhr.onload = function() {
            if (this.readyState === 4 && this.status === 200) {
                let response = xhr.responseText;
                console.log(response);
                document.getElementById('search_message').innerHTML = '';
                document.getElementsByClassName('container')[0].innerHTML = '';
                if (response == 0) {
                    
                }
            }
            else {
                console.log("Response not received");
                document.getElementById('search_message').innerHTML = '';
                document.getElementsByClassName('container')[0].innerHTML = '';
            }
        };
        xhr.open("POST", "/search_results", true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send();
        e.preventDefault();
    });
}

if (results) {
    if (results.contains(recipes)) {
        footerTag.style.position = 'relative';
    }
}

