function log(a, b) {
    console.log(a, b)
}


$(document).ready(function() {
    var mode = localStorage.getItem("mode");
    if(mode === "dark") {
        $( "body" ).addClass( "dark" );
        $( ".change" ).text( "Activate Light Mode" );
        $('#theMode').text("Dark Mode: ON");
    } else {
        $( "body" ).removeClass( "dark" );
        $( ".change" ).text( "Activate Dark Mode" );
        $('#theMode').text("Light Mode: ON");
    }
    $( ".change" ).on("click", function() {
        if( $( "body" ).hasClass( "dark" )) {
            $( "body" ).removeClass( "dark" );
            $( ".change" ).text( "Activate Dark Mode" );
            $('#theMode').text("Light Mode: ON");
            localStorage.setItem("mode", "light");
        } else {
            $( "body" ).addClass( "dark" );
            $( ".change" ).text( "Activate Light Mode" );
            $('#theMode').text("Dark Mode: ON");
            localStorage.setItem("mode", "dark");
        }
    });
});