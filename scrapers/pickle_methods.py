import pickle


def save(obj, output_file_name):
    with open(output_file_name, 'wb') as text_data:
        my_pickler = pickle.Pickler(text_data)
        my_pickler.dump(obj)


def load(input_file_name):
    with open(input_file_name, 'rb') as text_data:
        my_pickler = pickle.Unpickler(text_data)
        corpus = my_pickler.load()
        return corpus
