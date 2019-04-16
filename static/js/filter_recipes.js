let filterButton = document.getElementById('tags_search_btn');
let selects = document.querySelectorAll('select');
let container = document.getElementsByClassName('container')[0];
selects.forEach(select => select.onchange = () => container.innerHTML = '');

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



