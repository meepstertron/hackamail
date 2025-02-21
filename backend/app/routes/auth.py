from flask import Blueprint, redirect, request, session
import secrets
from app.services.slack_service import SlackService
from dotenv import load_dotenv
import os

bp = Blueprint('auth', __name__)
load_dotenv('slack.env')

slack_service = SlackService(
    client_id=os.getenv("SLACK_CLIENT_ID"),
    client_secret=os.getenv("SLACK_CLIENT_SECRET")
)

@bp.route("/auth")
def auth():
    state = secrets.token_urlsafe(32)
    session['oauth_state'] = state
    auth_url = slack_service.generate_auth_url(state)
    return redirect(auth_url)

@bp.route("/oauth/callback")
def oauth_callback():
    if request.args.get("state") != session.get('oauth_state'):
        return {"success": False, "error": "Invalid state parameter"}
        
    try:
        auth_result = slack_service.exchange_code_for_token(request.args.get("code"))
        user_token = auth_result["authed_user"].get("access_token")
        user_data = slack_service.get_user_identity(user_token)
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}