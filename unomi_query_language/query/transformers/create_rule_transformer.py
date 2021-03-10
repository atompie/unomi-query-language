from lark import Lark

from unomi_query_language.query.mappers.controllers.action_controller import action_controller
from unomi_query_language.query.mappers.uri_mapper import uri_mapper
from unomi_query_language.query.template import nested_condition
from unomi_query_language.query.transformers.condition_transformer import ConditionTransformer
from unomi_query_language.query.transformers.function_transformer import FunctionTransformer
from unomi_query_language.query.transformers.meta_transformer import MetaTransformer
from unomi_query_language.query.transformers.utils.meta_fields import MetaFields


class CreateRuleTransformer(MetaTransformer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace('uql_expr__', ConditionTransformer())
        self.namespace('uql_function__', FunctionTransformer())

    def create_rule(self, args):

        def get_function_meta(elements):
            function_elements = {k: v for k, v in elements}

            function_name = function_elements['FUNCTION_NAME'] if 'FUNCTION_NAME' in function_elements else None
            function_params = function_elements['PARAMS'] if 'PARAMS' in function_elements else None

            return function_name, function_params

        elements = {k: v for k, v in args}

        meta = MetaFields(elements)
        name = meta.get_name()
        describe = meta.get_descride()
        hidden = meta.get_hidden()
        disabled = meta.get_disabled()
        read_only = meta.get_read_only()
        tags = meta.get_tags()
        scope = meta.get_in_scope()

        rule_id = name.lower().replace(" ", "-").replace("_", '-')
        query_data_type = elements['DATA_TYPE'] if 'DATA_TYPE' in elements else None
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
                "tags": tags,
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
            function_name, function_params = get_function_meta(function_elements)

            template = action_controller.run(function_name)(function_params)
            query['actions'].append(template)

        return uri, method, query, status

    def when(self, args):
        return 'WHEN', args[1]

    def then(self, args):
        return 'THEN', args[1]

    def data_type(self, args):
        return 'DATA_TYPE', args[0].value.lower()

    def functions(self, args):
        return 'FUNCTIONS', [arg.children for arg in args]


