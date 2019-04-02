// Get modal elements
let ratingModal = document.getElementById('rating__modal');
let modal = document.getElementsByClassName('modal');
console.log(modal);
let likeModal = document.getElementById('like__modal');
let buttonModal = document.getElementById('rating__button');
let closeSpans = document.getElementsByClassName('close');
console.log(closeSpans);
let html = document.getElementsByTagName('html')[0];
let thumbsUp = document.getElementsByClassName('fa-thumbs-up')[0];
let thumbsDown = document.getElementsByClassName('fa-thumbs-down')[0];
let likeButtons = [thumbsDown, thumbsUp];

// When the user clicks on the rate recipe button show modal

likeButtons.forEach(function(likeButton) {
  likeButton.addEventListener('click', (e) => {
    likeModal.style.display = 'block';
    html.style.overflowY = 'hidden';
  });
});

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
