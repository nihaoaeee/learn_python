<<<<<<< HEAD
# -*- coding: utf-8 -*-
# filename: main.py
import hashlib
import random
=======
def demo(obj=None):
    if obj == None:
        obj = []
    print(obj)
    obj.append(1)
>>>>>>> 328263d278071ea077817b02ab32989ad4e36017


# import web
#
# urls = (
#     '/wx', 'Handle',
# )
#
#
# class Handle(object):
#     def GET(self):
#         return "hello, this is handle view"
def _geneStrTobeSign(args, secret_key):
    l = [("%s=%s" % (key, (args[key] if args[key] != None else ""))) for key in args.keys() if key != "sign"]
    l.sort()
    s = '&'.join(l)
    s = s + ":" + secret_key
    s = str(s)
    return s


if __name__ == '__main__':
    # app = web.application(urls, globals())
    # app.run()

    user_id = 10196
    access_id = 'wa17479c42d6108cec'
    secret_key = 'JatgAEXu8dL1zxwKNx3W9H3rQm061g7q'
    data = {
        "access_id": access_id,
        "user_id": user_id
    }

    sign = hashlib.sha256(_geneStrTobeSign(data, secret_key).encode('utf8')).hexdigest().lower()
    print(sign)

    a = [1, 2, 3, 4]
    for b in a:
        a1, a2 = b
        print(a1, a2)

<<<<<<< HEAD
=======
    # for i in tqdm(range(1000)):
    #     time.sleep(0.001)

    # base_id = [1,2]
    # if 3 not in base_id:
    #     print(1)
    import random

    print(round(5*random.uniform(1, 1.5)))

    a = [1] * 3
    a += [0]
    random.shuffle(a)
    print(a)
>>>>>>> 328263d278071ea077817b02ab32989ad4e36017
