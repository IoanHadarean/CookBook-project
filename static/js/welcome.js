window.onload = function() {
    const messages = ["WorldWide CookBook is super excited to have you onboard", "Doesn't that seem delicious? Try it out",
        "We predict that in the next minute you will go get something to eat", "There you go, welcome to our food fiesta!",
        "Take a look at these delicious recipes and get that frying pan out of the cupboard",
        "Is creativity your number one trait? Then you got the perfect matching recipes",
        "A recipe a day keeps the hunger away", "Recipes with love for your entire family!",
        "How are you going to resist? The answer is, you cannot",
        "For people that love to cook and try new things out"
    ];

    const randomIndex = Math.floor(Math.random() * messages.length);

    document.getElementsByClassName("random-message")[0].innerHTML = messages[randomIndex];
};
