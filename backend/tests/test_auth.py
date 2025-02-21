import pytest
from unittest.mock import MagicMock, patch
from app.services.slack_service import SlackService

def test_hello():
    assert 1 + 1 == 2

def test_slack_service_init():
    service = SlackService("test_id", "test_secret")
    assert service.client_id == "test_id"
    assert service.client_secret == "test_secret"
    assert "identity.basic" in service.USER_SCOPES
    assert "identity.email" in service.USER_SCOPES

@patch('slack_sdk.WebClient')
@patch('app.services.slack_service.WebClient')
def test_exchange_code_for_token(mock_web_client_import, mock_web_client):
    # Setup mock response
    mock_instance = MagicMock()
    mock_web_client_import.return_value = mock_instance
    
    mock_response = {
        "access_token": "test_token",
        "authed_user": {"id": "U123"},
        "team": {"id": "T123"}
    }
    mock_instance.oauth_v2_access.return_value = mock_response
    
    service = SlackService("test_id", "test_secret")
    result = service.exchange_code_for_token("test_code")
    
    mock_instance.oauth_v2_access.assert_called_once_with(
        client_id="test_id",
        client_secret="test_secret",
        code="test_code"
    )
    assert result == mock_response

@patch('slack_sdk.WebClient')
@patch('app.services.slack_service.WebClient')
def test_get_user_identity(mock_web_client_import, mock_web_client):
    # Setup mock response
    mock_instance = MagicMock()
    mock_web_client_import.return_value = mock_instance
    
    mock_response = {
        "user": {
            "id": "U123",
            "email": "test@example.com"
        }
    }
    mock_instance.users_identity.return_value = mock_response
    
    service = SlackService("test_id", "test_secret")
    result = service.get_user_identity("test_token")
    
    mock_instance.users_identity.assert_called_once()
    assert result == {
        "user_id": "U123",
        "email": "test@example.com"
    }
    
