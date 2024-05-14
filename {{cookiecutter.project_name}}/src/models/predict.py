from predict_sentence import predict_sentence

def predict(sentence_list: list, path_to_model):
    """
       Функция предсказания класса для списка предложения:
       :param sentence_list: список предложений для предсказания
       :param path_to_model: путь к модели
       :return: список названий предсказанного класса и вероятность предсказанных классов
    """
    class_names = []
    class_probabs = []
    for sentence in sentence_list:
        class_name, class_probab = predict_sentence(sentence, path_to_model)
        class_names.append(class_name)
        class_probabs.append(class_probab)
    return class_names, class_probabs