import re

def diff_stats(diff):

    insertions = 0
    deletions = 0

    for line in diff.splitlines():

        if line.startswith("+++") or line.startswith("---"):
            continue

        if line.startswith("+"):
            insertions += 1

        elif line.startswith("-"):
            deletions += 1

    files_changed = len(
        re.findall(
            r"diff --git",
            diff
        )
    )

    return {
        "files_changed": files_changed,
        "insertions": insertions,
        "deletions": deletions
    }