from app.query.mappers.uri_mapper import uri_mapper
from app.query.template import nested_condition
from app.query.transformers.condition_transformer import ConditionTransformer


class CreateTransformer(ConditionTransformer):

    def __init__(self):
        super().__init__()

    def create(self, args):

        elements = {k: v for k, v in args}

        query_data_type = elements['DATA_TYPE'] if 'DATA_TYPE' in elements else None
        value_condition = elements['CONDITION'] if 'CONDITION' in elements else None
        bool_condition = elements['BOOLEAN-CONDITION'] if 'BOOLEAN-CONDITION' in elements else None
        condition = [('BOOLEAN-CONDITION', bool_condition), ('CONDITION', value_condition)]

        # key = ('create', query_data_type)
        # if key in uri_mapper:
        #     uri, method = uri_mapper[key]
        # else:
        #     raise ValueError("Unknown {} {} syntax.".format(key[0], key[1]))

        query = {

        }

        condition = nested_condition(condition, query_data_type)
        if condition:
            query['condition'] = condition

        return query
        # return uri, method, query

    def when(self, args):
        return args[0]

    def data_type(self, args):
        return 'DATA_TYPE', args[0].value.lower()

    def create_name(self, args):
        return 'NAME', str(args[0]['value']['value'])

