/* global localStorage */
/* global string */

// Initial Rating
let initialRating = 0;

localStorage.setItem('initialRating', initialRating);

// Total Stars
const starsTotal = 5;

// Run getRatings when DOM loads
document.addEventListener('DOMContentLoaded', getRatings);

// Form Elements
const ratingControl = document.getElementById('rating-control');
let input = document.querySelector('input[type = "number"]');
let placeholder = input.getAttribute('placeholder');


// Rating Control KeyUp
ratingControl.addEventListener('keyup', (e) => {
    const rating = e.target.value;

    // Make sure rating is 5 or under
    if (rating > 5) {
        alert('Please rate the recipe from 1 to 5');
        return;
    }

    // Change Rating
    initialRating = rating;
    
    localStorage.setItem('rating', rating);

    getRatings();
});


// Rating Control Change
ratingControl.addEventListener('change', (e) => {
    const rating = e.target.value;

    // Make sure rating is 5 or under
    if (rating > 5 || rating < 0) {
        alert('Please rate the recipe from 1 to 5');
        return;
    }
    
    // Change Rating
    initialRating = rating;
    
    localStorage.setItem('rating', rating);

    getRatings();
});


// Get Ratings
function getRatings() {
    // Get percetage
    const starPercentage = (initialRating / starsTotal) * 100;

    //Round to nearest 10
    const starPercentageRounded = `${Math.round(starPercentage / 10) * 10}%`;

    //Set width of stars inner to percentage
    document.querySelector('.stars-inner').style.width = starPercentageRounded;
}
