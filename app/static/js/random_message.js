// Load the content
// Added random welcome messages array
// Added randomIndex to each of the messages

const messages = ["WorldWide CookBook is super excited to have you onboard", "Doesn't that seem delicious? Try it out",
    "We predict that in the next minute you will go get something to eat", "There you go, welcome to our food fiesta!",
    "Look at these delicious recipes! Get that frying pan out of the cupboard!",
    "Is creativity your number one trait? Then you got the perfect matching recipes",
    "A recipe a day keeps the hunger away", "Recipes with love for your entire family!",
    "How are you going to resist? The answer is, you cannot",
    "For people that love to cook and try new things out"
];


let welcomeHeaderMobile = document.getElementsByClassName("random-message")[0];
const randomIndexMessagesMobile = Math.floor(Math.random() * messages.length);
welcomeHeaderMobile.innerHTML = messages[randomIndexMessagesMobile];


