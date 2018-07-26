import os

users = {}
'''
users = {
    (sessionId): {
        price: {
            min: (min),
            max: (max)
        }
        questions: {
            [(id, question, response),
             (id, question, response),
             ...]
        },
        tags: {
            (tagId): value,
            (tagId): value,
            ...
        }
      }
    },
    ...
}
'''

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
    users[session]["tags"] = {}
    users[session]["questions"] = []
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
        users[session]["tags"] = (tag, value)
        return 1
    else:
        return 0

def get_tags(session):
    '''
    Gets all tags for a given user session.
    Returns 0 if user does not exist.
    '''
    if session in users:
        return users[session]["tags"]
    return 0

def add_question(session, question):
    '''
    Adds unanswered question tuple to user session's store.
    Returns 0 if user does not exist or adding question failed.
    Otherwise, returns 1.
    '''
    if session in users and "question" in users[session]:
        question_to_add = (question["id"], question["question"], 0)
        users[session]["question"].push(question_to_add)
        return 1
    return 0

def answer_question(session, response):
    '''
    Adds answer to user session's store and populates tags accordingly.
    Assumes response is of: "Y" = yes, "M" = maybe, "N" = no.
    Returns 0 if failed, 1 otherwise.
    '''
    if session in users and (response == "Y" or response == "M" or response == "N"):
        if len(users[session]["questions"]) > 0:
            users[session]["questions"].peak()[2] = response
            # get_question_weights(question_id)
            # update_tag_weights(session, question)
            return 1
    return 0

def set_price(session, price):
    '''
    Sets a user session's price expectations, given a price dict with min and max.
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
