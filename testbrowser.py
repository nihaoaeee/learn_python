from splinter import Browser
from fake_useragent import UserAgent

# 创建UserAgent对象
ua = UserAgent()

# 生成随机的用户代理
user_agent = ua.random
# 设置浏览器驱动路径

# 创建浏览器对象
browser = Browser(user_agent=user_agent)

# 打开12306网站登录页面
browser.visit('https://kyfw.12306.cn/otn/resources/login.html')

# 自动填写用户名和密码
browser.find_by_id('J-userName').fill('LIGUOXI')
browser.find_by_id('J-password').fill('QAZ123')

# 自动点击登录按钮
browser.find_by_id('J-login').click()

# 等待登录完成
# 根据实际情况，可能需要加入适当的等待时间或条件，以确保登录完成

# 进行后续操作...
# 在登录成功后，您可以继续进行其他操作，如查询车次、选择座位、提交订单等

# 关闭浏览器
# browser.quit()