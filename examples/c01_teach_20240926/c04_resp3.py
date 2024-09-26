import redis

# 建立链接
# 通过参数 protocol=3  支持 RESP3
r = redis.Redis(host='localhost', port=6379, db=0, protocol=3)

# 设置key
r.set('foo', 'bar')

# 获取key的值
print(r.get('foo'))
