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
        "venue": $(this).siblings("input.venue").val(),
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
    });
}


// Sends concert data to server via AJAX request for removal
function removeConcert(evt){
    evt.preventDefault();

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
        });

    }
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
    a = $(a);
    b = $(b);

    // Get concert's date from its hidden form input as an ISO String
    var aDate = new Date(a.find('input.start-datetime').val()).toISOString();
    var bDate = new Date(b.find('input.start-datetime').val()).toISOString();

    // Sort ascending
    if (aDate > bDate) {
        return 1;
    } else {
        return -1;
    }
}


// Sort results by artist's name
function sortByArtist(a, b){
    a = $(a);
    b = $(b);

    // Get concert's date from its hidden form input as an ISO String
    var aArtist = a.find('input.artist').val();
    var bArtist = b.find('input.artist').val();

    // Sort ascending
    if (aArtist > bArtist) {
        return 1;
    } else {
        return -1;
    }
}
