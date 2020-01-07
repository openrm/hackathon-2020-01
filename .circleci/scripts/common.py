import os
from github import Github

token = os.environ.get('GITHUB_ACCESS_TOKEN')
assert token, '[GITHUB_ACCESS_TOKEN] not set'

reponame = '{}/{}'.format(os.environ.get('CIRCLE_PROJECT_USERNAME'),
                          os.environ.get('CIRCLE_PROJECT_REPONAME'))
commit_id = os.environ.get('CIRCLE_SHA1')

pr_number = os.environ.get('CIRCLE_PR_NUMBER')
if not pr_number:
    uri = os.environ.get('CIRCLE_PULL_REQUEST')
    pr_number = os.path.basename(uri)

PR_COMMENT_MSG = '''
**Submission completed**
Commit {} has been evaluated:

Task: {}
{}

Check out the leaderboard [here]() :trophy:
'''

g = Github(token)

def comment_result(competition_info,
                   metrics,
                   reponame=reponame,
                   commit_id=commit_id,
                   pr_number=int(pr_number)):
    repo = g.get_repo(reponame)
    pr = repo.get_pull(pr_number)
    body = PR_COMMENT_MSG.format(
        commit_id,
        competition_info.name,
        '\n'.join(['{}: `{}`'.format(k, v) for k, v in metrics.items()]))
    pr.create_issue_comment(body)
