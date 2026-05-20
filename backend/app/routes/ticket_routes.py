from typing import List
from fastapi import APIRouter
from fastapi import HTTPException
from app.kafka.producer import send_ticket


from app.schemas.ticket_schemas import (
    TicketRequest
)
from app.schemas.response_schema import (TicketResponse)

from app.ai_service import (
    classify_ticket,
    analyze_sentiment,
    predict_priority,
    generate_summary
)
from app.database.database import  (SessionLocal)
from app.database.models import Ticket

router = APIRouter()


@router.post("/ticket")
def process_ticket(ticket: TicketRequest):
    db=SessionLocal()
    try:

        category = classify_ticket(ticket.message)

        sentiment = analyze_sentiment(ticket.message)

        priority = predict_priority(ticket.message)

        summary = generate_summary(ticket.message)

        new_ticket=Ticket(message=ticket.message,
                        category=category,
                        sentiment=sentiment,
                        priority=priority,
                        summary=summary)
        db.add(new_ticket)
        db.commit()
        db.refresh(new_ticket)

        send_ticket({
            "message":ticket.message,
            "category":category,
            "sentiment":sentiment,
            "priority":priority
        })

        return {
            "id":new_ticket.id,
            "category": category,
            "sentiment": sentiment,
            "priority": priority,
            "summary": summary
        }
    except Exception as error:
        raise HTTPException(status_code=500,detail=str(error))from error
    finally:
        db.close()

@router.get('/tickets',response_model=List[TicketResponse])
def get_tickets(limit:int=5):
    db=SessionLocal()
    try:
        tickets=db.query(Ticket).order_by(Ticket.id.desc()).limit(limit).all()
        return tickets
    finally:
        db.close()

@router.get("/ticket/{ticket_id}",response_model=TicketResponse)
def get_ticket(ticket_id: int):

    db = SessionLocal()
    try:
        ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

        if not ticket:
            raise HTTPException(
                status_code=404,
                detail="Ticket not found"
            )
        return ticket

    finally:

        db.close()
