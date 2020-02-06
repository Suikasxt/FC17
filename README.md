# FC17
清华大学自动化系2020年新生C语言大赛网站搭建（Django）



## 后端API列表（持续更新）

+ api/user/login/：post携带token、ID或者username、ID、password，返回提示信息
+ api/user/：获取已登录用户信息
+ api/user/{userid}：获取指定id用户信息
+ api/logout/：登出
+ api/team/：获取当前已登录用户队伍信息
+ api/team/{teamid}：获取指定id队伍信息
+ api/team/list：获取队伍列表
+ api/notice/list：获取公告列表
+ api/team/quit/：退出当前队伍或取消入队申请
+ api/team/apply/{teamid}：申请加入某队伍（同一时刻只能申请一个，会覆盖之前的请求）
+ api/team/manage/：修改队伍信息，post可携带数据为：
  + name、introduction（string）：直接修改队伍信息，若用户当前不属于任何队伍则创建新队伍
  + accept、dismiss（int）：通过某用户申请或踢出队内某用户
  + disband（boolean）：为true时解散队伍
+ api/team/leaderboard/{type}：type为total或daily，与api/team/list类似，但是会带上天梯分并且按指定天梯分排序








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



## 2020/01/29——sxt

1. 完成搭建公告系统和评论系统
2. 调整了部分代码结构
3. <font color=red>尝试了一下logout发现并不能登出？？？</font> 



## 2020/02/01——sxt

1. 前端实现登录，但代码结构散乱，后期可以看情况调整



## 2020/02/02——sxt

前端：

1. 登出
2. 个人信息
3. 队伍列表
增添了一些对于非法url的重定向


## 2020/02/03——urkax

前端：公告


## 2020/02/04——sxt

前端队伍系统



## 2020/02/05——urkax

ai文件提交




## 2020/02/06——urkax

ai文件删除，个人ai文件列表
队伍ai文件列表，ai文件下载，队长文件选择