** start of main.py **

full_dot = '●'
empty_dot = '○'

def create_character(name, str_stats, int_stats, cha_stats):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    for stat in [str_stats, int_stats, cha_stats]:
        if not isinstance(stat, int):
            return 'All stats should be integers'
        if stat < 1:
            return 'All stats should be no less than 1'
        if stat > 4:
            return 'All stats should be no more than 4'
    if sum([str_stats] + [int_stats] + [cha_stats]) != 7:
        return 'The character should start with 7 points'
    str_bar = full_dot * str_stats + empty_dot * (10 - str_stats)
    int_bar = full_dot * int_stats + empty_dot * (10 - int_stats)
    cha_bar = full_dot * cha_stats + empty_dot * (10 - cha_stats)
    result = (
        f"{name}\n"
        f"STR {str_bar}\n"
        f"INT {int_bar}\n"
        f"CHA {cha_bar}"
    )
    return result
print(create_character("ren", 4, 2, 1))
    


** end of main.py **

