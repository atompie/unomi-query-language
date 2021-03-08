field_mapper = {
    ('event', 'id'): "itemId",
    ('event', 'scope'): "scope",
    ('event', 'type'): 'eventType',
    ('event', 'timestamp'): 'timeStamp',
    ('event', 'profile.id'): "profileId",
    ('event', 'session.id'): "sessionId",
    ('event', 'source.id'): "source.itemId",
    ('event', 'target.id'): "target.itemId",
    ('event', 'source.scope'): "source.scope",
    ('event', 'target.scope'): "target.scope",
    ('event', 'source.type'): "source.itemType",
    ('event', 'target.type'): "target.itemType",

    ('profile', 'id'): "itemId",
    ('profile', 'timestamp'): 'systemProperties.lastUpdated',

    ('session', 'id'): "itemId",
    ('session', 'scope'): "scope",
    ('session', 'timestamp'): 'timeStamp',
    ('session', 'profile.id'): "profileId",
    ('session', 'profile.type'): "profile.itemType",
    ('session', 'profile.timestamp'): "profile.systemProperties.lastUpdated",
}

field_group_mapper = {
    ('event', 'properties'): "properties",
    ('event', 'source.properties'): "source.properties",
    ('event', 'target.properties'): "target.properties",

    ('profile', 'properties'): "properties",
    ('profile', 'segments'): "segments",
    ('profile', 'scores'): "scores",

    ('session', 'properties'): "properties",
    ('session', 'profile.properties'): "profile.properties",
    ('session', 'profile.segments'): "profile.segments",
    ('session', 'profile.scores'): "profile.scores",
}
