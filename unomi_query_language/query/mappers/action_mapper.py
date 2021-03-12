from unomi_query_language.query.statement_templates.action_stmt_template import copy_events_to_profile_properties_stmt, \
    set_profile_property_from_event_stmt, increment_profile_property_stmt, event_to_profile_property_stmt, \
    new_user_since

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
                           "This function requires 3 parameters na event property name, profile property name and " +
                           "type of assignment (default is equals).",
            "signature": "setProfilePropertyFromEvent(eventPropertyName, profilePropertyName [, op=\"equals\"])"
        },
        "exec": set_profile_property_from_event_stmt
    },
    "EventToProfileProperty": {
        "metadata": {

        },
        'exec': event_to_profile_property_stmt
    },
    "NewUserSince": {
        "metadata": {
            "signature": "NewUserSince(numberOfDays)"
        },
        'exec': new_user_since
    }

}
