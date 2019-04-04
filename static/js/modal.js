// Get modal elements
let ratingModal = document.getElementById('rating__modal');
let modal = document.getElementsByClassName('modal');
let likeModal = document.getElementById('like__modal');
let recipeModal = document.getElementById('recipe__modal');
let buttonModal = document.getElementById('rating__button');
let closeSpans = document.getElementsByClassName('close');
let thumbsUp = document.getElementsByClassName('fa-thumbs-up')[0];
let thumbsDown = document.getElementsByClassName('fa-thumbs-down')[0];
let likeButtons = [thumbsDown, thumbsUp];
let addRecipeButton = document.getElementsByClassName('box__link')[0];
let html = document.getElementsByTagName('html')[0];


// When the user clicks on the like/dislike button show modal
likeButtons.forEach(function(likeButton) {
  likeButton.addEventListener('click', (e) => {
    likeModal.style.display = 'block';
    html.style.overflowY = 'hidden';
  });
});

// When the user clicks on add recipe button show modal
addRecipeButton.addEventListener('click', (e) => {
  recipeModal.style.display = 'block';
  html.style.overflowY = 'hidden';
});


// When the user clicks on the rate recipe button show modal

buttonModal.addEventListener('click', (e) => {
  ratingModal.style.display = 'block';
  html.style.overflowY = 'hidden';
});


// When the user clicks on span close modal

for (var i = 0; i < closeSpans.length; i++) {
  if (closeSpans[i]) {
    closeSpans[i].addEventListener('click', (e) => {
      for (var i = 0; i < modal.length; i++) {
        modal[i].style.display = "none";
        html.style.overflowY = 'visible';
      }
    });
  }
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  for (var i = 0; i < modal.length; i++) {
    if (event.target == modal[i]) {
      modal[i].style.display = "none";
      html.style.overflowY = 'visible';
    }
  }
};