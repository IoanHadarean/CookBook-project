// Add global variables
/* global sessionStorage */


// Get HTML Elements
const ingredientAddButtons = document.getElementsByClassName('add-ingredient');
const ingredientDeleteButtons = document.getElementsByClassName('delete-ingredient');
const ingredientsList = document.getElementById('ingredients-list');
const firstRemoveIngredientButton = document.getElementsByClassName('delete-ingredient')[0];



// Add event listeners

loadEventListeners();


function loadEventListeners() {
    window.addEventListener('load', getIngredients);
    for (var i = 0; i < ingredientAddButtons.length; i++) {
        ingredientAddButtons[i].addEventListener('click', addIngredient);
    }
    for (var j = 0; j < ingredientDeleteButtons.length; j++) {
        ingredientDeleteButtons[j].addEventListener('click', removeIngredient);
    }
}


// Get Ingredients from session storage

function getIngredients() {
    let ingredients;

    if (sessionStorage.getItem('editedIngredients') === null) {
        ingredients = [];
    }
    else {
        ingredients = JSON.parse(sessionStorage.getItem('editedIngredients'));
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
        input.placeholder = "Add Ingredient";
        input.className = 'form-control';
        input.autocomplete = "off";
        input.minLength = "3";
        input.maxLength = "50";

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
    input.style.marginTop = '5px';
    input.required = true;
    input.name = `ingredient-${ingredientsListLength + 1}`;
    input.placeholder = "Add Ingredient";
    input.className = 'form-control';
    input.autocomplete = "off";
    input.minLength = "3";
    input.maxLength = "50";

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
    storeIngredientInSessionStorage(input.name);

    e.preventDefault();
}



// Store Ingredient in session storage
function storeIngredientInSessionStorage(ingredient) {
    let ingredients;

    if (sessionStorage.getItem('editedIngredients') === null) {
        ingredients = [];
    }
    else {
        ingredients = JSON.parse(sessionStorage.getItem('editedIngredients'));
    }


    ingredients.push(ingredient);

    sessionStorage.setItem('editedIngredients', JSON.stringify(ingredients));
}


// Remove Ingredient 
function removeIngredient(e) {
    let ingredientsListLength = document.getElementsByClassName('ingredient').length;

    if (ingredientsListLength == 1) {
        firstRemoveIngredientButton.disabled = true;
        document.getElementById('alert-message').innerHTML = 'You need to add at least one ingredient';
        document.getElementById('alert-message').style.visibility = 'visible';
        setTimeout(function() {
            firstRemoveIngredientButton.disabled = false;
            document.getElementById('alert-message').style.visibility = 'hidden';
        }, 5000);
    }
    else if (e.target.parentElement.classList.contains('delete-ingredient')) {
        e.target.parentElement.parentElement.remove();
        removeIngredientFromSessionStorage(e.target.parentElement.parentElement.firstChild);
    }
    else {
        e.target.parentElement.remove();
        removeIngredientFromSessionStorage(e.target.parentElement.firstChild);
    }

    e.preventDefault();
}


// Remove Ingredient from session storage
function removeIngredientFromSessionStorage(ingredientItem) {
    let ingredients;
    if (sessionStorage.getItem('editedIngredients') === null) {
        ingredients = [];
    }
    else {
        ingredients = JSON.parse(sessionStorage.getItem('editedIngredients'));
    }

    ingredients.forEach(function(ingredient, index) {
        if (ingredientItem.name === ingredient) {
            ingredients.splice(index, 1);
        }
    });

    sessionStorage.setItem('editedIngredients', JSON.stringify(ingredients));
}
