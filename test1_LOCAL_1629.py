# -*- coding: utf-8 -*-
# filename: main.py
import hashlib
import random


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

