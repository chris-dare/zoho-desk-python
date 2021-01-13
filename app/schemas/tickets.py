from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, HttpUrl

from datetime import datetime, timezone, timedelta
from typing import List, Optional, Union
from pydantic import BaseModel, HttpUrl, EmailStr


class TicketSLA(BaseModel):
    response: timedelta = timedelta(hours=1)
    resolution: timedelta = timedelta(hours=7)
    priority: str = "HIGH"

ticket_sla = TicketSLA()
#     id: int
    subject: str
    departmentId: Optional[int]
    contactId: Optional[str]
    contact: Optional[dict]
    productId: Optional[str]
    uploads: Optional[List]
    email: Optional[str]
    phone: Optional[str]
    description: Optional[str]
    status: Optional[str]
    assigneeId: Optional[int]
    category: Optional[str]
    subCategory: Optional[str]
    resolution: Optional[str]
    dueDate: Optional[datetime]
    priority: Optional[str]
    language: Optional[str]
    responseDueDate: Optional[datetime]
    channel: Optional[str]
    classification: Optional[str] # Type of ticket. Values supported are Problem, Request, Question, and Others
    cf: Optional[dict] # Custom fields in the ticket
    webUrl: Optional[HttpUrl]
    teamId: Optional[int]
    secondaryContacts: Optional[List]