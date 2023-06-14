要实现的功能:
    1,控制服务器的权限管理
    2,提供远程访问控制
    3,提供远程操作
    4,提供服务器管理
    5,提供玩家管理
    7,提供插件管理
    8,提供美观的GUI
    9,提供详细的服务器功能

文件目录:
    spoit_GUI
        |main.py
        |
        |
        |----gui
        |     |__init__.py
        |     |mainwin.py
        |         
        |
        |----tools
        |     |__init__.py
        |     |game.py
        |     |web.py
        |     |puctrl.py  
        |     |ctrl.py

    main.py:
        包含核心代码
        要实现的功能：
            启动客户端
    mainwin.py:
        客户端GUI的实现(PyQt)
    game.py:
        实现游戏内操作的功能
    web.py:
        实现远程功能
    puctrl.py:
        实现插件管理
    ctrl.py:
        实现服务器资源管理功能
