const colorMap = {
    '工作坊': '#7AC2B1',
    '分享會': '#FFA430',
    '比賽': '#E5A0A0'
}

const container = document.getElementById('events');

let events = [];
fetch("https://backend.cpsumsu.org/api/events")
    .then(function (res) {
        return res.json()
    })
    .then(function (result) {
        console.log(result.data)
        events = result.data
        createEventCards(events)
    })

function createEventCards(items) {
    let events = '';
    const CPS_URL = 'https://cps-website-eight.vercel.app/events';

    items.forEach(function (item) {
        const url = `${CPS_URL}/${item.id}`;
        const date = new Date(item.date);
        const formattedDate = `${date.getFullYear()}年${date.getMonth()}月${date.getDay()}日`;

        events += ` <div class="event">
                        <a target="_blank" href=${url}>
                            <div class="image-container">
                                <span class="type" style="background-color: ${colorMap[item.event_type]}">${item.event_type}</span>
                                <img src="${item.image}" alt="Post for ${item.name}">
                            </div>
                            <div class="event-info">
                                <p class="date">${formattedDate}</p>
                                <h3>${item.name}</h3>
                            </div>
                        </a>
                    </div>`
    })

    container.innerHTML = events;
}