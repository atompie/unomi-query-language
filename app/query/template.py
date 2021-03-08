def property_template(args, unomi_condition_type):

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
