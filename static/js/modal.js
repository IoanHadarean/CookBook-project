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


// let recipe_id;
// thumbsUp.addEventListener('click', loadLike);
// thumbsDown.addEventListener('click', loadDislike);

// function loadLike(e) {
//   $.post({
//       async: true,
//       url: "/get_recipe/" + recipe_id,
//   }).done(function(res) {
//     document.getElementById('likes__number').innerHTML = "Likes " + res.likes;
//   });
// }

// function loadDislike(e) {
//   $.post({
//       async: true,
//       url: "/get_recipe/" + recipe_id,
//   }).done(function(res) {
//     document.getElementById('likes__number').innerHTML = "Likes " + res.likes;
//     print("success");
//   });
// }



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

// thumbsUp.addEventListener('click', loadLike);
// thumbsDown.addEventListener('click', loadDislike);

// function loadLike(e) {
//   let xhr = new XMLHttpRequest();
//   xhr.onload = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       let response = JSON.parse(xhr.responseText);
//       console.log(response);
//       document.getElementById('likes__number').innerHTML = "Likes " + response.likes;
//     }
//   };
//   xhr.open("POST", "/like/5c7b948dfb6fc072012cbecc", true);
//   xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//   xhr.send();
//   e.preventDefault();
// }

// function loadDislike(e) {
//   let xhr = new XMLHttpRequest();
//   xhr.onload = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       let response = JSON.parse(xhr.responseText);
//       document.getElementById('likes__number').innerHTML = "Likes " + response.likes;
//     }
//   };
//   xhr.open("POST", "/dislike/5c7b948dfb6fc072012cbecc", true);
//   xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//   xhr.send();
//   e.preventDefault();
// }
