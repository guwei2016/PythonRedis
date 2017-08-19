import redis
# r=redis.StrictRedis(host='139.196.95.33',port=7001,db=0,password='guwei123456',decode_responses=True)
rdp = redis.ConnectionPool(host='139.196.95.33',port=7001,db=0,password='guwei123456',decode_responses=True)
r = redis.StrictRedis(connection_pool=rdp)
UserName=r.get('name')
Color=r.hget('car','color')
print(Color)
# if bytes.decode(UserName)=='guwei':
if UserName == 'guwei':
    print(UserName)
    print('Connect OK!')
All_Keys = r.keys()
for Key in All_Keys:
    print(Key)
print(r.client_list())
rdp.disconnect()
print('Finish!')
