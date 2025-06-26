
def filter_by_state(list_of_dict: list, state='EXECUTED') -> list:
    """Возвращает список словарей, у которых ключ state
       соответствует указанному значению, по умолчанию
       state = EXECUTED"""                              # noqa


    filtered_list = []
    for dic in list_of_dict:
         if dic.get('state') == state:
             filtered_list.append(dic)
    return filtered_list
