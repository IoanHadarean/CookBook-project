/* global HTMLElement */

class StarRating extends HTMLElement  {
    constructor() {
        super();
        
        this.stars = [];
        
        for (let i = 0; i < 5; i++) {
            let star = document.createElement('div');
            console.log(star);
            star.className = 'star';
            this.appendChild(star);
            this.stars.push(star);
            console.log(this.stars);
        }
    }
}

// register StarRating as an HTML element

window.customElements.define('x-star-rating', StarRating);