window.onload = function() {
    let navList = document.querySelectorAll('li a');
    for (let i = 0; i < navList.length; i++) {
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
            navList[i].style.backgroundColor = 'white';
            navList[i].style.height = '30px';
            navList[i].style.marginTop = '10px';
            navList[i].style.color = 'black';
            navList[i].style.display = 'flex';
            navList[i].style.alignItems = 'center';
            navList[i].style.justifyContent = 'center';
            navList[i].style.marginRight = '30px';
        }
    }
    
        const messages = ["WorldWide CookBook is super excited to have you onboard", "Doesn't that seem delicious? Try it out",
        "We predict that in the next minute you will go get something to eat", "There you go, welcome to our food fiesta!",
        "Take a look at these delicious recipes and get that frying pan out of the cupboard",
        "Is creativity your number one trait? Then you got the perfect matching recipes",
        "A recipe a day keeps the hunger away", "Recipes with love for your entire family!",
        "How are you going to resist? The answer is, you cannot",
        "For people that love to cook and try new things out"
    ];

    let colors = ["#00FFFF", "#FFA57D", "#FFC0CB", "#8A2BE2","#ADD8E6"];
    const randomIndexMessages = Math.floor(Math.random() * messages.length);
    const randomIndexColors = Math.floor(Math.random() * colors.length);

    let welcomeHeader = document.getElementsByClassName("random-message")[0];

    welcomeHeader.innerHTML = messages[randomIndexMessages];
    welcomeHeader.style.backgroundColor = colors[randomIndexColors];

    window.addEventListener('resize', randomColors);

    function randomColors() {
        if (screen.width <= 560) {
            let colorsMobile = ["#8A2BE2","#ADD8E6"];
            let welcomeHeaderMobile = document.getElementsByClassName("random-message")[0];
            const randomIndexMessagesMobile = Math.floor(Math.random() * messages.length);
            const randomIndexColorsMobile = Math.floor(Math.random() * colorsMobile.length);
            welcomeHeaderMobile.innerHTML = messages[randomIndexMessagesMobile];
            welcomeHeaderMobile.style.backgroundColor = colorsMobile[randomIndexColorsMobile];
        }
        else if (screen.width > 560) {
            let colorsDesktop = ["#00FFFF", "#FFA57D", "#FFC0CB"];
            const randomIndexMessagesDesktop = Math.floor(Math.random() * messages.length);
            const randomIndexColorsDesktop = Math.floor(Math.random() * colorsDesktop.length);

            let welcomeHeaderDesktop = document.getElementsByClassName("random-message")[0];

            welcomeHeaderDesktop.innerHTML = messages[randomIndexMessagesDesktop];
            welcomeHeaderDesktop.style.backgroundColor = colorsDesktop[randomIndexColorsDesktop];
        }
    }
};
