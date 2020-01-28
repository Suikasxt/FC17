# FC17
清华大学自动化系2020年新生C语言大赛网站搭建（Django）



## 2020/01/26——sxt

1. 创建superuser

   FC17

   Jbto3WD6pi5aHE8m

2. 初步完成login，可以使用test.py测试

   ​	方式为先携带token和用户ID访问login页面之后会将用户信息存入session（因为没有根据token获取用户id的api？）



## 2020/01/28——sxt

1. 初步完成队伍系统后端，包括：
   + 队伍创建（/team）
   + 队伍详情页（/team?id=1）
   + 队伍列表（/teamList）
   + 申请入队，同意入队，退出入队，解散队伍等