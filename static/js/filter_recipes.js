// Get HTML elements
let filterButton = document.getElementById('filter-btn');
let filterForm = document.getElementById('filter_form');
let footer = document.getElementsByTagName('footer')[0];
let selects = document.querySelectorAll('select');
let container = document.getElementsByClassName('container')[0];
let filterRecipes = document.getElementsByClassName('recipes')[0];
let filterResults = document.getElementById('num-results');


// Add on change event for selects



selects.forEach(select => select.onchange = function() {
    container.innerHTML = '';
    footer.style.position = 'absolute';
    filterButton.disabled = false;
    if (filterResults) {
        filterResults.innerHTML = '';
    }
    let fullOptions = [];
    let selectedOptions = [];
    selects.forEach(select => selectedOptions.push(select.options[select.selectedIndex]));
    console.log(selectedOptions);
    let constraints = ['choose-allergens', 'choose-cuisines', 'choose-courses'];
    let parsedSelects = selectedOptions.filter(parsed => !(constraints.includes(parsed.id)));
    console.log(parsedSelects);
    for (let i = 0; i < parsedSelects.length; i++) {
        let options = {};
        options[parsedSelects[i].name] = parsedSelects[i].value;
        fullOptions.push(options);
    }
    console.log(fullOptions);
});

// filterButton.addEventListener('click', getFilterResults);





// function getFilterResults() {
//     let xhr = new XMLHttpRequest();
//     xhr.open("POST", "/filter_results/" + options, true);
//     xhr.onload = function() {
//         if (this.readyState === 4 && this.status === 200) {
//             let response = xhr.responseText;
//             console.log(response);
//         }
//     };
//     xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//     xhr.onerror = function() {
//         console.log('Request error...');
//     };
//     xhr.send();
// }


// Fix footer according to results
if (container) {
    if (container.contains(filterRecipes)) {
        footer.style.position = 'relative';
    }
}

if (filterResults) {
    if (filterResults.innerHTML == 'No recipes found') {
        footer.style.position = 'absolute';
        filterButton.disabled = false;
    }
}
