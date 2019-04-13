// Get HTML elements
var searchButton = document.getElementById('submit_search');
var form = document.getElementById('search_form');
var input = document.getElementById('search_input');
var footerTag = document.getElementsByTagName('footer')[0];
var results = document.getElementsByClassName('container')[0];
var recipes = document.getElementsByClassName('recipes')[0];

// searchButton.addEventListener('click', resetForm);

// function resetForm() {
//     form.submit();
//     form.reset();
// }



// Load the search results
if (input) {
    input.addEventListener('input', function loadResults() {
        let xhr = new XMLHttpRequest();
        var inputValue = document.getElementById('search_input').value;
        document.getElementById('search_message').innerHTML = '';
        document.getElementsByClassName('container')[0].innerHTML = '';
        footerTag.style.position = 'absolute';
        inputValue = '';
        
        xhr.onload = function() {
            inputValue = '';
            if (this.readyState === 4 && this.status === 200) {
                let response = JSON.parse(xhr.responseText);
                var countResults = response;
                console.log(countResults);
                document.getElementById('search_message').innerHTML = '';
                if (countResults == 0) {
                    document.getElementById('search_message').innerHTML = 'No recipes were found';
                    inputValue = '';
                    document.getElementsByClassName('container')[0].innerHTML = '';
                }
                else {
                    document.getElementById('search_message').innerHTML = countResults + " matches were found";
                    inputValue = '';
                    document.getElementsByClassName('container')[0].innerHTML = '';
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
    });
}

if (results) {
    if (results.contains(recipes) || input.value != '') {
        footerTag.style.position = 'relative';
    }
}
