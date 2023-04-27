import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
JIRA_TOKEN = os.getenv("JIRA_TOKEN")
JIRA_SERVER = "https://ajaxsystems.atlassian.net"
JIRA_LOGIN = "nehutorov.y@ajax.systems"
