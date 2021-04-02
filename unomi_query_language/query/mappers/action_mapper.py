from unomi_query_language.query.statement_templates.action_stmt_template import copy_events_to_profile_properties_stmt, \
    set_profile_property_from_event_stmt, profile_property_equals_event_property_stmt, \
    new_user_since, set_profile_property_stmt, _add_to_profile_property_list_stmt, add_to_profile_property_stmt, \
    remove_from_profile_property_stmt

action_mapper = {
    "CopyEventsToProfileProperties": {
        "metadata": {
            "description": "Copy all properties from event to profile properties.",
            "signature": "copyEventsToProfileProperties()"
        },
        "exec": copy_events_to_profile_properties_stmt
    },
    "SetProfilePropertyFromEvent": {
        "metadata": {
            "description": "Copy selected property from event to profile property. " +
                           "This function requires 3 parameters an event property name, profile property name and " +
                           "type of assignment (default is equals).",
            "signature": "setProfilePropertyFromEvent(eventPropertyName, profilePropertyName [, op=\"equals\"])"
        },
        "exec": set_profile_property_from_event_stmt
    },
    # This one works
    "SetProfilePropertyValue": {
        "metadata": {
            "description": "Sets profile property to given value of type string, int, bool, list. " +
                           "This function requires 3 parameters a profile property name, event property name and " +
                           "type of assignment (default is equals).",
            "signature": "SetProfilePropertyValue(profilePropertyName:string, eventPropertyName:any, [, op=\"equals\"])"
        },
        "exec": set_profile_property_stmt
    },
    # This one works
    "AddToProfileListProperty": {
        "metadata": {
            "description": "Add value to profile property. Property must be array and be of the same type as value. " +
                           "This function requires 2 parameters a profile property name and property value to add.",
            "signature": "AddToProfileProperty(profilePropertyName:string, propertyToAdd:any)"
        },
        "exec": add_to_profile_property_stmt
    },
    # This one not working
    "RemoveFromProfileProperty": {
        "metadata": {
            "description": "Removes value from profile property. Property must be array and be of the same type as value. " +
                           "This function requires 2 parameters a profile property name and property value to remove.",
            "signature": "RemoveFromProfileProperty(profilePropertyName:string, propertyToRemove:any)"
        },
        "exec": remove_from_profile_property_stmt
    },
    "ProfilePropertyEqualsEventProperty": {
        "metadata": {
            "description": "Copy property from event to profile property. " +
                           "This function requires 2 parameters an profile property name, event property name.",
            "signature": "ProfilePropertyEqualsEventProperty(profilePropertyName:string, eventPropertyName:string)"
        },
        'exec': profile_property_equals_event_property_stmt
    },
    "NewUserSince": {
        "metadata": {
            "signature": "NewUserSince(numberOfDays:number)"
        },
        'exec': new_user_since
    },
    # This one not working
    "_AddToProfilePropertyList": {
        "metadata": {
            "signature": "AddToProfilePropertyList(listIdentifiers:array)"
        },
        'exec': _add_to_profile_property_list_stmt
    }

}
