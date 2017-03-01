
/* -------------------------------------- HOMEPAGE FUNCTIONS -------------------------------------- */


// Send location search to Songkick API via GET request
function searchSongkickLoc(evt) {
    evt.preventDefault();

    // Create fieldset for locations
    var locFieldset = $("<fieldset>").attr("id", "loc-selection").hide();
    var legend = $("<legend>").text("Choose your area:");

    var loadingDiv = $("<div>").attr("id", "loc-loading").text("Loading...");
    var loadingImg = $("<img>").attr("src", "/static/img/load-gps.gif");
    loadingDiv.append(loadingImg);

    locFieldset.append(legend, loadingDiv);

    // Remove the previous fieldset and append new fieldset to form
    $("#loc-selection").remove();
    $("#loc-search-form").append(locFieldset);
    locFieldset.slideDown();

    // Make GET request to server and display locations
    var searchTerm = $("#location-input").val();
    $.get("/location-search", {'search-term': searchTerm}, displayLocs)

    // Display error message if GET request fails
        .fail(function(err){
            $("#loc-loading").slideUp();
            $("#loc-selection").append("Location search failed <br>" +
                                       err.status + ": " + err.statusText);
        });
}


// Display locations from JSON response from Songkick API
function displayLocs(locations) {
    // Remove loading notification
    $("#loc-loading").slideUp();

    // If locations found
    if (locations) {

    // Iterate through list of locations
    for (var i = 0; i < locations.length; i++) {

        // Get the metro area's information
        var metro = locations[i];
        var locID = metro.id;
        var locName;

        // Create location's name from metro area's display name, county, and state (if available)
        if (metro.state) {
            locName = metro.displayName + ", " + metro.state.displayName + ", " + metro.country.displayName;
        } else {
            locName = metro.displayName + ", " + metro.country.displayName;
        }

        // Create a radio button using the location's ID and name
        var locRadio = '<input type="radio" name="sk-loc" value="sk:' + locID + '">' + locName + '<br>';

        // Append radio button to location selection fieldset
        $("#loc-selection").append(locRadio);

        // Add ID & name to new radio button's data
        var latest = $("#loc-selection input:last");
        latest.data({"locID": "sk:" + locID, "locName": locName});
    }

    // If no locations found, inform user
    } else {
        $("#loc-selection").append("No matching areas found.");
    }
}


// Send artist search to Spotify API via GET request
function searchSpotifyArtist(evt) {
    evt.preventDefault();

    // Create div for artist results
    var artistSelectionDiv = $("<div>").attr("id", "artist-selection").hide();
    var legend = $("<h3>").text("Choose the correct artist(s):");

    var loadingDiv = $("<div>").attr("id", "artist-loading").text("Loading...");
    var loadingImg = $("<img>").attr("src", "/static/img/load-gps.gif");
    loadingDiv.append(loadingImg);

    artistSelectionDiv.append(legend, loadingDiv);

    // Remove the previous artist selection div and append new div to form
    $("#artist-selection").remove();
    $("#artist-search-form").append(artistSelectionDiv);
    artistSelectionDiv.slideDown();

    // Make GET request to server and display artist results
    var searchTerm = $("#artist-input").val();
    $.get("/artist-search", {'search-term': searchTerm}, displayArtists)

        // Display error message if GET request fails
        .fail(function(err){
            $("#artist-loading").slideUp();
            $("#artist-selection").append("Artist search failed <br>" +
                                          err.status + ": " + err.statusText);
        });
}


