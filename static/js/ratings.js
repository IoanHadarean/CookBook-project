// Initial rating
const rating = 0;

// Total stars
const starsTotal = 5;

// Run getRatings when DOM loads
document.addEventListener('DOMContentLoaded', getRatings);

// Get ratings
function getRatings() {
    // Get percetage
    const starPercentage = (rating / starsTotal) * 100;
    
    //Round to nearest 10
    const starPercentageRounded = `${Math.round(starPercentage / 10) * 10}%`;
    
    //Set width of stars inner to percentage
    document.querySelector('.stars-inner').style.width = starPercentageRounded;
    
}