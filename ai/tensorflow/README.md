# TensorFlow 学习

MNIST、Fashion、激活函数、损失函数、优化器与正则化。

## 来源与边界

原分支：`tensorflow`。详细提交与文件映射见 [迁移清单](../../docs/migration-manifest.json)。

内部工程、资源和许可证保持原目录关系；同主题的不同实现保留各自边界。

## 内容导航

- [BP神经网络优化器/](BP%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%E4%BC%98%E5%8C%96%E5%99%A8/)
- [chap4/](chap4/)
- [fashion数据集八股.py](fashion%E6%95%B0%E6%8D%AE%E9%9B%86%E5%85%AB%E8%82%A1.py)
- [MNIST数据集.py](MNIST%E6%95%B0%E6%8D%AE%E9%9B%86.py)
- [MNIST数据集八股.py](MNIST%E6%95%B0%E6%8D%AE%E9%9B%86%E5%85%AB%E8%82%A1.py)
- [pytorch/](pytorch/)
- [spyder/](spyder/)
- [tensorflow入门.py](tensorflow%E5%85%A5%E9%97%A8.py)
- [test.py](test.py)
- [指数衰减学习率.py](%E6%8C%87%E6%95%B0%E8%A1%B0%E5%87%8F%E5%AD%A6%E4%B9%A0%E7%8E%87.py)
- [损失函数.py](%E6%8D%9F%E5%A4%B1%E5%87%BD%E6%95%B0.py)
- [激活函数.py](%E6%BF%80%E6%B4%BB%E5%87%BD%E6%95%B0.py)
- [神经网络.py](%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C.py)
- [类封装网络八股sequential.py](%E7%B1%BB%E5%B0%81%E8%A3%85%E7%BD%91%E7%BB%9C%E5%85%AB%E8%82%A1sequential.py)
- [缓解过拟合，正则化.py](%E7%BC%93%E8%A7%A3%E8%BF%87%E6%8B%9F%E5%90%88%EF%BC%8C%E6%AD%A3%E5%88%99%E5%8C%96.py)
- [网络八股sequential.py](%E7%BD%91%E7%BB%9C%E5%85%AB%E8%82%A1sequential.py)

## 环境与使用

保留原始教学代码；检查 TensorFlow API 版本，按实验分别准备环境。

从本模块或具体子工程目录启动。仓库没有统一运行入口，也没有统一依赖文件；不要将所有实验依赖装进同一个环境。

Python 示例建议先创建虚拟环境；优先使用选定子工程已有的 requirements.txt 或 setup.py。没有声明依赖的旧示例，按导入与实际 API 版本补齐，未推定统一版本。

涉及数据文件、模型权重、服务地址、摄像头或硬件的示例，需要先核对源码中的配置与路径。本次只重组资料并验证内容完整性，未宣称所有历史程序均可直接运行。
