import os
import uuid

import re
import locale

import random
import string

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('shop/images/product/', filename)

def get_skip_slug_article(path):
    last_path = path.split('/')[-1]
    skip_slug = None
    
    match = re.search(r'^(?P<article_slug>[\w-]+)-a\d+\.html$', last_path)

    if match:
        skip_slug = match.group('article_slug')

    return skip_slug

def format_currency_vietnam(number):
    locale.setlocale(locale.LC_ALL, 'vi_VN')

    formatted_number = locale.format_string("%d", number, grouping=True)  + "đ"

    return formatted_number

def chunked(items, quantity_per_group):
    # result = []

    # for i in range(0, len(items), quantity_per_group):
    #     chunk = items[i:i+quantity_per_group]

    #     result.append(chunk)

    # return result

    return [items[i:i+quantity_per_group] for i in range(0, len(items), quantity_per_group)]
    
def generate_order_code(length):
    # Tạo mã đơn hàng ngẫu nhiên
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length)) #8NSDHD86
