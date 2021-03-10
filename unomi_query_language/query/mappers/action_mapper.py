from unomi_query_language.query.actions.copy_event_properties_to_profile import set_profile_property_from_event, \
    copy_events_to_profile_properties

action_mapper = {
    "copyEventsToProfileProperties": {
        "metadata": {
            "description": "Copy all properties from event to profile properties.",
            "signature": "copyEventsToProfileProperties()"
        },
        "exec": copy_events_to_profile_properties
    },
    "setProfilePropertyFromEvent": {
        "metadata": {
            "description": "Copy selected property from event to profile property. " +
                           "This function requires 3 parameters na event property name, profile property name and " +
                           "type of assignment (default is equals).",
            "signature": "setProfilePropertyFromEvent(eventPropertyName, profilePropertyName [, op=\"equals\"])"
        },
        "exec": set_profile_property_from_event
    }
}
