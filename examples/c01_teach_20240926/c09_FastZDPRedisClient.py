import fastzdp_redis as fzr

# 建立链接
rc = fzr.FastZDPRedisClient()
r = rc.get_client()

r.set("name", "张大鹏")
print(r.get("name"))
