# Creating GitHub issues with CSV using GitHub CLI

This is a sample script to create GitHub issues with CSV using GitHub CLI.

## Requirements

- Python 3.9
- [GitHub CLI](https://cli.github.com/)

No PyPI package is not required.

## Usage

Edit `create_github_issues_with_csv.py` and change `REPO`, `PROJECT` and `DATA`.

```python
REPO = "[owner]/[repo]"
PROJECT = "[projectname]"
DATA = """
Milestone 1,Task 1
Milestone 1,Task 2
Milestone 1,Task 3
Milestone 2,Task 4
Milestone 2,Task 5
"""
```

Run the script.

```bash
python create_github_issues_with_csv.py
```

## Other options

There are some other options to create many issues easily.

### [PyGithub](https://github.com/PyGithub/PyGithub)

[Create issue | Issues — PyGithub 1 documentation](https://pygithub.readthedocs.io/en/latest/examples/Issue.html#create-issue)

```python
from github import Github

issues = ...

g = Github("access_token")
repo = g.get_repo("[owner]/[repo]")

for issue in issues:
    repo.create_issue(title=issue.title)
```

### [GitHub CSV Tools](https://github.com/gavinr/github-csv-tools)

https://github.com/gavinr/github-csv-tools

```bash
githubCsvTools myFile.csv
```
