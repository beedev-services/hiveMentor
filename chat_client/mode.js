// $(document).ready(function() {
//     var mode = localStorage.getItem("mode");
//     if(mode === "dark") {
//         $( "body" ).addClass( "dark" );
//         // $( ".change" ).text( "ON" );
//     } else {
//         $( "body" ).removeClass( "dark" );
//         // $( ".change" ).text( "OFF" );
//     }
//     // $( ".change" ).on("click", function() {
//     //     if( $( "body" ).hasClass( "dark" )) {
//     //         $( "body" ).removeClass( "dark" );
//     //         $( ".change" ).text( "OFF" );
//     //         localStorage.setItem("mode", "light");
//     //     } else {
//     //         $( "body" ).addClass( "dark" );
//     //         $( ".change" ).text( "ON" );
//     //         localStorage.setItem("mode", "dark");
//     //     }
//     // });
// });
// let theDiv = document.getElementById('root')
// let query
// window.addEventListener('message', function(event) {
//     console.log('pulling even from mode.js', event.data)
//     let myMode = event.data.mode
//     query = myMode
// })
// $(document).ready(function() {
//     if(query == 'dark') {
//         $('#theDiv').addClass("dark")
//     } else {
//         $('#theDiv').removeClass("dark")
//     }
// })