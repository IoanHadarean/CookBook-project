// Cancel profile update when reset progress button is clicked
let resetProgressButton = document.getElementsByClassName('event-clear')[0];
let addRecipe = document.getElementById('add-recipe');
resetProgressButton.addEventListener('click', resetAddRecipeForm);


function resetAddRecipeForm() {
    addRecipe.reset();
}