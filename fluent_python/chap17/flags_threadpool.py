import os
import time
import sys

import requests

from concurrent import futures

POP20_CC = ('CN IN US ID BR PK UG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split())
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads/')


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = f'{BASE_URL}/{cc.lower()}.gif'
    resp = requests.get(url)
    return resp.content


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return "success"


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    with futures.ProcessPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))
    #     executor的__exit__会调用executor.shutdown(await=True) 所以会阻塞直到所有的线程运行完毕
    # res是一个生成器, 可以迭代来获取返回值
    return len(list(res))


if __name__ == '__main__':
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    print(f'\n{count} flags downloaded in {elapsed:.2f} s')
