condition_mapper = {
    "event": {
        "condition": "eventPropertyCondition",
        "fields": {  # allowed fields
            'id': "itemId",
            'scope': "scope",
            'type': 'eventType',
            'timestamp': 'timeStamp',
            'profile.id': "profileId",
            'session.id': "sessionId",
            'source.id': "source.itemId",
            'target.id': "target.itemId",
            'source.scope': "source.scope",
            'target.scope': "target.scope",
            'source.type': "source.itemType",
            'target.type': "target.itemType",
            'target.profile.id': "target.profile.itemType",
        },
        "namespaces": {  # allowed fields namespace
            'properties': "properties",
            'source': "source",
            'source.properties': "source.properties",
            'target': "target",
            'profile': 'profile',
            'target.properties': "target.properties",
            'target.profile.properties': "target.profile.properties",
            'target.profile': "target.profile"
        },
    },
    "profile": {
        "condition": "profilePropertyCondition",
        "fields": {
            'id': "itemId",
            'timestamp': 'systemProperties.lastUpdated',
            'visits': 'properties.nbOfVisits'
        },
        "namespaces": {
            'properties': "properties",
            'segments': "segments",
            'scores': "scores",
        },
    },
    "session": {
        "condition": "sessionPropertyCondition",
        "fields": {
            "duration": 'duration',
            'id': "itemId",
            'scope': "scope",
            'timestamp': 'timeStamp',
            'profile.id': "profileId",
            'profile.type': "profile.itemType",
            'profile.timestamp': "profile.systemProperties.lastUpdated",
        },
        "namespaces": {
            'properties': "properties",
            'profile.properties': "profile.properties",
            'profile.segments': "profile.segments",
            'profile.scores': "profile.scores",
        }
    },
    "rule": {
        "condition": 'eventPropertyCondition',
        "fields": {  # allowed fields

            # Event
            'id': "itemId",
            'event.id': "itemId",
            'scope': "metadata.scope",
            'event.scope': "metadata.scope",
            'type': 'eventType',
            'event.type': 'eventType',
            'timestamp': 'timeStamp',
            'event.timestamp': 'timeStamp',

            # Profile
            'profile.id': "profileId",

            # Session
            'session.id': "sessionId",

            # Source
            'source.id': "source.itemId",
            'source.scope': "source.scope",
            'source.type': "source.itemType",

            # Trager
            'target.id': "target.itemId",
            'target.scope': "target.scope",
            'target.type': "target.itemType",
            'target.profile.id': "target.profile.itemType",

            # Original
            'eventType': 'eventType',
            'sessionId': "sessionId",
            'profileId': "profileId",
            'timeStamp': 'timeStamp',
            'source.itemType': "source.itemType",
            'target.itemType': "target.itemType",
            'target.profile.itemType': "target.profile.itemType",
            'version': 'version',
            'priority': 'priority'
        },
        "namespaces": {
            'properties': "properties",
            'segments': "segments",
            'scores': "scores",
            "metadata": "metadata"
        }
    },
    "segment": {
        "condition": 'profilePropertyCondition',
        "fields": {  # allowed fields

            # Segment
            'id': "itemId",
            'segment.id': "itemId",

            # Profile
            'profile.properties': "properties",

            # Original
            'itemType': 'itemType',
        },
        "namespaces": {
            'properties': "properties",
            'segments': "segments",
            'scores': "scores",
        }
    }
}
