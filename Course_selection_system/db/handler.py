import os
import pickle
from conf import settings


def save(obj):
    path = os.path.join(settings.DB_INFO, obj.__class__.__name__.lower())
    if not os.path.isdir(path):
        os.mkdir(path)
    obj_file = os.path.join(path, obj.name)
    with open(obj_file, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()


def query(name, user_type):
    path = os.path.join(settings.DB_INFO, user_type)
    if not os.path.isdir(path):
        os.mkdir(path)
    obj_file = os.path.join(path, name)
    if os.path.exists(obj_file):
        with open(obj_file, 'rb') as f:
            return pickle.load(f)
    else:
        return False


