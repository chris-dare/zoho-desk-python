from typing import List, Optional
from pydantic import BaseModel


class ZohoApp(BaseModel):
    scope: List[str]
    expiry_time: Optional[int] = None
    client_id: str
    client_secret: str
    code: str
    grant_types: dict
    access_token: str = None
    refresh_token: str = None
    redirect_uri: str = "https://serenity.health"

    def get_authorization_header(self) -> str:
        return f"Zoho-oauthtoken {self.access_token}"


class ZohoSelfClientApp(ZohoApp):
    pass
