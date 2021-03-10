from unomi_query_language.query.mappers.operation_mapper import operation_mapper
from unomi_query_language.query.transformers.value_transformer import ValueTransformer


class ConditionTransformer(ValueTransformer):

    def __init__(self):
        super().__init__()
        self._cmp = operation_mapper

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

    def between(self, args):
        return self.condition(args)

    def condition(self, args):

        args = {
            'field': args[0]['field'],
            'op': args[1]['op'],
            'values': args[2] if len(args) > 2 else None,
        }

        return 'CONDITION', args

    def exists(self, args):

        args.append({'op': {
            'token': 'exists',
            'unomi-op': self._cmp['exists'],
        }})

        return self.condition(args)

    def not_exists(self, args):

        args.append({'op': {
            'token': 'exists',
            'unomi-op': self._cmp['not exists'],
        }})

        return self.condition(args)

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
