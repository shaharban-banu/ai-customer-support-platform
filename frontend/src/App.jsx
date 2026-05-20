import { useEffect, useState } from "react";
import API from "./api/api";

import "./App.css";

function App() {

  const [message, setMessage] = useState("");

  const [tickets, setTickets] = useState([]);

  const [loading, setLoading] = useState(false);


  const fetchTickets = async () => {

    try {

      const response = await API.get("/tickets");

      setTickets(response.data);

    } catch (error) {

      console.log(error);
    }
  };


  useEffect(() => {

    fetchTickets();

  }, []);


  const submitTicket = async () => {

    if (!message) return;

    setLoading(true);

    try {

      await API.post(
        "/ticket",
        {
          message: message
        }
      );

      setMessage("");

      fetchTickets();

    } catch (error) {

      console.log(error);

    } finally {

      setLoading(false);
    }
  };


  return (

    <div className="container">

      <h1>
        AI Customer Support Intelligence Platform
      </h1>

      <div className="form-container">

        <textarea
          rows="4"
          placeholder="Enter customer issue..."
          value={message}
          onChange={(event) =>
            setMessage(event.target.value)
          }
        />

        <button onClick={submitTicket}>

          {
            loading
              ? "Processing..."
              : "Submit Ticket"
          }

        </button>

      </div>


      <h2>Tickets</h2>

      <div className="tickets">

        {
          tickets.map((ticket) => (

            <div
              key={ticket.id}
              className="ticket-card"
            >

              <p>
                <strong>Message:</strong>
                {" "}
                {ticket.message}
              </p>

              <p>
                <strong>Category:</strong>
                {" "}
                {ticket.category}
              </p>

              <p>
                <strong>Sentiment:</strong>
                {" "}

                <span
                  className={
                    ticket.sentiment === "Negative"
                      ? "negative"
                      : "positive"
                  }
                >
                  {ticket.sentiment}
                </span>
              </p>

              <p>
                <strong>Priority:</strong>
                {" "}

                <span
                  className={
                    ticket.priority === "high"
                      ? "high"
                      : "medium"
                  }
                >
                  {ticket.priority}
                </span>
              </p>

              <p>
                <strong>Summary:</strong>
                {" "}
                {ticket.summary}
              </p>

            </div>
          ))
        }

      </div>

    </div>
  );
}

export default App;