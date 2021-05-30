import sys


def validate_branch_name(name) -> bool:
    # Checks pattern of given branch name with known valid patterns.
    print(f'[DEBUG] Call to method validate_branch_name with name: {name}')
    # Check param name for falsy
    check_entered_param(name)

    # TODO Check, if name has wrong chars

    # TODO COMPARE with known patterns

    # By default, if invalid, then is wrong
    return False


def check_entered_param(name):
    if not name:
        sys.exit("Mandatory param name was not given.")
    pass


if __name__ == '__main__':
    # if sys.argv[1] and sys.argv[1] in []:
    #    sys.exit("Param:")
    # Checks branch name
    result = validate_branch_name(sys.argv[1])
    if result:
        sys.exit(0)
    else:
        sys.exit(1)
