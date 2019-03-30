/* global HTMLElement */

class StarRating extends HTMLElement  {
    
    // Highlight the stars depending on index
    highlight(index) {
        this.stars.forEach((star, i) => {
            star.classList.toggle('full', i <= index);
        });
    }
    constructor() {
        super();
        
        this.stars = [];
        
        
        // Create the div elements containing the stars
        for (let i = 0; i < 5; i++) {
            let star = document.createElement('div');
            console.log(star);
            star.className = 'star';
            this.appendChild(star);
            this.stars.push(star);
            console.log(this.stars);
        }
        
        // Add event listener for x-star-rating
        // Calculate the starIndex for each star
        this.addEventListener('mousemove', e => {
            let box = this.getBoundingClientRect(),
                starIndex = Math.floor((e.pageX - box.left) / box.width * this.stars.length);
            console.log(starIndex);
        });
    }
}

// register StarRating as an HTML element
window.customElements.define('x-star-rating', StarRating);