# -*-coding:utf-8-*-
# python3.4 project

import urllib.request
# urllib提供一系列用于操作URL的功能，request模块可以抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
import urllib.error
# urllib.error提供由链接访问错误的返回信息
import os
# os主要提供对操作系统内的相关操作支持

# --------------
No = 1  # 起始期数
n = 1  # 起始页数
# d_name = 'D:/tui/%02d' % No  这个地方原先失败的原因可能是因为变量永远是作为固定值的，内存中增加的数值应该体现在实际语句中
# --------------
get = True  # 下载标识
loop = True  # 循环标识
err = 0


def download_image(url, save_path):
    urllib.request.urlretrieve(url, save_path)


def download(No, n):
    # 'http://tui.wangyunsheng.com/No/n.jpg'
    html = 'http://tui.wangyunsheng.com/%d/%0d.jpg' % (No, n)
    dic = 'D:/tui/%02d/%d_%02d.jpg' % (No, No, n)
    try:
        response = urllib.request.urlopen(html)
        # html = response.()
    except urllib.error.URLError as e:
        print(html, '这个路径下没有图片，跳过')
        get = False
        return get  # 复位s
    else:
        download_image(html, dic)
        print(html, '下载成功')
        get = True
        return get  # 复位s
    pass


while loop:
    if not download(No, n):  # 当download不为True时
        err += 1  # 错误数加1
        if err == 11:  # 当错误数满足15次时
            No += 1  # 期数加1
            n = 0  # 页数归0
            err = 0  # 错误数归零
            os.mkdir('D:/tui/%02d' % No)  # 新建以期数为名的目录，加在这里的话首个目录需要自己建，因为没有错误返回
    n += 1  # 页数递增
print('OK!')
