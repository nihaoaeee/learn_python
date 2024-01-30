CLASS_DICT = {}


def register_class(cls):
    global CLASS_DICT
    CLASS_DICT[cls.__name__] = cls
    print(cls.__name__)
    return cls


def get_class():
    import register_class2
    # from register_class2 import MasterTaskConf

get_class()


for _ in range(10):
    print(1)
    for _ in range(10):
        print(2)
        for _ in range(10):
            print(3)
            break
