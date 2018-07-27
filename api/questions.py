NUM_TOTAL_QUESTIONS = 8

def get_question(store=0):
    '''
    Get an unasked question, as an object with a question String and Id,
    based on the tags and questions given the user session's store.
    Returns object with question String and Id.
    Returns false if no questions left.
    '''
    question = {"text": "Hello?", "id": 12345}
    question_id = mongo_query["id"]
    if (store):
        if store["num_questions"] >= NUM_TOTAL_QUESTIONS:
            return 0
        #elif has_question_been_asked(store, question_id):
        #    return get_question(store)
        else:
            return {"question": mongo_query["text"], "id": question_id}
    else:
        return {"question": mongo_query["text"], "id": question_id}

def get_question_weights(question_id, response):
    '''
    Given a question id and its response ("Y", "N", "M"),
    return a dict of tag ids and their multiplier.
    '''
    # TODO: Get all weights and not just primary tag weight
    if response == "Y":
        question = {"primary_tag": "sports", "primary_tag_weight": 1.0}
        return {question["primary_tag"], question["primary_tag_weight"]}
    elif response == "N":
        question = {"primary_tag": "sports", "primary_tag_weight": 1.0}
        return {question["primary_tag"], 0}
    else:
        return {}

def has_question_been_asked(store, question_id):
    '''
    Given a question store and question id, returns true if
    and only if the question has been asked in the user session.
    '''
    question_set = []
    if ("questions" in store):
        for question_tuple in store["questions"]:
            question_set.append(question_tuple[0])
    return question_id in question_set
