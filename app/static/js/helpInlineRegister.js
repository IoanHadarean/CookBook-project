/* Custom js responsiveness for mobile devices for register*/



// Declare element variables
let spans = document.getElementsByClassName('help-inline');
let footer = document.getElementsByTagName('footer')[0];

// Get the footer bottom style and parse it to integer
let footerStyle = window.getComputedStyle(footer, null);
let styleBottomValue = footerStyle.getPropertyValue("bottom");
let parsedBottomValue = parseInt(styleBottomValue, 10);

// Check for screen height and iterate through the spans
// Check for innerHTML of help-inline messages and get footer 
// down by the height of the span containing the message
// or by a height defined by the position of the footer
if (screen.height <= 768 && screen.width >= 321 && screen.width <= 732) {
    Array.prototype.forEach.call(spans, span => {
        if (span.innerHTML.indexOf('Field must be between 6 and 50 characters long.') !== -1) {
            parsedBottomValue -= 90;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Invalid email address.') !== -1) {
            parsedBottomValue -= 70;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 15 and 50 characters long.') !== -1) {
            parsedBottomValue -= 90;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 6 and 25 characters long.') !== -1) {
            parsedBottomValue -= 90;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else {
            parsedBottomValue -= 70;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
    });
}
else if (screen.height >= 812 && screen.width <= 480) {
     Array.prototype.forEach.call(spans, span => {
        if (span.innerHTML.indexOf('Field must be between 6 and 50 characters long.') !== -1) {
            parsedBottomValue -= 30;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Invalid email address.') !== -1) {
            parsedBottomValue -= 30;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 15 and 50 characters long.') !== -1) {
            parsedBottomValue -= 30;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 6 and 25 characters long.') !== -1) {
            parsedBottomValue -= 30;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else {
            parsedBottomValue -= 20;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
    });
}
else if (screen.width < 321) {
      Array.prototype.forEach.call(spans, span => {
        if (span.innerHTML.indexOf('Field must be between 6 and 50 characters long.') !== -1) {
            parsedBottomValue -= 110;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Invalid email address.') !== -1) {
            parsedBottomValue -= 110;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 15 and 50 characters long.') !== -1) {
            parsedBottomValue -= 110;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 6 and 25 characters long.') !== -1) {
            parsedBottomValue -= 110;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else {
            parsedBottomValue -= 100;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
    });
}
else if (screen.height >= 768 && screen.height <= 1080 && screen.width <= 1441) {
       Array.prototype.forEach.call(spans, span => {
        if (span.innerHTML.indexOf('Field must be between 6 and 50 characters long.') !== -1) {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Invalid email address.') !== -1) {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 15 and 50 characters long.') !== -1) {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 6 and 25 characters long.') !== -1) {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
    });
}
else if (screen.height <= 627 && screen.height <= 1080 && screen.width <= 1441) {
       Array.prototype.forEach.call(spans, span => {
        if (span.innerHTML.indexOf('Field must be between 6 and 50 characters long.') !== -1) {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Invalid email address.') !== -1) {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 15 and 50 characters long.') !== -1) {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 6 and 25 characters long.') !== -1) {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else {
            parsedBottomValue -= 50;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
    });
}



/* Custom box__link for alert so no interference with the alert modal is made */
let boxLink = document.getElementsByClassName('box__link')[0];
if (boxLink) {
    boxLink.style.display = 'flex';
    boxLink.style.height = '100%';
    boxLink.style.width = '100%';
    boxLink.style.alignItems = 'center';
    boxLink.style.justifyContent = 'center';
}
