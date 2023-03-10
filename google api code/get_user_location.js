// get the user's location from their wifi connection / mobile data.

// copy and paste the code below to get the location of the user when they open the site.

// call getLocation() to get coordinates of the user into two variables, latitude and longtitude.
function get_location() {
    console.log("get location function is running") // for troubleshooting
    console.log(x) // for troubleshooting
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(show_position);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}
function show_position(position) {
    var latitude = position.coords.latitude 
    var longitude = position.coords.longitude;
}

// assuming you have the destination and its address
function get_routing_url(destination) {
    var url = "https://maps.google.com?saddr=Current+Location&daddr=" + destination 
}

// assuming you have the destination in coordinates (lat, long)
function get_routing_url(destination) {
    var url = "https://maps.google.com?saddr=Current+Location&daddr=" + destination 
}