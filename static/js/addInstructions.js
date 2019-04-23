// Add global variables
/* global localStorage */


// Get HTML Elements
const firstInstruction = document.getElementsByClassName('add-instruction')[0];
const firstDeleteInstruction = document.getElementsByClassName('delete-instruction')[0];
const instructionsList = document.getElementById('instructions-list');


// Add event listeners

loadEventListeners();


function loadEventListeners() {
    document.addEventListener('DOMContentLoaded', getInstructions);
    if (firstInstruction) {
        firstInstruction.addEventListener('click', addInstruction);
    }
    if (firstDeleteInstruction) {
        firstDeleteInstruction.addEventListener('click', removeInstruction);
    }
}
