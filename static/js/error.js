// Get HTML alert
alert = document.querySelector('.alert');

// Clear alert after 3 seconds
setTimeout(clearError, 3000);


function clearError() {
    if (alert) {
        alert.remove();
    }
}