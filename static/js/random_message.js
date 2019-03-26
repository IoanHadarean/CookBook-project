// Load the content
// Added random welcome messages and colors array
// Added randomIndex to each of the messages and colors
// Colors array changes depending on the device width


const messages = ["WorldWide CookBook is super excited to have you onboard", "Doesn't that seem delicious? Try it out",
    "We predict that in the next minute you will go get something to eat", "There you go, welcome to our food fiesta!",
    "Take a look at these delicious recipes and get that frying pan out of the cupboard",
    "Is creativity your number one trait? Then you got the perfect matching recipes",
    "A recipe a day keeps the hunger away", "Recipes with love for your entire family!",
    "How are you going to resist? The answer is, you cannot",
    "For people that love to cook and try new things out"
];

if (screen.width <= 560) {
    let colorsMobile = ["#f26226", "#ADD8E6", "#4CAF50"];
    let welcomeHeaderMobile = document.getElementsByClassName("random-message")[0];
    const randomIndexMessagesMobile = Math.floor(Math.random() * messages.length);
    const randomIndexColorsMobile = Math.floor(Math.random() * colorsMobile.length);
    welcomeHeaderMobile.innerHTML = messages[randomIndexMessagesMobile];
    welcomeHeaderMobile.style.backgroundColor = colorsMobile[randomIndexColorsMobile];
}
else if (screen.width > 560) {
    let colorsDesktop = ["#ADD8E6", "#4CAF50"];
    const randomIndexMessagesDesktop = Math.floor(Math.random() * messages.length);
    const randomIndexColorsDesktop = Math.floor(Math.random() * colorsDesktop.length);

    let welcomeHeaderDesktop = document.getElementsByClassName("random-message")[0];

    welcomeHeaderDesktop.innerHTML = messages[randomIndexMessagesDesktop];
    welcomeHeaderDesktop.style.backgroundColor = colorsDesktop[randomIndexColorsDesktop];
}
