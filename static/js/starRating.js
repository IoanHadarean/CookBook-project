/* global HTMLElement */

class StarRating extends HTMLElement  {
    
    get value() {
        return this.getAttribute('value');
    }
    
    set value(val) {
        this.setAttribute('value', val);
        this.highlight(this.value - 1);
    }
    
    // Highlight the stars depending on index
    highlight(index) {
        this.stars.forEach((star, i) => {
            star.classList.toggle('full', i <= index);
        });
    }
    constructor() {
        super();
        
        this.stars = [];
        this.value = this.value;
        
        
        let input = document.getElementById('rate');
        console.log(input);
        
        
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
            
            this.highlight(starIndex);
        });
        
        
        // When the mouse is out, reset the stars value to 0
        this.addEventListener('mouseout', () => {
            this.value = this.value;
            input.setAttribute('value', this.value);
            console.log(input);
        });
        
        // When the rating stars are clicked, the rating stays
        this.addEventListener('click', e => {
            let box = this.getBoundingClientRect(),
                starIndex = Math.floor((e.pageX - box.left) / box.width * this.stars.length);
            
            this.value = starIndex + 1;
            console.log(this.value);
        });
    }
}

// register StarRating as an HTML element
window.customElements.define('x-star-rating', StarRating);

