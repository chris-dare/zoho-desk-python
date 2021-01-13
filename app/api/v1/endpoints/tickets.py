from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException

from app import schemas
from app.api import deps
from app.zoho_desk import ZohoDesk

router = APIRouter()

@router.get("/", response_model=List[schemas.ZohoTicket])
def get_tickets(params: Optional[dict]= {}, zoho_desk: ZohoDesk = Depends(deps.get_zoho_desk_api)) -> List[schemas.ZohoTicket]:
    tickets = zoho_desk.get_tickets()
    return [schemas.ZohoTicket(**ticket) for ticket in tickets] 

@router.post("/", response_model=schemas.ZohoTicket)
def create_ticket(
    ticket: schemas.Ticket, 
    zoho_desk: ZohoDesk = Depends(deps.get_zoho_desk_api)
) -> schemas.ZohoTicket:
    zoho_ticket = zoho_desk.create_ticket(ticket)
    return zoho_ticket
