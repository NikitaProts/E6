from flask import Flask, jsonify
import redis

r = redis.Redis(host='redis', port=6379)
app = Flask(__name__)


def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/<num>', methods=['GET'])
def get_fibo(num):
    num = int(num)
    mem_num = r.get(num)
    if mem_num:
        return 'From cache: ' + str(mem_num.decode())
    new_num = fibo(num)
    r.set(num, new_num)
    return 'From function: ' + str(new_num)
