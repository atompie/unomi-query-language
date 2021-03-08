uri_mapper = {
    ('select', 'event'): ('cxs/events/search', 'POST'),
    ('select', 'profile'): ('cxs/profiles/search/', 'POST'),
    ('select', 'rule'): ('cxs/rules/query/', 'POST'),
    ('select', 'goal'): ('cxs/goals/query/', 'POST'),
    ('select', 'session'): ('cxs/profiles/search/sessions/', 'POST')
}