from unomi_query_language.errors import ActionParamsError, ActionParamError


def copy_events_to_profile_properties_stmt(params):
    return {
        "type": "allEventToProfilePropertiesAction",
        "parameterValues": {},

    }


# TODO not working
def increment_profile_property_stmt(params):
    profile_value_type, profile_property_name = params[0]

    if profile_value_type != "ESCAPED_STRING":
        raise ActionParamError(
            "First param of action IncrementProfileProperty must be string. Type of `{}` given.".format(
                profile_value_type))

    return {
        "type": "incrementInterestAction",
        "parameterValues": {
            "eventInterestProperty": profile_property_name
        }
    }


def new_user_since(params):
    since_value_type, since_property_value = params[0]

    if since_value_type != "NUMBER":
        raise ActionParamError(
            "First param of action NewUserSince must be string. Type of `{}` given.".format(
                since_value_type))

    return {
        "type": "newVisitorCondition",
        "parameterValues": {
            "since": since_property_value
        }
    }


def set_profile_property_from_event_stmt(params):
    if 3 < len(params) or len(params) < 2:
        raise ActionParamsError(
            "Invalid number of parameters in action SetProfilePropertyFromEvent. Required parameters 2 or 3. Given {}".format(
                len(params)))

    if len(params) == 2:
        params.append(('ESCAPED_STRING', 'alwaysSet'))

    event_value_type, event_property_name = params[0]
    profile_value_type, profile_property_name = params[1]
    op_value_type, op_property_name = params[2]

    if profile_value_type != "ESCAPED_STRING":
        raise ActionParamError(
            "First param of action SetProfilePropertyFromEvent must be string. Type of `{}` given.".format(
                profile_value_type))

    if event_value_type == "ESCAPED_STRING":
        raise ActionParamError(
            "Second param of action SetProfilePropertyFromEvent must be string. Type of `{}` given.".format(
                event_value_type))

    if op_value_type != "ESCAPED_STRING":
        raise ActionParamError(
            "Third param of action SetProfilePropertyFromEvent must be string. Type of `{}` given.".format(
                op_value_type))

    return {
        "type": "setPropertyAction",
        "parameterValues": {
            "setPropertyName": "properties({})".format(profile_property_name),
            "setPropertyValue": "eventProperty::properties({})".format(event_property_name),
            "setPropertyStrategy": op_property_name
        }
    }


def set_profile_property_stmt(params):
    if 3 < len(params) or len(params) < 2:
        raise ActionParamsError(
            "Invalid number of parameters in action SetProfilePropertyValue. Required parameters 2 or 3. Given {}".format(
                len(params)))

    if len(params) == 2:
        params.append(('ESCAPED_STRING', 'alwaysSet'))

    profile_property_name_type, profile_property_name = params[0]
    property_value_type, property_value = params[1]
    op_value_type, op_property_name = params[2]

    if profile_property_name_type != "ESCAPED_STRING":
        raise ActionParamError(
            "First param of action SetProfilePropertyValue must be string. Type of `{}` given.".format(
                profile_property_name_type))

    if property_value_type == "ESCAPED_STRING":
        set_property_value = "setPropertyValue"
    elif property_value_type == "NUMBER":
        set_property_value = "setPropertyValueInteger"
    elif property_value_type == "array":
        set_property_value = "setPropertyValueMultiple"
    elif property_value_type == "BOOL":
        set_property_value = "setPropertyValueBoolean"
    else:
        raise ActionParamError(
            "Second param of action SetProfilePropertyValue must be string or number or array or bool. Type of `{}` given.".format(
                property_value_type))

    if op_value_type != "ESCAPED_STRING":
        raise ActionParamError(
            "Third param of action SetProfilePropertyValue must be string. Type of `{}` given.".format(
                op_value_type))

    return {
        "type": "setPropertyAction",
        "parameterValues": {
            "setPropertyName": "properties({})".format(profile_property_name),
            set_property_value: property_value,
            "setPropertyStrategy": op_property_name
        }
    }


def profile_property_equals_event_property_stmt(params):
    if len(params) != 2:
        raise ActionParamsError(
            "Invalid number of parameters in action ProfilePropertyEqualsEventProperty. Required parameters 2. Given {}".format(
                len(params)))

    profile_value_type, profile_property_name = params[0]
    event_value_type, event_property_name = params[1]

    if profile_value_type != "ESCAPED_STRING":
        raise ActionParamError(
            "First param of action ProfilePropertyEqualsEventProperty must be string. Type of `{}` given.".format(
                profile_value_type))

    if event_value_type != "ESCAPED_STRING":
        raise ActionParamError(
            "Second param of action ProfilePropertyEqualsEventProperty must be string. Type of `{}` given.".format(
                event_value_type))

    return {
        "type": "eventToProfilePropertyAction",
        "parameterValues": {
            "eventPropertyName": event_property_name,
            "profilePropertyName": profile_property_name,
        }
    }
