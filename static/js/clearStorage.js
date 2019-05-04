 /* global localStorage */




 // Get HTML elements
 let loginNavbarButton = document.getElementById('login-button');
 let registerNavbarButton = document.getElementById('register-button');
 let logoutNavbarButton = document.getElementById('logout-button');


 // Clear local storage when user logs out, logs in or register
 // to prevent users from getting multiple ingredient inputs or instruction inputs
 if (loginNavbarButton) {
     loginNavbarButton.addEventListener('click', clearLocalInformation);
 }
 if (registerNavbarButton) {
     registerNavbarButton.addEventListener('click', clearLocalInformation);
 }
 if (logoutNavbarButton) {
     logoutNavbarButton.addEventListener('click', clearLocalInformation);
 }

 function clearLocalInformation() {
     localStorage.clear();
 }
 