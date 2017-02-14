// Sends concert data to server via AJAX request for addition to database
function addConcert(evt){
    evt.preventDefault();

    var thisButton = $(this);

    // Get hidden values of concert data in form
    var formInputs = {
        "songkick-id": $(this).siblings("input.songkick-id").val(),
        "songkick-url": $(this).siblings("input.songkick-url").val(),
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
                thisDiv.hide();
            } else {
                // Alert user if unsuccessful
                alert('Cannot remove this concert at this time.');
            }
        });

    }
}