// Display artists from JSON response from Spotify API
function displayArtists(artists) {
    // Remove loading notification
    $("#artist-loading").slideUp();

    // If artists found
    if (artists) {

        // Iterate through list of artist results
        for (var i = 0; i < artists.length; i++) {
            var current = artists[i];

            // Create div for the artist with data embedded
            var artistDiv = $("<div>").addClass("artist-option");
            artistDiv.data({"spotifyID": current.spotify_id,
                            "artist": current.artist
                          });
            $("<h4>").text(current.artist).appendTo(artistDiv);

            // Add artist image if url available
            if (current.image_url) {
                $("<img>").attr("src", current.image_url).css('max-width', '100px').prependTo(artistDiv);
            }

            // Append artist to selection div
            $("#artist-selection").append(artistDiv);
        }

    // If no artists found, inform user
    } else {
        $("#artist-selection").append("No matching artists found.");
    }
}


// Add selected artist to chosen artists div
function chooseArtist(evt) {

    // Alert if too many artists chosen
    var numChosen = $("#chosen-artists-list").children("div").length;
    if (numChosen >= 10) {
        alert('Max artists selected');

    // If less than 10 artists chosen, add to div
    } else {
        // Clone clicked artist with data
        var artist = $(this).clone(true);

        // Check to see if clicked artist is already in the chosen artists div
        var alreadyChosen = false;
        $("#chosen-artists-list").children("div").each(function() {
            if ($(this).data("spotifyID") === artist.data("spotifyID")) {
                alreadyChosen = true;
            }
        });

        // Add clicked artist to chosen artists div if not already there
        if (!alreadyChosen) {
            artist.hide().prependTo("#chosen-artists-list").slideDown();
        }
    }
}


// Remove selected artist from chosen artists div
function removeChosenArtist(evt) {

    // Remove selected div
    $(this).slideUp(function() {
        $(this).remove();
    });
}


// Submit location data and redirect to spotify authorization url
function submitSpotifyAuth(evt) {
    evt.preventDefault();

    // Find selected location
    var selectedLoc = $('input[name="sk-loc"]:checked');

    // Send request to server with location's data and open returned url
    $.get('/spotify-auth', selectedLoc.data(), function(authurl) {
        window.location = authurl;
    }).fail(function(err){

    // Display error message if GET request fails
        alert("Spotify authorization failed: " + err.status + ": " + err.statusText);
    });
}


// Submit chosen artist and location data with no Spotify authorization
function submitNoAuth(evt) {
    evt.preventDefault();

    // Find selected location
    var selectedLoc = $('input[name="sk-loc"]:checked').data();

    // Get chosen artists' data
    var selectedArtists = {};
    $("#chosen-artists-list div.artist-option").each(function() {
        selectedArtists[$(this).data('spotifyID')] = $(this).data('artist');
    });

    // Alert if no artists selected
    if (Object.keys(selectedArtists).length === 0) {
        alert('Please select artists to use for the search.');

    // Otherwise, send data
    } else {
        // Merger selected artists & location data into payload
        var payload = Object.assign({}, selectedArtists, selectedLoc);

        // Create hidden form & inputs with location and chosen artists
        var noAuthForm = $("<form>").attr({"method": "POST", "action": "/no-auth-search"});
        for (var item in payload) {
            $("<input>").attr("name", item).val(payload[item]).appendTo(noAuthForm);
        }

        // Submit hidden form
        noAuthForm.hide().appendTo('body').submit();
    }
}



/* -------------------------------------- RESULTS FUNCTIONS -------------------------------------- */


// Sends concert data to server via AJAX request for addition to database
function addConcert(evt){
    evt.preventDefault();

    var thisButton = $(this);

    // Get hidden values of concert data in form
    var formInputs = {
        "songkick-id": $(this).siblings("input.songkick-id").val(),
        "songkick-url": $(this).siblings("input.songkick-url").val(),
        "display-name": $(this).siblings("input.display-name").val(),
        "artist": $(this).siblings("input.artist").val(),
        "spotify-id": $(this).siblings("input.spotify-id").val(),
        "image-url": $(this).siblings("input.image-url").val(),
        "venue-name": $(this).siblings("input.venue-name").val(),
        "venue-lat": $(this).siblings("input.venue-lat").val(),
        "venue-lng": $(this).siblings("input.venue-lng").val(),
        "city": $(this).siblings("input.city").val(),
        "start-datetime": $(this).siblings("input.start-datetime").val(),
    };

    // POST AJAX request to server
    $.post("/add-concert", formInputs, function(data) {
        // If the removal is successful, disable the button
        if (data == "True") {
            thisButton.prop("disabled", true);
            thisButton.val("Saved!");
        } else {
            // Alert user if unsuccessful
            alert('Cannot add this concert at this time.');
        }
    }).fail(function(err){
        // Display error message if GET request fails
        alert("Concert addition failed: " +
              err.status + ": " + err.statusText);
    });
}


