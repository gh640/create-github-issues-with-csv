"""Create GitHub issues with CSV using GitHub CLI """

import asyncio
import csv
import io
import sys
from asyncio import create_subprocess_exec
from asyncio.subprocess import PIPE
from asyncio.tasks import as_completed
from functools import partial
from typing import Generator

REPO = "[owner]/[repo]"
PROJECT = "[projectname]"
DATA = """
Milestone 1,Task 1
Milestone 1,Task 2
Milestone 1,Task 3
Milestone 2,Task 4
Milestone 2,Task 5
"""


async def main() -> None:
    """Main function"""
    issues = [x for x in read_data(DATA)]

    build_command_ = partial(build_command, body="", repo=REPO, project=PROJECT)
    commands = [
        build_command_(title=title, milestone=milestone) for milestone, title in issues
    ]

    for coro in asyncio.as_completed(
        [run(program, args) for program, args in commands]
    ):
        stdout, stderr = await coro
        print(stdout.rstrip())
        if stderr:
            print(stderr.rstrip(), file=sys.stderr)


def read_data(csv_text: str) -> Generator[tuple, None, None]:
    """Load issue data from CSV text"""
    reader = csv.reader(io.StringIO(csv_text))
    for row in reader:
        if not row:
            continue
        yield row


def build_command(
    repo: str, title: str, body: str, milestone: str, project: str
) -> tuple[str, list[str]]:
    """Build command to create an issue with GitHub CLI"""
    return (
        "gh",
        [
            "issue",
            "create",
            "--repo",
            repo,
            "--title",
            title,
            "--body",
            body,
            "--milestone",
            milestone,
            "--project",
            project,
        ],
    )


async def run(program: str, args: list[str]) -> tuple[str, str]:
    """Run a subprocess"""
    print(program, *args)
    proc = await create_subprocess_exec(program, *args, stdout=PIPE, stderr=PIPE)
    stdout, stderr = await proc.communicate()
    await proc.wait()

    return stdout.decode(), stderr.decode()


if __name__ == "__main__":
    asyncio.run(main())
