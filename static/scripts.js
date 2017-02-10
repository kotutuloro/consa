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