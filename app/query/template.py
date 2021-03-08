from app.query.mappers.condition_type_mapper import condition_type_mapper


def nested_condition(condition_args, query_data_type):
    for type, args in condition_args:
        if type == 'CONDITION' and args:
            return property_template(args, query_data_type)

        if type == 'BOOLEAN-CONDITION' and args:
            return boolean_condition(args, query_data_type)


def boolean_condition(args, query_data_type):
    return {
        "type": "booleanCondition",
        "parameterValues": {
            "operator": args['bool'],
            "subConditions": [nested_condition([sub_args], query_data_type) for sub_args in args['subConditions']]
        }
    }


def property_template(args, query_data_type):

    # znajdz jakiego typu użyc czy z zapytania czy z pola.
    data_type = args['field']['unomi-type'] if 'unomi-type' in args['field'] else query_data_type

    if query_data_type not in condition_type_mapper:
        raise ValueError("Unknown data type {}".format(query_data_type))

    unomi_condition_type = condition_type_mapper[data_type]['condition']

    result = {
        "type": unomi_condition_type,
        "parameterValues": {
            "propertyName": args['field']['field'],
            "comparisonOperator": args['op']['unomi-op']
        }
    }

    if 'values' in args and args['values'] is not None:
        if isinstance(args['values'], dict):
            args = args['values']
            result["parameterValues"][args['value']['unomi-type']] = args['value']['value']
        elif isinstance(args['values'], list):
            for value in args['values']:
                result["parameterValues"][value['value']['unomi-type']] = value['value']['value']
        else:
            raise ValueError("Unknown values type")

    return result
