action_mapper = {
    "allEventToProfilePropertiesAction": lambda params: {
        "type": "allEventToProfilePropertiesAction",
        "parameterValues": {}
    },
    "setPropertyAction": lambda params: {
      "type": "setPropertyAction",
      "parameterValues": {
        "setPropertyName": "properties({})".format(params[0][1]),
        "setPropertyValue": "eventProperty::properties({})".format(params[0][1]),
        "setPropertyStrategy": params[1][1]
      }
    }
}
