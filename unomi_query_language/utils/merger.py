def list_of_dict_deep_update(list_of_dicts):
    merged = {}
    for dict_item in list_of_dicts:
        merged = dict_deep_update(merged, dict_item)
    return merged


def dict_deep_update(original, update):
    """
    Recursively update a dict.
    Subdict's won't be overwritten but also updated.
    """
    for key, value in original.items():
        if key not in update:
            update[key] = value
        elif isinstance(value, dict):
            dict_deep_update(value, update[key])
    return update
