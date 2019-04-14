var filterForm = document.getElementById('filter_form');
var options = document.getElementsByTagName('select');
var filterButton = document.getElementById('tags_search_btn');


let selects = document.querySelectorAll('select');
selects.forEach(select => select.onchange = function() {
    return num_results();
});

function num_results() {
    filterButton.innerHTML = 'Processing...';
}


