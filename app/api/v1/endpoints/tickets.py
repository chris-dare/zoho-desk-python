from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException

from app import schemas
from app.api import deps

router = APIRouter()

@router.get("/", response_model=List[schemas.ZohoTicket])
def get_tickets(params: Optional[dict]= {}) -> List[schemas.ZohoTicket]:
    return [schemas.ZohoTicket(**{"subject": "Test Ticket"})]

