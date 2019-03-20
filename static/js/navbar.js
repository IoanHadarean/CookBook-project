// Load the content


// Get all links
let navLinks = document.querySelectorAll('li a');

// Iterate through links
for (let i = 0; i < navLinks.length; i++) {

    // Customize login link
    if (navLinks[i].textContent == 'Login') {
        navLinks[i].style.backgroundColor = '#f26226';
        navLinks[i].style.height = '30px';
        navLinks[i].style.marginTop = '10px';
        navLinks[i].style.color = 'white';
        navLinks[i].style.display = 'flex';
        navLinks[i].style.alignItems = 'center';
        navLinks[i].style.justifyContent = 'center';
    }

    // Customize register link
    else if (navLinks[i].textContent == 'Register') {
        navLinks[i].style.backgroundColor = 'white';
        navLinks[i].style.height = '30px';
        navLinks[i].style.marginTop = '10px';
        navLinks[i].style.color = 'black';
        navLinks[i].style.display = 'flex';
        navLinks[i].style.alignItems = 'center';
        navLinks[i].style.justifyContent = 'center';
    }


    //Customize other links

    else {
        navLinks[i].style.display = 'flex';
        navLinks[i].style.alignItems = 'center';
        navLinks[i].style.justifyContent = 'center';
    }
}
