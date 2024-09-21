function trackParcel() {
    alert("Tracking system coming soon!");
}
let counter = 1;
setInterval(function() {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if (counter > 3) {
        counter = 1;
    }
}, 5000); // Change image every 5 seconds
 