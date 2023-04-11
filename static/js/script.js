/** Sets the time laps for the alert messages */

$(document).ready(function() {
    setTimeout(function(){
        if ($('#message-alert').length > 0) {
            $('#message-alert').remove();
        }
    }, 15000);
});