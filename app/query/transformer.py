from lark import Transformer, Token

from app.query.mappers.field_mapper import field_mapper
from app.query.mappers.operation_mapper import operation_mapper
from app.query.mappers.uri_mapper import uri_mapper
from app.query.template import property_template, nested_condition

from app.utils.merger import list_of_dict_deep_update


class SelectTransformer(Transformer):

    def __init__(self):
        super().__init__()
        self._cmp = operation_mapper

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
            uri, method = uri_mapper[key]
        else:
            raise ValueError("Unknown {} {} syntax.".format(key[0], key[1]))

        query = {
            "offset": offset,
            "limit": limit,
            "forceRefresh": fresh,
            "condition": nested_condition(condition, query_data_type)
        }

        return uri, method, query

    def where(self, args):
        return args[0]

    def DATA_TYPE(self, args):
        return 'DATA_TYPE', args.value.lower()

    def FRESH(self, args):
        return 'FRESH', args.value.lower()

    def limit(self, args):
        return 'LIMIT', int(args[0]['value']['value'])

    def offset(self, args):
        return 'OFFSET', int(args[0]['value']['value'])

    def is_null(self, args):

        args = [
            args[0],
            {
                'op': {
                    'token': None,
                    'unomi-op': self._cmp['is null'],
                }
            },
            {
                'value': {
                    'token': None,
                    'type': 'null',
                    "unomi-type": 'propertyValue',
                    'value': 'null'
                }
            }
        ]

        return self.condition(args)

    def and_expr(self, args):
        return "BOOLEAN-CONDITION", {
            "bool": "and",
            "subConditions": args
        }

    def or_expr(self, args):
        return "BOOLEAN-CONDITION", {
            "bool": "or",
            "subConditions": args
        }

    def CHUNK(self, args):
        return args[:-1]

    def between(self, args):
        return self.condition(args)

    def condition(self, args):

        args = {
            'field': args[0]['field'],
            'op': args[1]['op'],
            'values': args[2] if len(args) > 2 else None,
        }

        return 'CONDITION', args

    def value(self, args):
        token = args[0]  # type: Token
        if isinstance(token, Token):
            return token.value
        else:
            return token

    def SIGNED_NUMBER(self, args):
        return {
            'value': {
                'token': args,
                'type': 'signed-number',
                "unomi-type": 'propertyValueInteger',
                'value': int(args.value)
            }
        }

    def NUMBER(self, args):
        return {
            'value': {
                'token': args,
                'type': 'number',
                "unomi-type": 'propertyValueInteger',
                'value': float(args.value)
            }
        }

    def string(self, args):
        return {
            'value': {
                'token': args,
                'type': 'string',
                "unomi-type": 'propertyValue',
                'value': str(args)
            }
        }

    def exists(self, args):

        args.append({'op': {
            'token': 'exists',
            'unomi-op': self._cmp['not exists'],
        }})

        return self.condition(args)

    def not_exists(self, args):

        args.append({'op': {
            'token': 'exists',
            'unomi-op': self._cmp['not exists'],
        }})

        return self.condition(args)

    def ESCAPED_STRING(self, args):
        string = str(args.value.strip('"'))
        string = string.replace('(', "\"")

        return {
            'value': {
                'token': args,
                'unomi-type': "propertyValue",
                'type': 'string',
                'value': string.replace(")", "\"")
            }

        }

    def array(self, args):
        values = [v for t, v in args]
        return {
            'value': {
                'token': args,
                "unomi-type": "propertyValues",
                'type': 'array',
                'value': values
            }
        }

    def range(self, args):
        values = [v['value']['value'] for v in args]
        return {
            'value': {
                'token': args,
                "unomi-type": "propertyValuesInteger",
                'type': 'range',
                'value': values
            }
        }

    def NULL(self, args):
        return {
            'value': {
                'token': args,
                "unomi-type": "propertyValue",
                'type': 'null',
                'value': None
            }
        }

    def FIELD(self, args):

        if ':' in args:
            splited_args = args.split(":")
            type = splited_args[0]
            field = splited_args[1]
            return {
                'field': {
                    'token': args,
                    'unomi-type': type,
                    'field': field
                }
            }
        else:
            return {
                'field': {
                    'token': args,
                    'field': args.value
                }
            }

    def OP(self, args):
        return {
            'op': {
                'token': args,
                'unomi-op': self._cmp[str(args)],
            }
        }
