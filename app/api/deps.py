import logging
from typing import Generator

from fastapi import Depends, HTTPException, status
from dotenv import load_dotenv

from app import schemas
from app.core.config import settings
from app.zoho_desk import ZohoDesk


load_dotenv()
ZOHO_DESK_API = None

def get_zoho_desk_api() -> ZohoDesk:
    GRANT_TYPES = {
        "authorization_code": "authorization_code",
        "refresh_token": "refresh_token"
    }
    zoho_self_client_app_dict = {
        "code": settings.ZOHO_AUTHORIZATION_CODE,
        "scope": settings.ZOHO_OAUTH_SCOPES,
        "expiry_time": None,
        "client_id": settings.ZOHO_CLIENT_ID,
        "client_secret": settings.ZOHO_CLIENT_SECRET,
        "access_token": settings.ZOHO_ACCESS_TOKEN,
        "refresh_token": settings.ZOHO_REFRESH_TOKEN,
        "grant_types": GRANT_TYPES,
        "redirect_uri": "https://patient.serenity.health",
    }
    zoho_self_client_app = schemas.ZohoSelfClientApp(**zoho_self_client_app_dict)
    try:

        zohoDesk = ZohoDesk(app=zoho_self_client_app)
        return zohoDesk
    except Exception:
        logging.error("Error initializing ZohoDesk API")
