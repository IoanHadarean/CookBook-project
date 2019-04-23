// Add global variables
/* global localStorage */


// Get HTML Elements
const form = document.getElementById('recipe');
const firstAddButton = document.getElementsByClassName('add-ingredient')[0];
const firstDeleteButton = document.getElementsByClassName('delete-item')[0];
const ingredientsList = document.getElementById('ingredients-list');


// Add event listeners

loadEventListeners();


function loadEventListeners() {
    firstAddButton.addEventListener('click', addIngredient);
    firstDeleteButton.addEventListener('click', removeIngredient);
}








// function getIngredients() {
//     let ingredients;

//     if (localStorage.getItem('ingredients') === null) {
//         ingredients = [];
//     }
//     else {
//         ingredients = JSON.parse(localStorage.getItem('tasks'));
//     }

//     ingredients.forEach(function(ingredient) {
//         // Create li element
//         const li = document.createElement('li');
//         // Add li class
//         li.className = 'collection-item';
//         // Create text node and append to li
//         li.appendChild(document.createTextNode(task));
//         // Create new link element
//         const link = document.createElement('a');
//         // Add link class
//         link.className = 'delete-item secondary-content';
//         // Add icon html
//         link.innerHTML = '<i class = "fa fa-remove"></i>';
//         // Append link to li
//         li.appendChild(link);

//         // Append li to ul
//         taskList.appendChild(li);
//     });
// }



function addIngredient(e) {
    
    let ingredientsListLength = document.getElementsByClassName('ingredient').length;
    
    // Create elements
    const ingredient = document.createElement("div");
    const input = document.createElement('input');
    const addButton = document.createElement('button');
    const removeButton = document.createElement('button');
    
    // Add class to ingredient container
    ingredient.className = 'ingredient';
    
    // Add properties to input
    input.type = "text";
    input.name = `ingredient-${ingredientsListLength + 1}`;
    input.placeholder = "Please enter an ingredient";
    input.className = 'form-control';
    
    // Add properties to buttons
    addButton.className = 'add-ingredient';
    addButton.addEventListener('click', addIngredient);
    removeButton.addEventListener('click', removeIngredient);
    removeButton.classList = 'delete-item secondary-content';
    addButton.innerHTML += `<i class="material-icons right">add</i>`;
    removeButton.innerHTML += `<i class="material-icons right">clear</i>`;
    addButton.type = 'button';
    removeButton.type = 'button';
    
    // Append elements
    ingredient.appendChild(input);
    ingredient.appendChild(addButton);
    ingredient.appendChild(removeButton);
    ingredientsList.appendChild(ingredient);
    console.log(ingredient);
    e.preventDefault();
}
    
function removeIngredient(e) {
    let ingredientsListLength = document.getElementsByClassName('ingredient').length;
    console.log(ingredientsListLength);
    
    if (ingredientsListLength == 1) {
        console.log("Not Allowed");
    }
    else if (e.target.parentElement.classList.contains('delete-item')) {
        if (confirm('Are you sure you want to delete this ingredient?')) {
            e.target.parentElement.parentElement.remove();
        }
    }
}
