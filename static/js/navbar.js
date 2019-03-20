window.onload = function() {
    let navList = document.querySelectorAll('li a');
    console.log(navList);
    for (let i = 0; i < navList.length; i++) {
        console.log(navList[i]);
        if (navList[i].textContent == 'Login') {
            navList[i].style.backgroundColor = '#f26226';
            navList[i].style.height = '30px';
            navList[i].style.marginTop = '10px';
            navList[i].style.color = 'white';
            navList[i].style.display = 'flex';
            navList[i].style.alignItems = 'center';
            navList[i].style.justifyContent = 'center';
        }
        else if (navList[i].textContent == 'Register') {
            navList[i].style.backgroundColor = '#f26226';
            navList[i].style.height = '30px';
            navList[i].style.marginTop = '10px';
            navList[i].style.color = 'white';
            navList[i].style.display = 'flex';
            navList[i].style.alignItems = 'center';
            navList[i].style.justifyContent = 'center';
        }
    }
};
