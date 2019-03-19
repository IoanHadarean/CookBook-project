/* Custom js responsiveness for mobile devices */

window.onload = function() {
    
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
    if (screen.height <= 568) {
        Array.prototype.forEach.call(spans, span => {
            if (span.innerHTML.indexOf('Field must be between 6 and 50 characters long.') !== -1) {
                parsedBottomValue -= 40;
                styleBottomValue = String(parsedBottomValue + 'px');
                footer.style.bottom = styleBottomValue;
            }
            else if (span.innerHTML.indexOf('Invalid email address.') !== -1) {
                parsedBottomValue -= 20;
                console.log(parsedBottomValue);
                styleBottomValue = String(parsedBottomValue + 'px');
                footer.style.bottom = styleBottomValue;
            }
            else if (span.innerHTML.indexOf('Field must be between 15 and 50 characters long.') !== -1) {
                parsedBottomValue -= 40;
                console.log(parsedBottomValue);
                styleBottomValue = String(parsedBottomValue + 'px');
                footer.style.bottom = styleBottomValue;
            }
            else if (span.innerHTML.indexOf('Field must be between 6 and 25 characters long.') !== -1) {
                parsedBottomValue -= 40;
                console.log(parsedBottomValue);
                styleBottomValue = String(parsedBottomValue + 'px');
                footer.style.bottom = styleBottomValue;
            }
            else {
                parsedBottomValue -= 40;
                console.log(parsedBottomValue);
                styleBottomValue = String(parsedBottomValue + 'px');
                footer.style.bottom = styleBottomValue;
            }
        });
    }
};