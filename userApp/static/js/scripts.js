function auth() {
    var l = document.getElementById('login')
    var r = document.getElementById('reg')
    var t = document.getElementById('text')
    if (r.style.display === 'flex') {
        r.style.display = 'none'
        l.style.display = 'flex'
        l.style.flexDirection = 'column';
        t.innerHTML = 'Register'
    } else {
        l.style.display = 'none'
        r.style.display = 'flex'
        r.style.flexDirection = 'column';
        t.innerHTML = 'Login'
    }
}

function menu() {
    var x = document.getElementById("myLinks")
    if(x.style.display === 'flex') {
        x.style.display = none
    } else {
        x.style.display = 'flex'
        x.style.flexDirection = 'columm'
    }
}




$(document).ready(function() {
    var mode = localStorage.getItem("mode");
    if(mode === "dark") {
        $( "body" ).addClass( "dark" );
        $( ".change" ).text( "ON" );
    } else {
        $( "body" ).removeClass( "dark" );
        $( ".change" ).text( "OFF" );
    }
    $( ".change" ).on("click", function() {
        if( $( "body" ).hasClass( "dark" )) {
            $( "body" ).removeClass( "dark" );
            $( ".change" ).text( "OFF" );
            localStorage.setItem("mode", "light");
        } else {
            $( "body" ).addClass( "dark" );
            $( ".change" ).text( "ON" );
            localStorage.setItem("mode", "dark");
        }
    });
});

let chatUser

function enterChat(chatUser) {
    location.replace(`http://127.0.1:8000/chat/frame/${chatUser}/`)
}
function sendUserInfo(chatUser) {
    // chatUser = document.chat.theUser.value
    console.log(chatUser)
    enterChat(chatUser)
}