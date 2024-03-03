import sys
import re
from typing import Union
from subprocess import check_output


def getJiraPrefix(branch: str) -> Union[str, None]:
    prefix: Union[str, None] = None

    regex = r"^.*?\/([A-Z]*?-[0-9]{1,})(-)?.*$"
    results = re.match(regex, branch)
    if results:
        prefix = results.group(1)
    return prefix


def main():

    branch: str = (
        check_output(["git", "symbolic-ref", "--short", "HEAD"]
                     ).decode("utf-8").strip()
    )

    prefix = getJiraPrefix(branch)

    print(branch, prefix)

    if prefix is not None:
        commitMsgFilepath = sys.argv[1]

        with open(commitMsgFilepath) as file:
            message = file.read()

        if message.find(prefix) == -1:
            with open(commitMsgFilepath, 'r') as original:
                data = original.read()
            with open(commitMsgFilepath, 'w') as modified:
                modified.write(prefix + ': ' + data)


if __name__ == "__main__":
    main()
