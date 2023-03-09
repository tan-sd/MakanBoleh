// map-related functions

// create your map
function initMap(location, lodging) {
    
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        // center: {lat: 37.5665, lng:126.9780},
    }
    );
    // get capital from capitalList, get country code from function, get country from cache
    
    var capital = vm.get_capital_city(vm.get_country_code(vm.$data.trip_details.destination))
    // console.log(vm.$data.trip_details.destination)
    // console.log(vm.get_country_code(vm.$data.trip_details.destination))
    vm.set_country_center(capital,map)
    // map.addListener("click", (e) => {
    //     create_marker_by_click(e.latLng,map);
    // });
    for (var place in location) {
        // create_marker(place, map)
        create_marker(location[place], map, place)
    }
    // console.log(lodging)
    if (lodging != null) {
        create_lodging_marker(lodging, map)
    }
    
        
    initAutocomplete(map);
    

}
// enable Autocomplete
function initAutocomplete(map) {
    
    // Init Autocomplete
    var input = document.getElementById('autocomplete');
    // get country code
    
    var country = vm.get_country_code(vm.trip_details.destination)
    
    // console.log(country)
    const options = {
        componentRestrictions: {'country':country},
        fields: ['place_id','name','geometry','formatted_address']
    };
    const autocomplete = new google.maps.places.Autocomplete(input, options);
    // autocomplete connected to map viewport
    autocomplete.bindTo('bounds',map);
    
    // create marker for searched location, go to location, save into marker list
    autocomplete.addListener('place_changed', () => {

        const infowindow = new google.maps.InfoWindow();
        const icon = {
            url:  "http://maps.google.com/mapfiles/ms/icons/red-dot.png",
            scaledSize: new google.maps.Size(40,40),
            };
        var marker = new google.maps.Marker({
            map: map,
            icon: icon
        });
        
        infowindow.close()
        marker.setVisible(false);
        
        const place = autocomplete.getPlace();
        // console.log(place)
        vm.$data.selected_name = place.name;
        vm.$data.selected_address = place.formatted_address;
        vm.$data.selected_latlng = {lat: place.geometry.location.lat(), lng: place.geometry.location.lng()}
        
        
        if (!place.geometry || !place.geometry.location) {
        window.alert(`No details available for the place: "${place.name}"`
        );
        return;
        }
        if (place.geometry.viewport) {
        map.fitBounds(place.geometry.viewport);
        } else {
        map.setCenter(place.geometry.location);
        }

        marker.setPosition(place.geometry.location);
        marker.setVisible(true);

        marker.id = uniqueId;
        vm.$data.current_id = uniqueId
        // console.log(vm.$data.current_id)
        const contentString = 
        `
        <div id="content" name="${marker.id}">
            <div id="siteNotice"></div>

            <div class="container">
                <div class="row">
                    <div class = "col-8">
                    <span class="badge rounded-pill text-bg-warning">#Shopping</span>
                    <h3>${place.name}</h3>
                    <p class="address">${place.formatted_address}<p>
                    <hr>
                </div>  
            </div>
        </div>
        `
    // line for deleting marker by clicking in InfoWindow
    // <input type = 'button' va;ue = 'Delete' onclick = 'DeleteMarker( ${marker.id});' value = 'Delete Activity' />
    infowindow.setContent(contentString);
    infowindow.open(map, marker);
    markers.push(marker)
    marker.addListener("click", (googleMapsEvent) => {
        infowindow.open(map, marker);})
    marker.addListener("dblclick", (googleMapsEvent) => {
        infowindow.close(map, marker);})
    })
    window.autocomplete = autocomplete
    
    // autocomplete.addListener("", () => {
    //     autocomplete.set("place", null)
    // })
}
