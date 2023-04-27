from jira import JIRA

from config import JIRA_SERVER


def get_jira_client(username: str, token: str) -> JIRA:
    return JIRA(server=JIRA_SERVER,
                basic_auth=(username, token))
