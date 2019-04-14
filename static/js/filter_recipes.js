let filterButton = document.getElementById('tags_search_btn');


let selects = document.querySelectorAll('select');
selects.forEach(select => select.onchange = function() {
    return num_results();
});










function num_results() {
    filterButton.innerHTML = 'Processing...';
    let selectedOptions = [];
    selects.forEach(select => selectedOptions.push(select.options[select.selectedIndex]));

    let constraints = ['choose-allergens', 'choose-cuisines', 'choose-courses'];
    let parsedSelects = selectedOptions.filter(parsed => !(constraints.includes(parsed.id)));
    console.log(parsedSelects.length);
    if (parsedSelects.length == 0) {
        document.getElementById('results').innerHTML = '';
        document.getElementById('num-results').innerHTML = '';
        document.getElementById('tags_search_btn').innerHTML = 'Select a tag!';
        return false;
    }
    else {
        document.getElementById('tags_search_btn').disabled = false;
    }
    let options = {};
    for (let i = 0; i <parsedSelects.length; i++) {
        options[parsedSelects[i].name] = parsedSelects[i].value;
    }
    console.log(options);
    let xhr = new XMLHttpRequest();
    xhr.onload = function() {
            if (this.readyState === 4 && this.status === 200) {
                let response = xhr.responseText;
                console.log(response);
            }
    };
    xhr.open("POST", "/filter_results", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send(options);
}



