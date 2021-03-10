from unomi_query_language.query.mappers.operation_mapper import operation_mapper
from unomi_query_language.query.transformers.value_transformer import ValueTransformer


class ConditionTransformer(ValueTransformer):

    def __init__(self):
        super().__init__()
        self._cmp = operation_mapper

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

    def OP_FIELD(self, args):

        if ':' in args:
            splited_args = args.split(":")
            type = splited_args[0]
            field = splited_args[1]
            return {
                'field': {
                    'unomi-type': type,
                    'field': field
                }
            }
        else:
            return {
                'field': {
                    'field': args.value
                }
            }

    def op_condition(self, args):

        args = {
            'field': args[0]['field'],
            'op': args[1]['op'],
            'values': args[2] if len(args) > 2 else None,
        }

        return 'CONDITION', args

    def op_between(self, args):

        args[1] = {
            'op': {
                'unomi-op': self._cmp['between'],
            }
        }

        return self.op_condition(args)

    def op_exists(self, args):

        args.append({'op': {
            'unomi-op': self._cmp['exists'],
        }})

        return self.op_condition(args)

    def op_not_exists(self, args):

        args.append({'op': {
            'unomi-op': self._cmp['not exists'],
        }})

        return self.op_condition(args)

    def op_is_null(self, args):

        args = [
            args[0],
            {
                'op': {
                    'unomi-op': self._cmp['is null'],
                }
            },
            {
                'value': {
                    'type': 'null',
                    "unomi-type": 'propertyValue',
                    'value': 'null'
                }
            }
        ]

        return self.op_condition(args)

    def OP(self, args):
        return {
            'op': {
                'unomi-op': self._cmp[str(args)],
            }
        }
