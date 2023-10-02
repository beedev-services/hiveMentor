let url = 'http://127.0.0.1:8000/api/trello/'

function loadData() {
    fetch(url)
    .then(res => res.json())
    .then(data => {
        console.log(data.status)
        // console.log(data.status.production)
    })
}
loadData()