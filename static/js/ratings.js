/* global localStorage */

// Get Rating Value
const numberRating = document.querySelector('.numbers-rating').innerHTML;

// Total Stars
const starsTotal = 5;

// Run getRatings when DOM loads
document.addEventListener('DOMContentLoaded', getRatings);

getRatings();

// Get Ratings
function getRatings() {
    // Get percetage
    const starPercentage = (numberRating / starsTotal) * 100;

    //Round to nearest 10
    const starPercentageRounded = `${Math.round(starPercentage / 10) * 10}%`;

    //Set width of stars inner to percentage
    document.querySelector('.stars-inner').style.width = starPercentageRounded;
}
