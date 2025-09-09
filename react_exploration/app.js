import React, { useEffect, useState } from "react";
import { getTickets } from "./src/services/list";


function App() {
    const[tickets, setTickets] = useState([]);

    useEffect(() => {
        let mounted = true;
        getTickets()
            .then(tickets => {
                if(mounted) {
                    setTickets(tickets)
                }
            })
        return () => mounted = false;
    }, [])
    
    return(
        <div className="wrapper">
            <h1>My Grocery List</h1>
            <ul>
                {list.map(ticket => <li key={ticket.ticket}>{ticket.ticket}</li>)}
            </ul>
        </div>
    )
}

export default App;