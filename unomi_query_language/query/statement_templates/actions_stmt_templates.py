from lark import Tree
from lark.lexer import Token

from unomi_query_language.query.mappers.controllers.action_controller import action_controller


def create_actions_group_stmt(actions):
    def get_function_meta(elements):

        if not isinstance(elements, list):
            elements = [elements]

        function_elements = {k: v for k, v in elements}

        function_name = function_elements['FUNCTION_NAME'] if 'FUNCTION_NAME' in function_elements else None
        function_params = function_elements['PARAMS'] if 'PARAMS' in function_elements else None

        return function_name, function_params

    _actions = []

    if isinstance(actions, Tree):
        actions = [actions.children]
    else:
        actions = actions[1]

    for function_elements in actions:
        function_name, function_params = get_function_meta(function_elements)
        template = action_controller.run(function_name)(function_params)
        _actions.append(template)
    return _actions
