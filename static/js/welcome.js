window.onload = function(e) {
    const messages = ["Vegan CookBook is super excited to have you onboard", "Doesn't that seem delicious? Try it out",
        "We predict that in the next minute you will go get something to eat", "There you go, welcome to our food fiesta"
    ];

    const randomIndex = Math.floor(Math.random() * messages.length);

    document.getElementsByClassName("random-message")[0].innerHTML = messages[randomIndex];
    e.preventDefault();
};
