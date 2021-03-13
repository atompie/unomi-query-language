from unomi_query_language.query.statement_templates.action_stmt_template import copy_events_to_profile_properties_stmt, \
    set_profile_property_from_event_stmt, increment_profile_property_stmt, profile_property_equals_event_property_stmt, \
    new_user_since, set_profile_property_stmt

action_mapper = {
    "CopyEventsToProfileProperties": {
        "metadata": {
            "description": "Copy all properties from event to profile properties.",
            "signature": "copyEventsToProfileProperties()"
        },
        "exec": copy_events_to_profile_properties_stmt
    },
    # "IncrementProfileProperty": {
    #     "metadata": {
    #
    #     },
    #     'exec': increment_profile_property_stmt
    # },
    "SetProfilePropertyFromEvent": {
        "metadata": {
            "description": "Copy selected property from event to profile property. " +
                           "This function requires 3 parameters an event property name, profile property name and " +
                           "type of assignment (default is equals).",
            "signature": "setProfilePropertyFromEvent(eventPropertyName, profilePropertyName [, op=\"equals\"])"
        },
        "exec": set_profile_property_from_event_stmt
    },
    "SetProfilePropertyValue": {
        "metadata": {
            "description": "Sets profile property to given value of type string, int, bool, list. " +
                           "This function requires 3 parameters an profile property name, property value and " +
                           "type of assignment (default is equals).",
            "signature": "SetProfilePropertyValue(profilePropertyName, propertyValue, [, op=\"equals\"])"
        },
        "exec": set_profile_property_stmt
    },
    "ProfilePropertyEqualsEventProperty": {
        "metadata": {
            "description": "Copy property from event to profile property. " +
                           "This function requires 2 parameters an profile property name, event property name.",
            "signature": "ProfilePropertyEqualsEventProperty(profilePropertyName, eventPropertyName)"
        },
        'exec': profile_property_equals_event_property_stmt
    },
    "NewUserSince": {
        "metadata": {
            "signature": "NewUserSince(numberOfDays)"
        },
        'exec': new_user_since
    }

}
