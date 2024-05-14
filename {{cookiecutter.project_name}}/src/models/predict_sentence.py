import fasttext
import utils

def predict_sentence(sentence, path_to_model):
    """
       Функция предсказания класса для одного предложения:
       :param sentence: предложение, для которого делается предсказание
       :param path_to_model: путь к модели
       :return: название предсказанного класса и вероятность предсказанного класса
    """
    model = fasttext.load_model(path_to_model)
    res = model.predict(utils.clean_str(sentence))
    class_name = res[0][0].split('__')[2]
    class_probab = round(res[1][0], 3)
    return class_name, class_probab