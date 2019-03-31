// Get all links
let navLinks = document.querySelectorAll('li a');

// Iterate through links
for (let i = 0; i < navLinks.length; i++) {

    // Customize login link
    if (navLinks[i].textContent == 'Login' || navLinks[i].textContent == 'Logout') {
        navLinks[i].style.backgroundColor = '#f26226';
        navLinks[i].style.color = 'white';
        navLinks[i].style.marginTop = '10px';
        navLinks[i].style.height = '30px';
        navLinks[i].style.width = '80px';
        navLinks[i].style.display = 'flex';
        navLinks[i].style.alignItems = 'center';
        navLinks[i].style.justifyContent = 'center';
    }

    // Customize register link
    else if (navLinks[i].textContent == 'Register') {
        navLinks[i].style.marginTop = '10px';
        navLinks[i].style.height = '30px';
        navLinks[i].style.width = '80px';
        navLinks[i].style.display = 'flex';
        navLinks[i].style.alignItems = 'center';
        navLinks[i].style.justifyContent = 'center';
    }
}
