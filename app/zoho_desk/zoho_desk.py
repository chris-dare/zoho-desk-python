import json
import logging

import requests

from app.schemas import ZohoSelfClientApp


class ZohoDesk:
    def __init__(self, app: ZohoSelfClientApp, urls: dict = None):
        self.urls = urls
        if not self.urls:
            self.urls = {
                "oauth": "https://accounts.zoho.com/oauth/v2/token",
                "base_url": "https://desk.zoho.com/api/v1",
            }
        self.app = app
        if not self.app.access_token and not self.app.refresh_token:
            self.get_oauth_tokens()
        elif not self.app.refresh_token:
            self.refresh_oauth_tokens()

    def get_oauth_tokens(self) -> dict:
        payload = {
            "code": self.app.code,
            "grant_type": self.app.grant_types["authorization_code"],
            "client_id": self.app.client_id,
            "client_secret": self.app.client_secret,
            "redirect_uri": self.app.redirect_uri,
        }
        response = requests.post(self.urls["oauth"], params=payload)
        try:
            if response.status_code == 200 and not response.json().get("error"):
                logging.info("Successfully retrieved oauth tokens")
                tokens = response.json()
                self.app.access_token = tokens["access_token"]
                self.app.refresh_token = tokens["refresh_token"]
                tokens["status"] = True
            else:
                logging.error("Failed to retrieve oauth tokens")
                tokens = dict()
                tokens["status"] = False
        except (ValueError, KeyError) as e:
            pass  # there's no token
        return tokens

    def refresh_oauth_tokens(self) -> dict:
        if not self.app.refresh_token:
            tokens = self.get_oauth_tokens()
            if not tokens["status"]:
                return tokens
        else:
            payload = {
                "refresh_token": self.app.refresh_token,
                "scope": self.app.scope,
                "grant_type": self.app.grant_types["refresh_token"],
                "client_id": self.app.client_id,
                "client_secret": self.app.client_secret,
                "redirect_uri": self.app.redirect_uri,
            }
            response = requests.post(self.urls["oauth"], params=payload)
            logging.warning(response.url)
            try:
                if response.status_code == 200 and not response.json().get("error"):
                    tokens = response.json()
                    self.app.access_token = tokens["access_token"]
                    tokens["status"] = True
                else:
                    tokens = dict()
                    tokens["status"] = False
            except ValueError:
                pass  # there's no token
            return tokens

    def _get_authorization_header(self):
        """
        Returns an active access for making requests under the scope provided
        in self.app.scope
        """
        # TODO: Check that current access token is valid. Else refresh it
        authorization_header = {
            "Authorization": f"Zoho-oauthtoken {self.app.access_token}"
        }
        return authorization_header

    def get_departments(
        self,
        params: dict = {},
    ) -> dict:
        headers = self._get_authorization_header()
        #     params = {**params, 'isEnabled': True, "chatStatus": "AVAILABLE"}
        response = requests.get(
            f'{self.urls["base_url"]}/departments', headers=headers, params=params
        )
        if response.status_code == 200:
            data = response.json()
        else:
            data = {"error": True}
        return data

    def get_department(
        self,
        department_id: int,
        params: dict = {},
    ) -> dict:
        headers = self._get_authorization_header()
        #     params = {**params, 'isEnabled': True, "chatStatus": "AVAILABLE"}
        response = requests.get(
            f'{self.urls["base_url"]}/departments/{department_id}',
            headers=headers,
            params=params,
        )
        if response.status_code == 200:
            data = response.json()
        else:
            data = {"error": True}
        return data

    def get_tickets(
        self,
        params: dict = {},
    ) -> dict:
        headers = self._get_authorization_header()
        response = requests.get(
            f'{self.urls["base_url"]}/tickets', headers=headers, params=params
        )
        if response.status_code == 200:
            data = response.json()["data"]
        else:
            data = {"error": True}
        return data

    def create_ticket(
        self,
        payload: dict,
    ) -> dict:
        headers = self._get_authorization_header()
        response = requests.post(
            f'{self.urls["base_url"]}/tickets',
            headers=headers,
            data=json.dumps(payload),
        )
        if response.status_code == 201 or response.status_code == 200:
            data = response.json()
        else:
            data = {"error": True}
        return data