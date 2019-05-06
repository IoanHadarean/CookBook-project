// Cancel profile update when reset progress button is clicked
let resetProgressButton = document.getElementsByClassName('reset-progress')[0];
let addRecipeForm = document.getElementById('add-recipe');
resetProgressButton.addEventListener('click', resetAddRecipeForm);


function resetAddRecipeForm() {
    addRecipeForm.reset();
}