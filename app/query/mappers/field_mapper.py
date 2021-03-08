field_mapper = {
    "event": {
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
    "profile": {
        'id': "itemId",
        'timestamp': 'systemProperties.lastUpdated',
    },
    "session": {
        'id': "itemId",
        'scope': "scope",
        'timestamp': 'timeStamp',
        'profile.id': "profileId",
        'profile.type': "profile.itemType",
        'profile.timestamp': "profile.systemProperties.lastUpdated",
    }
}

field_group_mapper = {

    "event": {
        'properties': "properties",
        'source.properties': "source.properties",
        'target.properties': "target.properties",
    },

    "profile": {
        'properties': "properties",
        'segments': "segments",
        'scores': "scores",
    },

    "session": {
        'properties': "properties",
        'profile.properties': "profile.properties",
        'profile.segments': "profile.segments",
        'profile.scores': "profile.scores",
    }
}
