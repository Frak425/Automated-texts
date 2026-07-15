import datetime
import json
import os

from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load env vars from keys.env
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "keys.env"))

# Credentials: either a file path in `GOOGLE_SERVICE_ACCOUNT_FILE`
# or the raw JSON in `GOOGLE_SERVICE_ACCOUNT_JSON`.
cred_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")

if cred_path:
    if not os.path.exists(cred_path):
        raise RuntimeError(f"Service account file not found: {cred_path}")
    credentials = service_account.Credentials.from_service_account_file(
        cred_path,
        scopes=["https://www.googleapis.com/auth/calendar"]
    )
else:
    raise RuntimeError(
        "Set GOOGLE_SERVICE_ACCOUNT_FILE=/path/to/key.json or set GOOGLE_SERVICE_ACCOUNT_JSON with the service account JSON"
    )

service = build(
    "calendar",
    "v3",
    credentials=credentials
)

calendar_id = os.getenv("CALENDAR_ID", "indiana@myclass101.com")

now = datetime.datetime.now(datetime.timezone.utc).isoformat()

events = service.events().list(
    calendarId=calendar_id,
    timeMin=now,
    maxResults=10,
    singleEvents=True,
    orderBy="startTime"
).execute()

for event in events.get("items", []):
    start = event["start"].get("dateTime", event["start"].get("date"))
    print(f"{start}: {event['summary']}")