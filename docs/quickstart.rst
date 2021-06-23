快速开始
============

初始化钉钉SDK
---------------------

企业内部应用，需要到钉钉开发后台注册一个应用，然后获取钉钉应用的以下参数：

1. appkey: 应用的key
#. appsecret: 应用的密钥

拿到以上参数既可初始化一个钉钉SDK实例：

.. code-block :: bash

    from dingtalk.dingtalk import DingTalk

    dingtalk = DingTalk(appkey,appsecret)

初始化完成之后，就可以调用SDK中各种业务接口了，这里以获取管理员账号为例：

.. code-block :: bash

    res = dingtalk.user.get_manager()