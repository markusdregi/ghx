import os
import yaml
import githubapimock as api

config_path = os.path.expanduser("~/repo.yml")
settings = yaml.load(open(config_path))

org = settings["org"]
repo = settings["repo"]
user = settings["user"]
token = settings["token"]

new_issues = yaml.load(open("issues.yml"))
for issue in new_issues:
    title = issue["title"]
    body = issue["body"]
    api.create_issue(org, repo, user, token, title, body)
    print("Created issue: " + title)
