uri_mapper = {
    ('select', 'event'):    ('cxs/events/search', 'POST', 200),
    ('select', 'profile'):  ('cxs/profiles/search/', 'POST', 200),
    ('select', 'rule'):     ('cxs/rules/query/', 'POST', 200),
    ('select', 'goal'):     ('cxs/goals/query/', 'POST', 200),
    ('select', 'session'):  ('cxs/profiles/search/sessions/', 'POST', 200),

    ('create', 'segment'):  ('cxs/segments/', 'POST', 204),
    ('create', 'rule'):     ('cxs/rules/', 'POST', 204),
    ('create', 'goal'):     ('cxs/goals/', 'POST', 204),

    ('delete', 'segment'):  ('cxs/segments/{item-id}', 'DELETE', 200),
    ('delete', 'rule'):     ('cxs/rules/{item-id}', 'DELETE', 200),
    ('delete', 'profile'):  ('cxs/profiles/{item-id}', 'DELETE', 200),
    ('delete', 'goal'):     ('cxs/goals/{item-id}', 'DELETE', 200),
    ('delete', 'scoring'):  ('cxs/scorings/{item-id}', 'DELETE', 200),
    ('delete', 'scope'):    ('cxs/cluster/{item-id}', 'DELETE', 204),
    ('delete', 'campaign'): ('cxs/campaigns/{item-id}', 'DELETE', 204),

}