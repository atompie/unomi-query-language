from lark import Token

from unomi_query_language.query.mappers.uri_mapper import uri_mapper
from unomi_query_language.query.template import nested_condition
from unomi_query_language.query.transformers.condition_transformer import ConditionTransformer
from unomi_query_language.query.transformers.transformer_namespace import TransformerNamespace


class SelectTransformer(TransformerNamespace):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.namespace('uql_expr__', ConditionTransformer())

    def select(self, args):

        elements = {k: v for k, v in args}

        query_data_type = elements['DATA_TYPE'] if 'DATA_TYPE' in elements else None
        value_condition = elements['CONDITION'] if 'CONDITION' in elements else None
        bool_condition = elements['BOOLEAN-CONDITION'] if 'BOOLEAN-CONDITION' in elements else None
        condition = [('BOOLEAN-CONDITION', bool_condition), ('CONDITION', value_condition)]
        fresh = elements['FRESH'] if 'FRESH' in elements else False
        offset = elements['OFFSET'] if 'OFFSET' in elements else 0
        limit = elements['LIMIT'] if 'LIMIT' in elements else 20

        key = ('select', query_data_type)
        if key in uri_mapper:
            uri, method, status = uri_mapper[key]
        else:
            raise ValueError("Unknown {} {} syntax.".format(key[0], key[1]))

        query = {
            "offset": offset,
            "limit": limit,
            "forceRefresh": fresh,
        }

        condition = nested_condition(condition, query_data_type)
        if condition:
            query['condition'] = condition

        return uri, method, query, status

    def where(self, args):
        return args[0]

    def data_type(self, args):
        return 'DATA_TYPE', args[0].value.lower()

    def FRESH(self, args):
        return 'FRESH', args.value.lower()

    def limit(self, args):
        return 'LIMIT', int(args[0]['value']['value'])

    def offset(self, args):
        return 'OFFSET', int(args[0]['value']['value'])


