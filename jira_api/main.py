import schedule
from jira import Issue
from jira_api.data_fetcher import get_last_created_issue

from jira_api.db_api import cur


def main():
    issue: Issue = get_last_created_issue()
    print(issue.fields.issuetype)
    cur.execute("SELECT key FROM issues ORDER BY id DESC LIMIT 1;")
    f"INSERT INTO issues (key) VALUES ({issue.key}"
    last_bug_key = cur.fetchone()[0]
    print(last_bug_key, issue.key)
    if issue.key == last_bug_key:
        print("Last issue is - ", last_bug_key)


schedule.every(1).seconds.do(main)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
