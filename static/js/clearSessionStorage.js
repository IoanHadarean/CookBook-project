 /* global sessionStorage */



 // Get HTML elements
 let editRecipeButtons = document.getElementsByClassName('edit-button');
 let addRecipeForm = document.getElementById('add-recipe');
 let editRecipeForm = document.getElementById('edit-recipe');



 // Clear session storage when the add and edit recipe forms are submitted
 if (addRecipeForm) {
     addRecipeForm.addEventListener('submit', clearLocalInformation);
 }

 if (editRecipeForm) {
     editRecipeForm.addEventListener('submit', clearPartialInformation);
 }

 // Clear session storage when any edit button is clicked
 if (editRecipeButtons) {
     for (var i = 0; i < editRecipeButtons.length; i++) {
         editRecipeButtons[i].addEventListener('click', clearPartialInformation);
     }
 }


 // Clear session storage function
 function clearLocalInformation() {
     sessionStorage.clear();
 }

 // Clear just the editIngredients and editInstructions
 // from session storage so the user can go back to adding a recipe
 // This way, the user's inputs are saved even if the user decides
 // to leave the add recipe form and edit another recipe
 function clearPartialInformation() {
     sessionStorage.removeItem('editedIngredients');
     sessionStorage.removeItem('editedInstructions');
 }
 