// Sort concert divs based on button pressed
function sortConcerts(evt){
    var evtButton = $(this);

    // Get all concert divs and fade out
    var concerts = $('.concert-rec');
    concerts.fadeOut(function() {

        // Sort divs based on which button triggered event
        if (evtButton.hasClass('sort-by-date')) {
            concerts.sort(sortByDate);
        } else if (evtButton.hasClass('sort-by-artist')) {
            concerts.sort(sortByArtist);
        }

        // Remove and reattach sorted divs and fade in
        concerts.detach().appendTo($('#concert-results')).fadeIn();
    });
}


// Sort results by concert's date
function sortByDate(a, b){
    // Get concert's date from its hidden form input as an ISO String
    var aDate = new Date($(a).find('input.start-datetime').val()).toISOString();
    var bDate = new Date($(b).find('input.start-datetime').val()).toISOString();

    // Sort ascending
    if (aDate > bDate) {
        return 1;
    } else {
        return -1;
    }
}


// Sort results by artist's name
function sortByArtist(a, b){
    // Get concert's date from its hidden form input as an ISO String
    var aArtist = $(a).find('input.artist').val();
    var bArtist = $(b).find('input.artist').val();

    // Sort ascending
    if (aArtist > bArtist) {
        return 1;
    } else {
        return -1;
    }
}



/* -------------------------------------- PROFILE FUNCTIONS -------------------------------------- */


// Sends concert data to server via AJAX request for removal
function removeConcert(evt){
    evt.preventDefault();

    var thisButton = $(this);
    var thisDiv = $(this).closest("div");

    // Confirm deletion
    var confirmation = confirm("Are you sure you want to delete this?");
    if (confirmation) {

        // Get hidden value of songkick id in form
        var formInputs = {
            "songkick-id": $(this).siblings("input.songkick-id").val()
        };

        // POST AJAX request to server
        $.post("/remove-concert", formInputs, function(data) {
            // If the removal is successful, remove the concert's div
            if (data == "True") {
                thisDiv.slideUp();
            } else {
                // Alert user if unsuccessful
                alert('Cannot remove this concert at this time.');
            }
        }).fail(function(err){
            // Display error message if GET request fails
            alert("Concert removal failed: " +
                  err.status + ": " + err.statusText);
        });
    }
}


// Create a Google Maps object for a concert div
function createConcertMap(index) {

    // Get concert's coordinates from hidden inputs
    var venue = $(this).children("input.map-venue").val();
    var lat = $(this).children("input.map-lat").val();
    var lng = $(this).children("input.map-lng").val();
    var coords = {lat: parseFloat(lat),
                  lng: parseFloat(lng)};

    // Create map and marker in the div
    var map = new google.maps.Map(this, {center: coords,
                                         zoom: 14,
                                         gestureHandling: 'cooperative',
                                         mapTypeControl: false,
                                         streetViewControl: false
                                        });

    var marker = new google.maps.Marker({position: coords,
                                         map: map,
                                         animation: google.maps.Animation.DROP,
                                         title: venue,
                                        });

    // Open info window on marker click
    var infowindow = new google.maps.InfoWindow({
        content: "<h4>" + venue + "</h4>"
    });
    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });
}
