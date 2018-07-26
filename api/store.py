users = {}

def create_user(session):
    '''
    Creates a user session in the store.
    '''
    users[session] = {}

def delete_user(session):
    '''
    Delete a user session from the store.
    '''
    users.pop(session, None)

def set_tag(session, tag, value):
    '''
    Sets a tag for a user session in the store.
    '''
    users[session][tag] = value

def get_tags(session):
    '''
    Gets all tags for a given user session.
    '''
    return users[session]
