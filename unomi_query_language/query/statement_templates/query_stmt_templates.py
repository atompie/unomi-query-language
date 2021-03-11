from unomi_query_language.query.mappers.controllers.action_controller import action_controller
from unomi_query_language.query.statement_templates.condition_stmt_template import nested_condition_stmt
from unomi_query_language.query.transformers.utils.meta_fields import MetaFields


def metadata_stmt(elements):
    meta = MetaFields(elements)
    name = meta.get_name()
    segment_id = name.lower().replace(" ", "-").replace("_", '-')
    describe = meta.get_descride()
    hidden = meta.get_hidden()
    disabled = meta.get_disabled()
    read_only = meta.get_read_only()
    tags = meta.get_tags()
    scope = meta.get_in_scope()

    return {
        "metadata": {
            "id": segment_id,
            "name": name,
            "description": describe,
            "scope": scope,
            "tags": tags,
            "enabled": disabled,
            "missingPlugins": False,
            "hidden": hidden,
            "readOnly": read_only
        }
    }


def select_stmt(elements, condition):
    fresh = elements['FRESH'] if 'FRESH' in elements else False
    offset = elements['OFFSET'] if 'OFFSET' in elements else 0
    limit = elements['LIMIT'] if 'LIMIT' in elements else 20

    body = {
        "offset": offset,
        "limit": limit,
        "forceRefresh": fresh,
    }

    if condition:
        body['condition'] = condition

    return body


def create_segment_stmt(elements, condition):
    meta = metadata_stmt(elements)
    body = {
        "itemId": meta['metadata']['id'],
        "itemType": "segment",
        "metadata": metadata_stmt(elements)
    }
    if condition:
        body['condition'] = condition

    return body


def create_rule_stmt(elements, condition, actions):
    meta = metadata_stmt(elements)
    body = {
        "itemId": meta['metadata']['id'],
        "itemType": "rule",
        "raiseEventOnlyOnceForProfile": False,
        "raiseEventOnlyOnceForSession": False,
        "priority": -1,
        "metadata": metadata_stmt(elements),
        "actions": actions
    }
    if condition:
        body['condition'] = condition

    return body


def create_condition_stmt(condition, query_data_type):
    condition = {k: v for k, v in [condition]}
    field_condition = condition['CONDITION'] if 'CONDITION' in condition else None
    bool_condition = condition['BOOLEAN-CONDITION'] if 'BOOLEAN-CONDITION' in condition else None

    condition = [('BOOLEAN-CONDITION', bool_condition), ('CONDITION', field_condition)]
    return nested_condition_stmt(condition, query_data_type)


def create_action_stmt(actions):
    def get_function_meta(elements):
        function_elements = {k: v for k, v in elements}

        function_name = function_elements['FUNCTION_NAME'] if 'FUNCTION_NAME' in function_elements else None
        function_params = function_elements['PARAMS'] if 'PARAMS' in function_elements else None

        return function_name, function_params

    _actions = []
    for function_elements in actions[1]:
        function_name, function_params = get_function_meta(function_elements)
        template = action_controller.run(function_name)(function_params)
        _actions.append(template)
    return _actions
