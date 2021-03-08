from app.query.template import property_template


condition_type_mapper = {
    "event": {
        "condition": "eventPropertyCondition",
        "template": property_template
    },
    "profile": {
        "condition": "profilePropertyCondition",
        "template": property_template
    },
    "session": {
        "condition": "sessionPropertyCondition",
        "template": property_template
    }
}