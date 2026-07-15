import google_auth_oauthlib
import googleapiclient
import twilio
import schedule
import sqlalchemy
import google.auth
import logging
from twilio.rest import Client
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv("keys.env")

api_key = os.getenv("TWILIO_API_KEY_SID")
api_key_secret = os.getenv("TWILIO_API_KEY_TOKEN")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
service_sid = os.getenv("TWILIO_MESSAGING_SERVICE_SID")

client = Client(
    username=api_key,
    password=api_key_secret,
    account_sid=account_sid,
)

message = client.messages.create(
    messaging_service_sid=service_sid,
    body="Hello, this is a test message!",
    to="+18128372222"
)

print(message.sid)

#This works!