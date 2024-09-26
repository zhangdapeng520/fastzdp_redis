import redis
import time

# 建立链接
# decode_responses=True 得加在获取连接池对象的参数里面, 否则不生效
pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# 设置key
# nx 不存在, 才新建
r.set('foo', 'bar', nx=True)
r.set('foo', 'bar333', nx=True)
print(r.get('foo'))


# 设置key
# 如果不设置nx, 则每次都会修改
r.set('foo', 'bar')
r.set('foo', 'bar333')
print(r.get('foo'))

