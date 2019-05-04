/* global date */


// Create UTC datetime to localtime for each user
var UTC = date + ' UTC';
document.getElementById('date-time').innerHTML = new Date(UTC).toLocaleString();


// Cancel profile update when reset progress button is clicked
let resetProgressButton = document.getElementsByClassName('reset-progress')[0];
let profileForm = document.getElementById('profile-form');
resetProgressButton.addEventListener('click', resetProfileUpdate);


function resetProfileUpdate() {
    profileForm.reset();
}
