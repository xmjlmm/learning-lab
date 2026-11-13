# RoboMaster

瞄准、串口通信、CRC、滤波和目标选择原型。

## 来源与边界

原分支：`robomaster`。详细提交与文件映射见 [迁移清单](../../docs/migration-manifest.json)。

内部工程、资源和许可证保持原目录关系；同主题的不同实现保留各自边界。

## 内容导航

- [aiming_node(改).py](aiming_node%28%E6%94%B9%29.py)
- [aiming_Node.py](aiming_Node.py)
- [aiming_process.py](aiming_process.py)
- [crc.py](crc.py)
- [rm_serial_driver.py](rm_serial_driver.py)
- [vscode launch 配置.py](vscode%20launch%20%E9%85%8D%E7%BD%AE.py)
- [一阶低通滤波.py](%E4%B8%80%E9%98%B6%E4%BD%8E%E9%80%9A%E6%BB%A4%E6%B3%A2.py)
- [卡尔曼滤波器/](%E5%8D%A1%E5%B0%94%E6%9B%BC%E6%BB%A4%E6%B3%A2%E5%99%A8/)
- [波形图.py](%E6%B3%A2%E5%BD%A2%E5%9B%BE.py)
- [舵少/](%E8%88%B5%E5%B0%91/)
- [选板逻辑.cpp](%E9%80%89%E6%9D%BF%E9%80%BB%E8%BE%91.cpp)
- [选班.py](%E9%80%89%E7%8F%AD.py)

## 环境与使用

部分代码依赖 ROS、串口设备及配套硬件；先检查设备名、协议与节点配置。

从本模块或具体子工程目录启动。仓库没有统一运行入口，也没有统一依赖文件；不要将所有实验依赖装进同一个环境。

Python 示例建议先创建虚拟环境；优先使用选定子工程已有的 requirements.txt 或 setup.py。没有声明依赖的旧示例，按导入与实际 API 版本补齐，未推定统一版本。

涉及数据文件、模型权重、服务地址、摄像头或硬件的示例，需要先核对源码中的配置与路径。本次只重组资料并验证内容完整性，未宣称所有历史程序均可直接运行。
