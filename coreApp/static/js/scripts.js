function log(a, b) {
    console.log(a, b)
}

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
        x.style.flexDirection = 'column'
    }
}

function openForm(a) {
    let theForm = document.getElementById(a)
    if(theForm.style.display == 'flex') {
        theForm.style.display = 'none'
        // log('open form if statement', 'triggered')
    } else {
        theForm.style.display = 'flex'
        theForm.style.flexDirection = 'column'
        theForm.style.border = '4px groove #54F1C4'
        theForm.style.padding = '.5em'
        // log('open form else statement', 'triggered')
    }
    console.log('what element', theForm)
}

function filterFoods() {
    var catId = document.getElementById('foodCat')
    var dropdown = document.getElementById('foodItemSelect')
    // allUrl = `http://127.0.0.1:8000/api/allFoodData/`
    allUrl = `https://dev.thehive-services.com/api/allFoodData/`
    // allUrl = `https://hivementor.beedev-services.com/api/allFoodData/`
    // oneUrl = `http://127.0.0.1:8000/api/foodData/`
    oneUrl = `https://dev.thehive-services.com/api/foodData/`
    // oneUrl = `https://hivementor.beedev-services.com/api/foodData/`
    catId = catId.value
    console.log(catId)
    if (catId  == 'All') {
        fetch(allUrl)
        .then(res => res.json())
        .then(data => {
            console.log(data.fList) 
            dropdown.innerHTML = '<option value="">Please Choose</option>'
            data.fList.forEach(item => {
                const option = document.createElement("option");
                option.value = item.id;
                option.textContent = `${item.food} ${item.calories}cal / per Serving`;
                dropdown.appendChild(option)
            })
        })
    }
    else if (catId == '') {
        console.log('wrong if')
    } else {
        console.log('else')
        fetch(`${oneUrl}${catId}`)
        .then(res => res.json())
        .then(data => {
            console.log(data.fList)
            dropdown.innerHTML = '<option value="">Please Choose</option>'
            data.fList.forEach(item => {
                const option = document.createElement("option");
                option.value = item.id;
                option.textContent = `${item.food} ${item.calories}cal / per Serving`;
                dropdown.appendChild(option)
            })
        })
    }
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

let chatUser

function enterChat(chatUser) {
    location.replace(`http://127.0.1:8000/chat/frame/${chatUser}/`)
}
function sendUserInfo(chatUser) {
    // chatUser = document.chat.theUser.value
    console.log('from django to js',chatUser)
    enterChat(chatUser)
}