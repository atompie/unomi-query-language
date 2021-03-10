from unomi_query_language.errors import ActionParamsError


def copy_events_to_profile_properties(params):
    return {
        "type": "allEventToProfilePropertiesAction",
        "parameterValues": {},

    }


def set_profile_property_from_event(params):
    if 3 < len(params) or len(params) < 2:
        raise ActionParamsError(
            "Invalid number of parameters in action setProfilePropertyFromEvent. Required parameters 2 or 3. Given {}".format(
                len(params)))

    if len(params) == 2:
        params.append(('ESCAPED_STRING', 'alwaysSet'))

    profile_value_type, profile_property_name = params[0]
    event_value_type, event_property_name = params[1]
    op_value_type, op_property_name = params[2]

    return {
               "type": "setPropertyAction",
               "parameterValues": {
                   "setPropertyName": "properties({})".format(profile_property_name),
                   "setPropertyValue": "eventProperty::properties({})".format(event_property_name),
                   "setPropertyStrategy": op_property_name
               }
           },
