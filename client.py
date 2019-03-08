import os
import yaml
import githubapimock as api

config_path = os.path.expanduser("~/repo.yml")
settings = yaml.load(open(config_path))

org = settings["org"]
repo = settings["repo"]
user = settings["user"]
token = settings["token"]

title = "My first client issue"
body = "This was created from the client application"
issue_id = api.create_issue(org, repo, user, token, title, body)

print("Created issue " + str(issue_id) + " in " + org + "/" + repo)

