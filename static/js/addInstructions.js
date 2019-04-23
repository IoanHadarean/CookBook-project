// Add global variables
/* global localStorage */


// Get HTML Elements
const firstInstruction = document.getElementsByClassName('add-instruction')[0];
const firstDeleteInstruction = document.getElementsByClassName('delete-instruction')[0];
const instructionsList = document.getElementById('instructions-list');


// Add event listeners

loadEventListeners();


function loadEventListeners() {
    // document.addEventListener('DOMContentLoaded', getInstructions);
    if (firstInstruction) {
        firstInstruction.addEventListener('click', addInstruction);
    }
    // if (firstDeleteInstruction) {
    //     firstDeleteInstruction.addEventListener('click', removeInstruction);
    // }
}



// Add Instruction

function addInstruction(e) {

    let instructionsListLength = document.getElementsByClassName('instruction').length;

    // Create elements
    const instruction = document.createElement('div');
    const input = document.createElement('input');
    const addButton = document.createElement('button');
    const removeButton = document.createElement('button');
    addButton.addEventListener('click', addInstruction);
    // removeButton.addEventListener('click', removeInstruction);
    const addIcon = document.createElement('i');
    const deleteIcon = document.createElement('i');

    // Add class to ingredient container
    instruction.className = 'instruction';

    // Add properties to input
    input.type = "text";
    input.style.marginTop = '5px';
    input.name = `instruction-${instructionsListLength + 1}`;
    input.placeholder = "Please enter an instruction";
    input.className = 'form-control';

    // Add properties to icons
    addIcon.className = 'material-icons right';
    deleteIcon.className = 'material-icons right';
    addIcon.innerHTML = 'add';
    deleteIcon.innerHTML = 'clear';

    // Add properties to buttons
    addButton.className = 'add-instruction secondary-content';
    removeButton.className = 'delete-instruction secondary-content';
    removeButton.style.marginLeft = '4px';
    addButton.type = 'button';
    removeButton.type = 'button';

    // Append elements
    addButton.appendChild(addIcon);
    removeButton.appendChild(deleteIcon);
    instruction.appendChild(input);
    instruction.appendChild(addButton);
    instruction.appendChild(removeButton);
    instructionsList.appendChild(instruction);

    // // Store Ingredient in local storage
    // storeIngredientInLocalStorage(input.name);

    e.preventDefault();
}
