// Get HTML elements
let filterButton = document.getElementById('filter-btn');
let filterForm = document.getElementById('filter_form');
let footer = document.getElementsByTagName('footer')[0];
let selects = document.querySelectorAll('select');
let container = document.getElementsByClassName('container')[0];
let filterRecipes = document.getElementsByClassName('recipes')[0];
let filterResults = document.getElementById('num-results');
let activeFilterResults = document.getElementById('filter_results');





// // Add on change event for selects
// selects.forEach(select => select.onchange = function() {
//     container.innerHTML = '';
//     footer.style.position = 'absolute';
//     filterButton.disabled = false;
//     if (filterResults) {
//         filterResults.innerHTML = '';
//     }
// });


// Adding a list of dictionaries for select options
var fullOptions = [{ "allergen_name": "" }, { "cuisine_name": "" }, { "course_name": "" }];
selects.forEach(select => select.onchange = function() {
    container.innerHTML = '';
    footer.style.position = 'absolute';
    filterButton.disabled = false;
    if (filterResults) {
        filterResults.innerHTML = '';
    }
    let selectedOptions = [];
    selectedOptions.push(select.options[select.selectedIndex]);
    let constraints = ['choose-allergens', 'choose-cuisines', 'choose-courses'];
    let parsedSelects = selectedOptions.filter(parsed => !(constraints.includes(parsed.id)));
    if (select.id == 'course_name') {
        for (let i = 0; i < parsedSelects.length; i++) {
            fullOptions[2]["course_name"] = parsedSelects[i].value;
        }
    }
    if (select.id == 'cuisine_name') {
        for (let i = 0; i < parsedSelects.length; i++) {
            fullOptions[1]["cuisine_name"] = parsedSelects[i].value;
        }
    }
    if (select.id == 'allergen_name') {
        for (let i = 0; i < parsedSelects.length; i++) {
            fullOptions[0]["allergen_name"] = parsedSelects[i].value;
        }
    }
    let allergenName = fullOptions[0]["allergen_name"];
    let cuisineName = fullOptions[1]["cuisine_name"];
    let courseName = fullOptions[2]["course_name"];
    if (allergenName == '') {
        allergenName = 'None';
    }
    if (cuisineName == '') {
        cuisineName = 'None';
    }
    if (courseName == '') {
        courseName = 'None';
    }
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/filter_results/" + allergenName + "/" + cuisineName + "/" + courseName, true);

    xhr.onload = function() {
        console.log(xhr.status);
        if (this.readyState === 4 && this.status === 200) {
            let filters = xhr.responseText;
            if (filters == "0") {
                    if (filterResults) {
                        filterResults.innerHTML = '';
                    }
                    activeFilterResults.innerHTML = 'No recipes found';
                }
                else {
                    if (filters == "1") {
                        if (filterResults) {
                            filterResults.innerHTML = '';
                        }
                        activeFilterResults.innerHTML = filters + ' recipe was found';
                    }
                    else if (filters != "1") {
                        if (filterResults) {
                            filterResults.innerHTML = '';
                        }
                        activeFilterResults.innerHTML = filters + ' recipes were found';
                    }
                }
        }
    };
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhr.onerror = function() {
        console.log('Request error...');
    };
    xhr.send();
});









// function getFilterResults() {
//     let xhr = new XMLHttpRequest();
//     console.log(fullOptions);
//     xhr.open("POST", "/filter_results/" + allergenName + cuisineName + courseName, true);
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
    }
}
