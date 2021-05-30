import sys


def validate_branch_name(name):
    # Checks pattern of given branch name with known valid patterns.
    print(f'[DEBUG] Call to method validate_branch_name with name: {name}')
    # Check param name for falsy
    check_entered_param(name)

    # TODO Check, if name has wrong chars

    # TODO COMPARE with known patterns

    # TODO Return default - false


def check_entered_param(name):
    if not name:
        sys.exit("Mandatory param name was not given.")
    pass


if __name__ == '__main__':
    # Checks branch name
    validate_branch_name(sys.argv[1])
