export function getTickets() {
    return fetch('http://localhost:3333/list')
    .then(data => data.json)
}