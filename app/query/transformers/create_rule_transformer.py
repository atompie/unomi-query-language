from app.query.mappers.action_mapper import action_mapper
from app.query.mappers.uri_mapper import uri_mapper
from app.query.template import nested_condition
from app.query.transformers.condition_transformer import ConditionTransformer


class CreateRuleTransformer(ConditionTransformer):

    def __init__(self):
        super().__init__()

    def create_rule(self, args):

        def get_function_meat(elements):
            _, function = elements
            function_elements = {k: v for k, v in function}

            function_name = function_elements['FUNCTION_NAME'] if 'FUNCTION_NAME' in function_elements else None
            function_params = function_elements['PARAMS'] if 'PARAMS' in function_elements else None

            return function_name, function_params

        elements = {k: v for k, v in args}

        name = elements['NAME'] if 'NAME' in elements else None
        rule_id = name.lower().replace(" ","-").replace("_",'-')
        read_only = elements['READ_ONLY'] if 'READ_ONLY' in elements else False
        hidden = elements['HIDDEN'] if 'HIDDEN' in elements else False
        disabled = elements['DISABLED'] if 'DISABLED' in elements else True
        describe = elements['DESCRIBE'] if 'DESCRIBE' in elements else ""
        query_data_type = elements['DATA_TYPE'] if 'DATA_TYPE' in elements else None
        scope = elements['IN_SCOPE'] if 'IN_SCOPE' in elements else None
        when_condition = elements['WHEN'] if 'WHEN' in elements else None
        when_condition = {k: v for k, v in [when_condition]}
        when_field_condition = when_condition['CONDITION'] if 'CONDITION' in when_condition else None
        when_bool_condition = when_condition['BOOLEAN-CONDITION'] if 'BOOLEAN-CONDITION' in when_condition else None
        condition = [('BOOLEAN-CONDITION', when_bool_condition), ('CONDITION', when_field_condition)]

        key = ('create', query_data_type)
        if key not in uri_mapper:
            raise ValueError("Unknown {} {} syntax.".format(key[0], key[1]))

        uri, method, status = uri_mapper[key]

        query = {
            "itemId": rule_id,
            "itemType": "rule",
            "raiseEventOnlyOnceForProfile": False,
            "raiseEventOnlyOnceForSession": False,
            "priority": -1,
            "metadata": {
                "id": rule_id,
                "name": name,
                "description": describe,
                "scope": scope,
                "tags": [],
                "enabled": disabled,
                "missingPlugins": False,
                "hidden": hidden,
                "readOnly": read_only
            },
            "actions": []
        }

        condition = nested_condition(condition, query_data_type)
        if condition:
            query['condition'] = condition

        then = elements['THEN'] if 'THEN' in elements else None
        for function_elements in then[1]:
            function_name, function_params = get_function_meat(function_elements)

            if function_name in action_mapper:
                query['actions'].append(action_mapper[function_name])

        return uri, method, query, status

    def when(self, args):
        return 'WHEN', args[0]

    def then(self, args):
        return 'THEN', args[0]

    def data_type(self, args):
        return 'DATA_TYPE', args[0].value.lower()

    def rule_name(self, args):
        return 'NAME', str(args[0].value).strip("\"")

    def in_scope(self, args):
        return 'IN_SCOPE', str(args[0].value).strip("\"")

    def rule_describe(self, args):
        return 'DESCRIBE', str(args[0].value).strip("\"")

    def READ_ONLY(self, args):
        return 'READ_ONLY', True

    def DISABLED(self, args):
        return 'DISABLED', False

    def HIDDEN(self, args):
        return 'HIDDEN', True

    def functions(self, args):
        return 'FUNCTIONS', args

    def function(self, args):
        return 'FUNCTION', args

    def function_name(self, args):
        return 'FUNCTION_NAME', args[0].value

    def params(self, args):
        return 'PARAMS', args

    def param(self, args):
        return args[0].type, args[0].value
