import re
import pickle
import numpy as np

def clean_str(s: str) -> str:
    """
    Функция обработки строки удаляет числа, заменяет сокращения:
    :param s: строка, которую необходимо обработать
    :return: строка с заменой сокращений, удаленными числами
    """
    file_dict = open("../references/dict_1.pkl", "rb")
    dict_1 = pickle.load(file_dict)
    file_dict.close()

    file_dict = open("../references/dict_2.pkl", "rb")
    dict_2 = pickle.load(file_dict)
    file_dict.close()

    s = s.strip().lower()
    for key in dict_1:
        s = s.replace(key, dict_1[key])
    s = re.sub('[0-9]', ' ', s)
    s = re.sub(" +", " ", s)
    s = re.sub(r'\W+', " ", s)
    arr = np.array(s.split())
    if len(arr) == 0:
        return ''
    for key in dict_2:
        arr = np.where(arr == key, dict_2[key], arr)
    s = ' '.join(arr)
    return s

