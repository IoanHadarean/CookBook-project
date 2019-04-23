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
    document.addEventListener('DOMContentLoaded', getIngredients);
    firstAddButton.addEventListener('click', addIngredient);
    firstDeleteButton.addEventListener('click', removeIngredient);
}








function getIngredients() {
    let ingredients;

    if (localStorage.getItem('ingredients') === null) {
        ingredients = [];
    }
    else {
        ingredients = JSON.parse(localStorage.getItem('ingredients'));
    }

    ingredients.forEach(function(ingredient) {
        
        // Create elements
        const ingredientContainer = document.createElement('div');
        const input = document.createElement('input');
        const addButton = document.createElement('button');
        const removeButton = document.createElement('button');
        addButton.addEventListener('click', addIngredient);
        removeButton.addEventListener('click', removeIngredient);
        const addIcon = document.createElement('i');
        const deleteIcon = document.createElement('i');

        // Add class to ingredient container
        ingredientContainer.className = 'ingredient';

        // Add properties to input
        input.type = "text";
        input.name = ingredient;
        input.placeholder = "Please enter an ingredient";
        input.className = 'form-control';

        // Add properties to icons
        addIcon.className = 'material-icons right';
        deleteIcon.className = 'material-icons right';
        addIcon.innerHTML = 'add';
        deleteIcon.innerHTML = 'clear';

        // Add properties to buttons
        addButton.className = 'add-ingredient secondary-content';
        removeButton.className = 'delete-item secondary-content';
        addButton.type = 'button';
        removeButton.type = 'button';

        // Append elements
        addButton.appendChild(addIcon);
        removeButton.appendChild(deleteIcon);
        ingredientContainer.appendChild(input);
        ingredientContainer.appendChild(addButton);
        ingredientContainer.appendChild(removeButton);
        ingredientsList.appendChild(ingredientContainer);
    });
}



// Add Ingredient

function addIngredient(e) {

    let ingredientsListLength = document.getElementsByClassName('ingredient').length;

    // Create elements
    const ingredient = document.createElement('div');
    const input = document.createElement('input');
    const addButton = document.createElement('button');
    const removeButton = document.createElement('button');
    addButton.addEventListener('click', addIngredient);
    removeButton.addEventListener('click', removeIngredient);
    const addIcon = document.createElement('i');
    const deleteIcon = document.createElement('i');

    // Add class to ingredient container
    ingredient.className = 'ingredient';

    // Add properties to input
    input.type = "text";
    input.name = `ingredient-${ingredientsListLength + 1}`;
    input.placeholder = "Please enter an ingredient";
    input.className = 'form-control';

    // Add properties to icons
    addIcon.className = 'material-icons right';
    deleteIcon.className = 'material-icons right';
    addIcon.innerHTML = 'add';
    deleteIcon.innerHTML = 'clear';

    // Add properties to buttons
    addButton.className = 'add-ingredient secondary-content';
    removeButton.className = 'delete-item secondary-content';
    addButton.type = 'button';
    removeButton.type = 'button';

    // Append elements
    addButton.appendChild(addIcon);
    removeButton.appendChild(deleteIcon);
    ingredient.appendChild(input);
    ingredient.appendChild(addButton);
    ingredient.appendChild(removeButton);
    ingredientsList.appendChild(ingredient);
    console.log(ingredient);

    // Store Ingredient in local storage
    storeIngredientInLocalStorage(input.name);

    input.name = '';

    e.preventDefault();
}



// Store Ingredient in local storage
function storeIngredientInLocalStorage(ingredient) {
    let ingredients;

    if (localStorage.getItem('ingredients') === null) {
        ingredients = [];
    }
    else {
        ingredients = JSON.parse(localStorage.getItem('ingredients'));
    }

    ingredients.push(ingredient);

    localStorage.setItem('ingredients', JSON.stringify(ingredients));
}


// Remove Ingredient 
function removeIngredient(e) {
    let ingredientsListLength = document.getElementsByClassName('ingredient').length;
    console.log(ingredientsListLength);

    if (ingredientsListLength == 1) {
        console.log("Not Allowed");
    }
    else if (e.target.parentElement.classList.contains('delete-item')) {
        e.target.parentElement.parentElement.remove();
    }
    else {
        e.target.parentElement.remove();
    }

    e.preventDefault();
}
