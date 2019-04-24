// Add global variables
/* global localStorage */


// Get HTML Elements
let footerInstructions = document.getElementsByTagName('footer')[0];
const firstInstruction = document.getElementsByClassName('add-instruction')[0];
const firstDeleteInstruction = document.getElementsByClassName('delete-instruction')[0];
const instructionsList = document.getElementById('instructions-list');

// Get the footer bottom style and parse it to integer
let footerStyleInstructions = window.getComputedStyle(footerInstructions, null);
let footerBottomValueInstructions = footerStyleInstructions.getPropertyValue("bottom");
let parsedBottomValueInstructions = parseInt(footerBottomValueInstructions, 10);

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


// Get Instructions from local storage

function getInstructions() {
    let instructions;

    if (localStorage.getItem('instructions') === null) {
        instructions = [];
    }
    else {
        instructions = JSON.parse(localStorage.getItem('instructions'));
    }

    instructions.forEach(function(instruction) {

        // Create elements
        const instructionContainer = document.createElement('div');
        const input = document.createElement('input');
        const addButton = document.createElement('button');
        const removeButton = document.createElement('button');
        addButton.addEventListener('click', addInstruction);
        removeButton.addEventListener('click', removeInstruction);
        const addIcon = document.createElement('i');
        const deleteIcon = document.createElement('i');
        
        // Get footer down by the height of the instruction input 
        parsedBottomValueInstructions -= 75;
        footerBottomValueInstructions = String(parsedBottomValueInstructions + 'px');
        footerInstructions.style.bottom = footerBottomValueInstructions;

        // Add class to instruction container
        instructionContainer.className = 'instruction';

        // Add properties to input
        input.type = "text";
        input.required = true;
        input.name = instruction;
        input.style.marginTop = '5px';
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
        instructionContainer.appendChild(input);
        instructionContainer.appendChild(addButton);
        instructionContainer.appendChild(removeButton);
        if (instructionsList) {
            instructionsList.appendChild(instructionContainer);
        }
    });
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
    removeButton.addEventListener('click', removeInstruction);
    const addIcon = document.createElement('i');
    const deleteIcon = document.createElement('i');
    
    // Get footer down by the height of the instruction input 
    parsedBottomValueInstructions -= 75;
    footerBottomValueInstructions = String(parsedBottomValueInstructions + 'px');
    footerInstructions.style.bottom = footerBottomValueInstructions;

    // Add class to ingredient container
    instruction.className = 'instruction';

    // Add properties to input
    input.type = "text";
    input.required = true;
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

    // Store Ingredient in local storage
    storeInstructionInLocalStorage(input.name);

    e.preventDefault();
}


// Store Instruction in local storage
function storeInstructionInLocalStorage(instruction) {
    let instructions;

    if (localStorage.getItem('instructions') === null) {
        instructions = [];
    }
    else {
        instructions = JSON.parse(localStorage.getItem('instructions'));
    }


    instructions.push(instruction);

    localStorage.setItem('instructions', JSON.stringify(instructions));
}


// Remove Instruction
function removeInstruction(e) {
    let instructionsListLength = document.getElementsByClassName('instruction').length;

    if (instructionsListLength == 1) {
        console.log("Not Allowed");
    }
    else if (e.target.parentElement.classList.contains('delete-instruction')) {
        e.target.parentElement.parentElement.remove();
        removeInstructionFromLocalStorage(e.target.parentElement.parentElement.firstChild);
    }
    else {
        e.target.parentElement.remove();
        removeInstructionFromLocalStorage(e.target.parentElement.firstChild);
    }

    e.preventDefault();
}



// Remove Instruction from local storage
function removeInstructionFromLocalStorage(instructionItem) {
    let instructions;

    if (localStorage.getItem('instructions') === null) {
        instructions = [];
    }
    else {
        instructions = JSON.parse(localStorage.getItem('instructions'));
    }

    instructions.forEach(function(instruction, index) {
        if (instructionItem.name === instruction) {
            instructions.splice(index, 1);
        }
    });

    localStorage.setItem('instructions', JSON.stringify(instructions));
}