// Add global variables
/* global sessionStorage */



// Get HTML Elements
const instructionAddButtons = document.getElementsByClassName('add-instruction');
const instructionDeleteButtons = document.getElementsByClassName('delete-instruction');
const instructionsList = document.getElementById('instructions-list');

// Add event listeners

loadEventListeners();


function loadEventListeners() {
    window.addEventListener('load', getInstructions);
    for (var i = 0; i < instructionAddButtons.length; i++) {
        instructionAddButtons[i].addEventListener('click', addInstruction);
    }
    for (var j = 0; j < instructionDeleteButtons.length; j++) {
        instructionDeleteButtons[j].addEventListener('click', removeInstruction);
    }
}


// Get Instructions from session storage

function getInstructions() {
    let instructions;

    if (sessionStorage.getItem('editedInstructions') === null) {
        instructions = [];
    }
    else {
        instructions = JSON.parse(sessionStorage.getItem('editedInstructions'));
    }

    instructions.forEach(function(instruction) {

        // Create elements
        let instructionContainer = document.createElement('div');
        let input = document.createElement('input');
        let addButton = document.createElement('button');
        let removeButton = document.createElement('button');
        addButton.addEventListener('click', addInstruction);
        removeButton.addEventListener('click', removeInstruction);
        let addIcon = document.createElement('i');
        let deleteIcon = document.createElement('i');

        // Add class to instruction container
        instructionContainer.className = 'instruction';

        // Add properties to input
        input.type = "text";
        input.required = true;
        input.name = instruction;
        input.style.marginTop = '5px';
        input.placeholder = "Add Instruction";
        input.className = 'form-control';
        input.autocomplete = "off";
        input.minLength = "4";
        input.maxLength = "100";

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
        instructionsList.appendChild(instructionContainer);
    });
}




// Add Instruction

function addInstruction(e) {


    // Create elements
    const instruction = document.createElement('div');
    const input = document.createElement('input');
    const addButton = document.createElement('button');
    const removeButton = document.createElement('button');
    addButton.addEventListener('click', addInstruction);
    removeButton.addEventListener('click', removeInstruction);
    const addIcon = document.createElement('i');
    const deleteIcon = document.createElement('i');


    // Add class to ingredient container
    instruction.className = 'instruction';

    // Add properties to input
    input.type = "text";
    input.required = true;
    input.style.marginTop = '5px';
    input.name = `instruction-${Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15)}`;
    input.placeholder = "Add Instruction";
    input.className = 'form-control';
    input.autocomplete = "off";
    input.minLength = "4";
    input.maxLength = "100";

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
    storeInstructionInSessionStorage(input.name);

    e.preventDefault();
}


// Store Instruction in session storage
function storeInstructionInSessionStorage(instruction) {
    let instructions;

    if (sessionStorage.getItem('editedInstructions') === null) {
        instructions = [];
    }
    else {
        instructions = JSON.parse(sessionStorage.getItem('editedInstructions'));
    }


    instructions.push(instruction);

    sessionStorage.setItem('editedInstructions', JSON.stringify(instructions));
}




// Remove Instruction
function removeInstruction(e) {
    let instructionsListLength = document.getElementsByClassName('instruction').length;


    if (instructionsListLength == 1) {
        let nav = document.getElementsByTagName('nav')[0];
        instructionDeleteButtons[0].disabled = true;

        // Insert alert after nav and set one second timeout
        nav.insertAdjacentHTML('afterend', '<div id ="alert-edit-instruction" class = "alert alert-danger">You need to add at least one instruction</div>');
        setTimeout(() => {
            document.getElementById('alert-edit-instruction').remove();
            instructionDeleteButtons[0].disabled = false;
        }, 1200);
    }
    else if (e.target.parentElement.classList.contains('delete-instruction')) {
        e.target.parentElement.parentElement.remove();
        removeInstructionFromSessionStorage(e.target.parentElement.parentElement.firstChild);
    }
    else {
        e.target.parentElement.remove();
        removeInstructionFromSessionStorage(e.target.parentElement.firstChild);
    }

    e.preventDefault();
}



// Remove Instruction from session storage
function removeInstructionFromSessionStorage(instructionItem) {
    let instructions;

    if (sessionStorage.getItem('editedInstructions') === null) {
        instructions = [];
    }
    else {
        instructions = JSON.parse(sessionStorage.getItem('editedInstructions'));
    }

    instructions.forEach(function(instruction, index) {
        if (instructionItem.name === instruction) {
            instructions.splice(index, 1);
        }
    });

    sessionStorage.setItem('editedInstructions', JSON.stringify(instructions));
}
