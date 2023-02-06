def myzip(it1, it2):
    """
    Name: Artiom
    Functon Name: myzip
    Description: zipping two collections
    :param it1:
    :param it2:
    :return:
    """
    try:
        if type(it1) is list and type(it2) is list and (all(isinstance(item, int) for item in it1) and (all(isinstance(item, int) for item in it2))):
            return zip(it1, it2)
    except Exception as e:
        raise e
