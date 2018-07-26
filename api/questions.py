def get_question(session=0):
    '''
    Get a question, as an object with a question String and Id,
    based on the tags given the user session's store.
    Returns object with question String and Id.
    Returns false if no questions left.
    '''
    if (store):
        return {question: "Hello?", id: 0}
    else:
        return {question: "Hello?", id: 0}

def get_question_weights(question_id):
    '''
    Given a question id, return a dict of tag ids and their multiplier.
    '''
    return {}
