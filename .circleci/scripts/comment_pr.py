import os
import sys
import json
import argparse
from github import Github

import common


"""
Environment variables
"""

token = os.environ.get('GITHUB_ACCESS_TOKEN')
assert token, '[GITHUB_ACCESS_TOKEN] not set'

reponame = '{}/{}'.format(os.environ.get('CIRCLE_PROJECT_USERNAME'),
                          os.environ.get('CIRCLE_PROJECT_REPONAME'))
commit_id = os.environ.get('CIRCLE_SHA1')

pr_number = os.environ.get('CIRCLE_PR_NUMBER')
if not pr_number and 'CIRCLE_PULL_REQUEST' in os.environ:
    uri = os.environ.get('CIRCLE_PULL_REQUEST')
    pr_number = os.path.basename(uri)

is_pr = pr_number is not None


"""
Template
"""

PR_COMMENT_MSG = '''
**Submission completed**
Commit {} has been evaluated:

Task: {}
{}

Check out the leaderboard [here](https://hackathon.openrm.jp/) :trophy:
'''


# Init Github client
g = Github(token)

def comment_result(competition_info,
                   metrics,
                   reponame=reponame,
                   commit_id=commit_id,
                   pr_number=pr_number):
    if not is_pr:
        return
    repo = g.get_repo(reponame)
    pr = repo.get_pull(int(pr_number))
    body = PR_COMMENT_MSG.format(
        commit_id,
        competition_info.name,
        '\n'.join(['{}: `{}`'.format(k.capitalize(), v) for k, v in metrics.items()]))
    pr.create_issue_comment(body)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('task_id', type=str)
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    flags = parser.parse_args()

    metrics = json.load(flags.infile)
    competition_info = common.resolve_task(flags.task_id)

    comment_result(competition_info,
                   metrics)
