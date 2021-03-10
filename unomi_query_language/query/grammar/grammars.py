import os

_local_dir = os.path.dirname(__file__)


def condition():
    with open(os.path.join(_local_dir, 'condition.lark')) as f:
        return f.read()


def select():
    _condition_file = condition()

    with open(os.path.join(_local_dir, 'select.lark')) as f:
        file = f.read()

    return file.replace('%condition.lark%', _condition_file)


def create_segment():
    _condition_file = condition()

    with open(os.path.join(_local_dir, 'create_segment.lark')) as f:
        file = f.read()

    return file.replace('%condition.lark%', _condition_file)


def create_rule():
    _condition_file = condition()

    with open(os.path.join(_local_dir, 'create_rule.lark')) as f:
        file = f.read()

    return file.replace('%condition.lark%', _condition_file)


def delete():
    _condition_file = condition()

    with open(os.path.join(_local_dir, 'delete.lark')) as f:
        file = f.read()

    return file.replace('%condition.lark%', _condition_file)
