import joblib

def load_pickle_file(file_name):
    return joblib.load(filename=file_name)