import redis

# 建立链接
# decode_responses=True 得加在获取连接池对象的参数里面, 否则不生效
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# 设置key
r.set('foo', 'bar')

# 获取key的值
print(r.get('foo'))
