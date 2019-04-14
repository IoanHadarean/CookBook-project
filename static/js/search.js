// Get HTML elements
let input = document.getElementById('search_input');
let footerTag = document.getElementsByTagName('footer')[0];
let results = document.getElementsByClassName('container')[0];
let recipes = document.getElementsByClassName('recipes')[0];



// Load the search results
if (input) {
    input.addEventListener('input', function loadResults(e) {
        let xhr = new XMLHttpRequest();
        document.getElementById('search_message').innerHTML = '';
        document.getElementsByClassName('container')[0].innerHTML = '';
        footerTag.style.position = 'absolute';
        document.getElementsByClassName('container')[0].innerHTML = '';
        xhr.onload = function() {
            if (this.readyState === 4 && this.status === 200) {
                let response = xhr.responseText;
                document.getElementById('search_message').innerHTML = '';
                document.getElementsByClassName('container')[0].innerHTML = '';
                if (response == 0) {
                    
                }
            }
            else {
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


