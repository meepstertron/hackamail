from slack_sdk import WebClient
from slack_sdk.oauth import AuthorizeUrlGenerator
import os

class SlackService:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.USER_SCOPES = ["identity.basic", "identity.email"]
        self.WORKSPACE_SCOPES = []

    def generate_auth_url(self, state):
        generator = AuthorizeUrlGenerator(
            client_id=self.client_id,
            scopes=self.WORKSPACE_SCOPES,
            user_scopes=self.USER_SCOPES
        )
        return generator.generate(state=state)

    def exchange_code_for_token(self, code):
        client = WebClient()
        response = client.oauth_v2_access(
            client_id=self.client_id,
            client_secret=self.client_secret,
            code=code
        )
        # Convert SlackResponse to dictionary
        return {
            "access_token": response.get("access_token"),
            "authed_user": response.get("authed_user", {}),
            "team": response.get("team", {})
        }

    def get_user_identity(self, access_token):
        client = WebClient(token=access_token)
        response = client.users_identity()
        return {
            "user_id": response.get("user", {}).get("id"),
            "email": response.get("user", {}).get("email")
        }