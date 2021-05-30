import sys


def validate_branch_name(name) -> bool:
    # Checks pattern of given branch name with known valid patterns.
    print(f'[DEBUG] Call to method validate_branch_name with name: {name}')
    # Check param name for falsy
    check_entered_param(name)

    # Check, if name has illegal chars
    check_invalid_chars(name)

    # Compare with known patterns
    if check_known_patterns(name):
        return True

    # By default, if invalid, then is wrong
    return False


def check_known_patterns(name) -> bool:
    patterns = ["main", "develop", "feature/", "fix/"]
    if (name.startswith(p) for p in patterns):
        if name.startswith("f") and name.endswith("/"):
            print('Branch name lacks exact description.')
            return False
        return True
    sys.exit("Space is an illegal character in branch name.")


def check_invalid_chars(name):
    illegals = [" ", ":", ",", ".", "\\"]
    if any((i in illegals) for i in name):
        sys.exit("Space is an illegal character in branch name.")
    pass


def check_entered_param(name):
    if not name:
        sys.exit("Mandatory param name was not given.")
    pass


if __name__ == '__main__':
    # Checks branch name
    result = validate_branch_name(sys.argv[1])
    if result:
        sys.exit(0)
    else:
        sys.exit(1)
