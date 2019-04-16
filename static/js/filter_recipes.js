let filterButton = document.getElementById('tags_search_btn');
let filterForm = document.getElementById('filter_form');
let footer = document.getElementsByTagName('footer')[0];
let selects = document.querySelectorAll('select');
let container = document.getElementsByClassName('container')[0];
let filterRecipes = document.getElementsByClassName('recipes')[0];
selects.forEach(select => select.onchange = function() {
   container.innerHTML = '';
   footer.style.position = 'absolute';
});


filterButton.addEventListener('click', num_results);



function num_results() {
    let xhr = new XMLHttpRequest();
    xhr.onload = function() {
            if (this.readyState === 4 && this.status === 200) {
                let response = xhr.responseText;
                console.log(response);
            }
    };
    xhr.open("POST", "/filter_results", true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.send();
}

if (container) {
    if (container.contains(filterRecipes)) {
        footer.style.position = 'relative';
    }
    else {
        footer.style.position = 'absolute';
    }
}



