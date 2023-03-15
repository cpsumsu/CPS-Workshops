const container = document.getElementById('event-container');

let a = 0;

fetch("https://backend.cpsumsu.org/api/events") 
    .then(function(res) {
        return res.json();
    })
    .then(function(result) {
        const events = result.data;
        let eventElements = '';

        events.forEach(function(item) {
            const date = new Date(item.date);
            const formattedDate = `${date.getFullYear()}年${date.getMonth()+1}月${date.getDay()+1}日`;

            eventElements += `<div class="event">
                                <div class="image-container">
                                    <img src="${item.image}" alt="">
                                    <span class="event-type">${item.event_type}</span>
                                </div>
                                <div class="event-info">
                                    <p class="date">${formattedDate}</p>
                                    <h3>${item.name}</h3>
                                </div>
                            </div>`;
        })

        container.innerHTML = eventElements;
    })

console.log("end of file");