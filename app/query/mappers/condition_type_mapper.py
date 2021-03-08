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
        },
        "namespaces": {  # allowed fields namespace
            'properties': "properties",
            'source.properties': "source.properties",
            'target.properties': "target.properties",
        },
    },
    "profile": {
        "condition": "profilePropertyCondition",
        "fields": {
            'id': "itemId",
            'timestamp': 'systemProperties.lastUpdated',
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
    }
}
