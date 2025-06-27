
def sort_by_date(my_list: list, reverse=False) -> list:
    '''Функция сортирует список словарей по дате'''  # noqa
    sorted_list = sorted(my_list, key=lambda x: x['date'], reverse=reverse)
    return sorted_list
