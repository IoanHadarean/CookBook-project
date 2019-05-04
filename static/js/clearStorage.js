 /* global localStorage */


 // Clear local storage when user logs out, logs in or register
 // to prevent users from getting multiple ingredient inputs or instruction inputs
 // Note: even if not all the code below might be necessary, it's better to be preventive

 // Get HTML elements
 let loginNavbarButton = document.getElementById('login-button');
 let registerNavbarButton = document.getElementById('register-button');
 let logoutNavbarButton = document.getElementById('logout-button');
 let loginFormButton = document.getElementById('login-form-button');
 let registerFormButton = document.getElementById('register-form-button');
 let editRecipeButtons = document.getElementsByClassName('edit-button');
 let addRecipeForm = document.getElementById('add-recipe');
 let editRecipeForm = document.getElementById('edit-recipe');

 // Add event listeners for buttons, except for add and update recipe buttons
 let buttonsArray = [loginNavbarButton, registerNavbarButton, logoutNavbarButton, loginFormButton, registerFormButton];
 for (var i = 0; i < buttonsArray.length; i++) {
  if (buttonsArray[i]) {
   buttonsArray[i].addEventListener('click', clearLocalInformation);
  }
 }


 // Clear local storage when the add and edit recipe forms are submitted
 if (addRecipeForm) {
  addRecipeForm.addEventListener('submit', clearLocalInformation);
 }
 
 if (editRecipeForm) {
  editRecipeForm.addEventListener('submit', clearPartialInformation);
 }

 // Clear local storage when any edit button is clicked
 if (editRecipeButtons) {
  for (var i = 0; i < editRecipeButtons.length; i++) {
   editRecipeButtons[i].addEventListener('click', clearPartialInformation);
  }
 }


 // Clear local storage function
 function clearLocalInformation() {
  localStorage.clear();
 }
 
 // Clear just the editIngredients and editInstructions
 // from local storage so the user can go back to adding a recipe
 // This way, the user's inputs are saved even if the user decides
 // to leave the add recipe form and edit another recipe
 function clearPartialInformation() {
 localStorage.removeItem('editedIngredients');
 localStorage.removeItem('editedInstructions');
 }