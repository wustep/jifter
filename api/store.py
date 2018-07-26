import os

users = {}
PRICE_MIN_DEFAULT = os.getenv("PRICE_MIN_DEFAULT")
PRICE_MAX_DEFAULT = os.getenv("PRICE_MAX_DEFAULT")

def create_user(session):
    '''
    Creates a user session in the store.
    Returns true if an existing session was deleted, or false if not.
    '''
    result = 0
    if session in users:
        users.pop(session)
        result = 1
    users[session] = {}
    return result

def delete_user(session):
    '''
    Delete a user session from the store if exists.
    '''
    users.pop(session, None)

def set_tag(session, tag, value):
    '''
    Sets a tag for a user session in the store.
    Returns 0 if user does not exist, otherwise 1.
    '''
    if session in users:
        users[session][tag] = value
        return 1
    else:
        return 0

def get_tags(session):
    '''
    Gets all tags for a given user session.
    Returns 0 if user does not exist.
    '''
    if session in users:
        return users[session]
    return 0

def set_price(session, price):
    '''
    Sets a user's price expectations, given a price dict with min and max.
    Returns 0 if user does not exist or max < min.
    '''
    if session in users:
        min_price = price["min"] if "min" in price else PRICE_MIN_DEFAULT
        max_price = price["max"] if "max" in price else PRICE_MAX_DEFAULT
        if (min_price < max_price):
            users[session]["price"] = {}
            users[session]["price"]["min"] = min_price
            users[session]["price"]["max"] = max_price
            return 1
    return 0
