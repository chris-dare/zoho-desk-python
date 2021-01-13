import json 

from datetime import datetime, timezone, timedelta
from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl, EmailStr

from app.core.config import settings


class TicketSLA(BaseModel):
    response: timedelta = timedelta(hours=1)
    resolution: timedelta = timedelta(hours=7)
    priority: str = "HIGH"

ticket_sla = TicketSLA()

class Ticket(BaseModel):
#     id: int
    subject: str
    departmentId: Optional[int] = settings.ZOHO_DEFAULT_DEPARTMENT
    contact: Optional[dict]
    email: Optional[EmailStr]
    phone: Optional[str]
    description: Optional[str]
    status: Optional[str]
    assigneeId: Optional[int]
    category: Optional[str]
    subCategory: Optional[str]
    resolution: Optional[str]
    priority: Optional[str]
    language: Optional[str]
    channel: Optional[str]
    classification: Optional[str] # Type of ticket. Values supported are Problem, Request, Question, and Others
    cf: Optional[dict] # Custom fields in the ticket
    webUrl: Optional[HttpUrl]
    teamId: Optional[int]
    secondaryContacts: Optional[List]

    def non_empty_json(self):
        non_empty_fields = {k: v for k, v in self.dict().items() if v is not None}
        return json.dumps(non_empty_fields)
class ZohoTicket(Ticket):
    id: int
    contactId: Optional[str]
    productId: Optional[str]
    uploads: Optional[List]
    dueDate: Optional[str]
    responseDueDate: Optional[str]
