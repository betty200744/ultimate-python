import redis

encoding = "utf-8"


# connect
def get_connect():
    conn = redis.Redis(host='localhost', port=6379, db=0)
    return conn


# string,get, set
def string_get_set(r, key, value):
    r.set(key, value)
    tmp = r.get(key)
    result = tmp.decode(encoding)
    print(result)


# hashes, hset, hgetall
def hashes_hset_hgetall(r, key, field, value):
    r.hset(key, field, value)
    tmp = r.hgetall(key)
    result = {}
    for k, v in tmp.items():
        v.decode(encoding)
        result[k.decode(encoding)] = v.decode(encoding)
    r.hdel(key, field, value)
    print(result)


# sorted sets, zadd, zrank, zrange
def ssets_zadd_zrank_zrange(r, key, mapping):
    r.zadd(key, mapping)
    tmp = r.zrange(key, 0, -1)
    result = []
    for v in tmp:
        result.append(v.decode(encoding))

    print(result)


if __name__ == '__main__':
    rd = get_connect()
    string_get_set(rd, 'ss', 'a')
    hashes_hset_hgetall(rd, 'ha', 'id', '1')
    hashes_hset_hgetall(rd, 'ha', 'name', 'n')
    ssets_zadd_zrank_zrange(rd, 'zz', {'1': '1', '2': '2'})
