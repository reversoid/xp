from copy import deepcopy

user_dict_template: dict = {'page': 1,
                            'bookmarks': set()}

users_db: dict = {}


def createUserStructure():
    return deepcopy(user_dict_template)


def getUserById(id: int):
    return users_db[id]
