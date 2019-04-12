// Custom js responsiveness for mobile devices for profile //


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
if (screen.height <= 732 && screen.width < 768) {
    Array.prototype.forEach.call(spans, span => {
        if (span.innerHTML.indexOf('Field must be between 6 and 50 characters long.') !== -1) {
            parsedBottomValue -= 48;
            console.log(parsedBottomValue);
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Invalid email address.') !== -1) {
            parsedBottomValue -= 48;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 15 and 50 characters long.') !== -1) {
            parsedBottomValue -= 48;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 12 and 140 characters long.') !== -1) {
            parsedBottomValue -= 48;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else {
            parsedBottomValue -= 48;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
    });
}
else if (screen.height > 500 && screen.height <= 1080 && screen.width >= 768 && screen.width <= 2560) {
    Array.prototype.forEach.call(spans, span => {
        if (span.innerHTML.indexOf('Field must be between 6 and 50 characters long.') !== -1) {
            parsedBottomValue -= 80;
            console.log(parsedBottomValue);
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Invalid email address.') !== -1) {
            parsedBottomValue -= 80;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 15 and 50 characters long.') !== -1) {
            parsedBottomValue -= 80;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else if (span.innerHTML.indexOf('Field must be between 12 and 140 characters long.') !== -1) {
            parsedBottomValue -= 80;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
        else {
            parsedBottomValue -= 80;
            styleBottomValue = String(parsedBottomValue + 'px');
            footer.style.bottom = styleBottomValue;
        }
    });
}

// Create datetime for each user according to timezone

document.getElementById('date-time').innerHTML = new Date().toLocaleString();