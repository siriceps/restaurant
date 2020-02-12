import random
import string


def gen_code(*args, is_admin=False):
    code = 'A-' if is_admin else ''
    code += ''.join(str(args[index]) + '-' for index in range(len(args)))
    code += ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    return code
