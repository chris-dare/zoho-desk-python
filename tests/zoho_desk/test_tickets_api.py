import json
from typing import List
from app.api.deps import get_zoho_desk_api
from app.schemas import Ticket, ZohoTicket


def test_get_tickets():
    """Checks whether ZohoDesk.get_tickets is able to 
    retrieve ALL tickets on ZohoDesk successfully
    """
    zoho_desk = get_zoho_desk_api()
    tickets = zoho_desk.get_tickets()
    tickets = [ZohoTicket(**ticket) for ticket in tickets]
    ticket_types = [type(ticket)==ZohoTicket for ticket in tickets]
    assert(False not in ticket_types)


def test_create_ticket():
    """Test whether the Zoho Desk API can create a ticket on Zoho Desk
    TODO: Implement after adding api to delete a ticket
    """
    pass