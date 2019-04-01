// Get modal elements
let modal = document.getElementById('rating__modal');
let buttonModal = document.getElementById('rating__button');
let closeSpan = document.getElementsByClassName('close')[0];
let html = document.getElementsByTagName('html')[0];

// When the user clicks on the rate recipe button show modal
buttonModal.addEventListener('click', (e) => {
  modal.style.display = 'block';
  html.style.overflowY = 'hidden';
  // xStarRating.value = 0;
  // inputRating.value = 0;
});

// When the user clicks on span close modal
if (closeSpan) {
  closeSpan.addEventListener('click', (e) => {
    modal.style.display = 'none';
    html.style.overflowY = 'visible';
    // xStarRating.value = 0;
    // inputRating.value = 0;
  });
}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    html.style.overflowY = 'visible';
    // xStarRating.value = 0;
    // inputRating.value = 0;
  }
};
