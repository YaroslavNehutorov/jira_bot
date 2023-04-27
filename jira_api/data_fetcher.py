from typing import List

from jira import JIRA, Issue

from config import JIRA_LOGIN, JIRA_TOKEN
from .loader import get_jira_client

jira_client: JIRA = get_jira_client(username=JIRA_LOGIN, token=JIRA_TOKEN)


def get_last_created_issue(project="intrusion"):
    result = jira_client.search_issues(jql_str=f'project = {project} AND type=\"BUG\"', maxResults=1)
    return result[0]


def get_list_of_issues(project="intrusion", max_results=50) -> List[Issue]:
    result = jira_client.search_issues(jql_str=f'project = {project}', maxResults=max_results)
    return result


if __name__ == '__main__':
    print(type(get_last_created_issue()))
    print(get_last_created_issue().key, get_last_created_issue().fields.summary)

