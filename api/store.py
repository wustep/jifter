import os
import gifts, questions

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
        },
        products: [
            TODO
        ],
        question_count: (number_of_questions_asked)
      }
    },
    ...
}
'''

PRICE_MIN_DEFAULT = os.getenv("PRICE_MIN_DEFAULT")
PRICE_MAX_DEFAULT = os.getenv("PRICE_MAX_DEFAULT")
DEFAULT_TAG_WEIGHT = 0.1

def create_user(session):
    '''
    Creates a user session in the store with a new question.
    Returns true if an existing session was deleted, or false if not.
    '''
    result = 0
    if session in users:
        users.pop(session)
        result = 1
    users[session] = {}
    users[session]["tags"] = {}
    users[session]["questions"] = []
    users[session]["products"] = []
    users[session]["questions_count"] = 1
    add_question(session)
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
        users[session]["questions_count"] += 1
        return 1
    return 0

def answer_question(session, response):
    '''
    Adds answer to user session's store and populates tags accordingly.
    Also adds a new question if available.
    Assumes response is of: "Y" = yes, "M" = maybe, "N" = no.
    Returns 0 if failed, 1 otherwise.
    '''
    if session in users and (response == "Y" or response == "M" or response == "N"):
        if len(users[session]["questions"]) > 0:
            users[session]["questions"][-1][2] = response
            tag_weights = get_question_weights(question_id)
            update_tags(session, tag_weights)
            update_products(session)
            add_question(session, question)
            return 1
    return 0

def get_latest_question(session):
    '''
    Gets the latest unanswered String question, or 0 if unavailable, likely because there are
    no questions, no questions left, or invalid session.
    '''
    if session in users:
        if len(users[session]["questions"] > 0):
            latest_question = users[session]["questions"][-1]
            if (latest_question[2] == 0):
                return latest_question[1]
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

def update_tags(session, tag_weights):
    '''
    Given a user session and a dict of tag weights, update the user's
    tags accordingly.
    '''
    if session in users:
        for tag in tag_weights:
            if tag in users[session]["tags"]:
                users[session]["tags"][tag] *= tag_weights[tag]
            else:
                users[session]["tags"][tag] = DEFAULT_TAG_WEIGHT * tag_weights[tag]
    return 0

def update_products(session):
    '''
    Given a user session, update their products according to their
    tag weights.
    Returns the new list of products, or 0 if failed.
    '''
    if session in users:
        recommendations = gifts.get_recommendations(users[session]["tags"])
        users[session]["products"] = recommendations
    return 0

def get_products(session):
    '''
    Gets a user session's current top products list.
    '''
    if session in users:
        return users[session]["products"]
    return 0
