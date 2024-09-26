import redis

# 建立链接
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

# 设置key
r.set('foo', 'bar')

# 获取key的值
print(r.get('foo'))
