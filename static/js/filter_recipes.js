// Get HTML elements
let filterButton = document.getElementById('filter-btn');
let footer = document.getElementsByTagName('footer')[0];
let selects = document.querySelectorAll('select');
let container = document.getElementsByClassName('container')[0];
let filterRecipes = document.getElementsByClassName('recipes')[0];
let filterResults = document.getElementById('num-results');
let activeFilterResults = document.getElementById('filter_results');
let btnFilterContainer = document.getElementById('filter-btn-container');

// Event listener for clicking disabled button
document.addEventListener('click', styleDisabledFilterButton);

// Adding a list of dictionaries for select options
var fullOptions = [{ "allergen_name": "" }, { "cuisine_name": "" }, { "course_name": "" }];
selects.forEach(select => select.onchange = function() {
    container.innerHTML = '';
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
    var searchRequest = null;
    xhr.open("POST", "/filter_results/" + allergenName + "/" + cuisineName + "/" + courseName, true);
    // Abort old pending requests
    if (searchRequest) {
        searchRequest.abort();
    }
    xhr.onload = function() {
        console.log(xhr.status);
        if (this.readyState === 4 && this.status === 200) {
            let filters = xhr.responseText;
            
            if (filters == "0") {
                if (filterResults) {
                    filterResults.innerHTML = '';
                }
                activeFilterResults.innerHTML = 'No recipes found';
                container.style.marginTop = '80px';
            }
            else {
                if (filters == "1") {
                    if (filterResults) {
                        filterResults.innerHTML = '';
                    }
                    activeFilterResults.innerHTML = filters + ' recipe was found';
                    container.style.marginTop = '80px';
                }
                else if (filters != "1") {
                    if (filterResults) {
                        filterResults.innerHTML = '';
                    }
                    activeFilterResults.innerHTML = filters + ' recipes were found';
                    container.style.marginTop = '80px';
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



// Fix footer according to results
if (container) {
    if (container.contains(filterRecipes)) {
        footer.style.position = 'relative';
    }
}


// Style the search button when it's disabled
function styleDisabledFilterButton() {
    if (btnFilterContainer) {
        let clickInside = btnFilterContainer.contains(event.target);
        if (clickInside) {
            filterButton.style.borderColor = 'black';
            filterButton.style.borderWidth = 'thin';
        }
        else {
            filterButton.style.borderColor = 'white';
        }
    }
}
