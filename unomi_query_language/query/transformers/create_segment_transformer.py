from unomi_query_language.query.mappers.uri_mapper import uri_mapper
from unomi_query_language.query.template import nested_condition
from unomi_query_language.query.transformers.condition_transformer import ConditionTransformer
from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class CreateSegmentTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace('uql_expr__', ConditionTransformer())

    def create_segment(self, args):

        elements = {k: v for k, v in args}

        name = elements['NAME'] if 'NAME' in elements else None
        segment_id = name.lower().replace(" ","-").replace("_",'-')
        query_data_type = elements['DATA_TYPE'] if 'DATA_TYPE' in elements else None
        when_condition = elements['WHEN'] if 'WHEN' in elements else None
        scope = elements['IN_SCOPE'] if 'IN_SCOPE' in elements else None

        when_condition = {k: v for k, v in [when_condition]}

        when_field_condition = when_condition['CONDITION'] if 'CONDITION' in when_condition else None
        when_bool_condition = when_condition['BOOLEAN-CONDITION'] if 'BOOLEAN-CONDITION' in when_condition else None

        condition = [('BOOLEAN-CONDITION', when_bool_condition), ('CONDITION', when_field_condition)]

        key = ('create', query_data_type)
        if key not in uri_mapper:
            raise ValueError("Unknown {} {} syntax.".format(key[0], key[1]))

        uri, method, status = uri_mapper[key]

        query = {
            "itemId": segment_id,
            "itemType": "segment",
            "metadata": {
                "id": segment_id,
                "name": name,
                "scope": scope
            }
        }

        condition = nested_condition(condition, query_data_type)
        if condition:
            query['condition'] = condition

        return uri, method, query, status

    def when(self, args):
        return 'WHEN', args[0]

    def then(self, args):
        return 'THEN', args[0]

    def data_type(self, args):
        return 'DATA_TYPE', args[0].value.lower()

    def create_name(self, args):
        return 'NAME', str(args[0].value).strip("\"")

    def in_scope(self, args):
        return 'IN_SCOPE', str(args[0].value).strip("\"")

