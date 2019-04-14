let filterButton = document.getElementById('tags_search_btn');


let selects = document.querySelectorAll('select');
selects.forEach(select => select.onchange = function() {
    console.log(select);
    return num_results();
});

function num_results() {
    filterButton.innerHTML = 'Processing...';
    let selectedOption = [];
    selects.forEach(select => selectedOption.push(select.options[select.selectedIndex]));
    console.log(selectedOption);
}

// let selectedOption = [];
// selects.forEach(select => selectedOption.push(select.options[select.selectedIndex]));
// console.log(selectedOption);
