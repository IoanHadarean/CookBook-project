// Add global variables
/* global localStorage */


// Get HTML Elements
const firstAddButton = document.getElementsByClassName('add-ingredient')[0];
const firstDeleteButton = document.getElementsByClassName('delete-ingredient')[0];
const ingredientsList = document.getElementById('ingredients-list');


// Add event listeners

loadEventListeners();


function loadEventListeners() {
    document.addEventListener('DOMContentLoaded', getIngredients);
    if (firstAddButton) {
        firstAddButton.addEventListener('click', addIngredient);
    }
    if (firstDeleteButton) {
        firstDeleteButton.addEventListener('click', removeIngredient);
    }
}


// Get Ingredients from local storage

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
        input.style.marginTop = '5px';
        input.required = true;
        input.placeholder = "Please enter an ingredient";
        input.className = 'form-control';

        // Add properties to icons
        addIcon.className = 'material-icons right';
        deleteIcon.className = 'material-icons right';
        addIcon.innerHTML = 'add';
        deleteIcon.innerHTML = 'clear';

        // Add properties to buttons
        addButton.className = 'add-ingredient secondary-content';
        removeButton.className = 'delete-ingredient secondary-content';
        removeButton.style.marginLeft = '4px';
        addButton.type = 'button';
        removeButton.type = 'button';

        // Append elements
        addButton.appendChild(addIcon);
        removeButton.appendChild(deleteIcon);
        ingredientContainer.appendChild(input);
        ingredientContainer.appendChild(addButton);
        ingredientContainer.appendChild(removeButton);
        if (ingredientsList) {
            ingredientsList.appendChild(ingredientContainer);
        }
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
    input.style.marginTop = '5px';
    input.required = true;
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
    removeButton.className = 'delete-ingredient secondary-content';
    removeButton.style.marginLeft = '4px';
    addButton.type = 'button';
    removeButton.type = 'button';

    // Append elements
    addButton.appendChild(addIcon);
    removeButton.appendChild(deleteIcon);
    ingredient.appendChild(input);
    ingredient.appendChild(addButton);
    ingredient.appendChild(removeButton);
    ingredientsList.appendChild(ingredient);

    // Store Ingredient in local storage
    storeIngredientInLocalStorage(input.name);

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

    if (ingredientsListLength == 1) {
        console.log("Not Allowed");
    }
    else if (e.target.parentElement.classList.contains('delete-ingredient')) {
        e.target.parentElement.parentElement.remove();
        removeIngredientFromLocalStorage(e.target.parentElement.parentElement.firstChild);
    }
    else {
        e.target.parentElement.remove();
        removeIngredientFromLocalStorage(e.target.parentElement.firstChild);
    }

    e.preventDefault();
}


// Remove Ingredient from local storage
function removeIngredientFromLocalStorage(ingredientItem) {
    let ingredients;
    if (localStorage.getItem('ingredients') === null) {
        ingredients = [];
    }
    else {
        ingredients = JSON.parse(localStorage.getItem('ingredients'));
    }

    ingredients.forEach(function(ingredient, index) {
        if (ingredientItem.name === ingredient) {
            ingredients.splice(index, 1);
        }
    });

    localStorage.setItem('ingredients', JSON.stringify(ingredients));
}
