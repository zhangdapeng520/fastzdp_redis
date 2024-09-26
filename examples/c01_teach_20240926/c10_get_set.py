import fastzdp_redis as fzr

# 建立链接
r = fzr.FastZDPRedisClient()

r.set("name", "张大鹏")
print(r.get("name"))
