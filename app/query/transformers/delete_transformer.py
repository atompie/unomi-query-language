from app.query.mappers.uri_mapper import uri_mapper
from app.query.transformers.condition_transformer import ConditionTransformer


class DeleteTransformer(ConditionTransformer):

    def __init__(self):
        super().__init__()

    def delete(self, args):
        elements = {k: v for k, v in args}

        name = elements['NAME'] if 'NAME' in elements else None
        query_data_type = elements['DATA_TYPE'] if 'DATA_TYPE' in elements else None

        key = ('delete', query_data_type)
        if key not in uri_mapper:
            raise ValueError("Unknown {} {} syntax.".format(key[0], key[1]))

        uri, method, status = uri_mapper[key]
        uri = uri.replace('{item-id}', name)

        query = {}

        return uri, method, query, status

    def data_type(self, args):
        return 'DATA_TYPE', args[0].value.lower()

    def create_name(self, args):
        return 'NAME', str(args[0].value).strip("\"")
