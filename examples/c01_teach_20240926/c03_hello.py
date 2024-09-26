import redis

# 建立链接
r = redis.Redis(host='localhost', port=6379, db=0)

# 设置key
r.set('foo', 'bar')

# 获取key的值
print(r.get('foo'))