# 人工智能专业课程

课程实验及 FCSN、keras-yolo3 项目副本。

## 来源与边界

原分支：`Specialized_courses_ai_special`。详细提交与文件映射见 [迁移清单](../../docs/migration-manifest.json)。

内部工程、资源和许可证保持原目录关系；同主题的不同实现保留各自边界。

## 内容导航

- [demo01.py](demo01.py)
- [FCSN-master/](FCSN-master/)
- [keras-yolo3-master/](keras-yolo3-master/)
- [第一个实验/](%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%AE%9E%E9%AA%8C/)
- [第二个实验/](%E7%AC%AC%E4%BA%8C%E4%B8%AA%E5%AE%9E%E9%AA%8C/)

## 环境与使用

嵌入的第三方项目保持完整，按各自 README 准备框架、数据和权重。

从本模块或具体子工程目录启动。仓库没有统一运行入口，也没有统一依赖文件；不要将所有实验依赖装进同一个环境。

Python 示例建议先创建虚拟环境；优先使用选定子工程已有的 requirements.txt 或 setup.py。没有声明依赖的旧示例，按导入与实际 API 版本补齐，未推定统一版本。

涉及数据文件、模型权重、服务地址、摄像头或硬件的示例，需要先核对源码中的配置与路径。本次只重组资料并验证内容完整性，未宣称所有历史程序均可直接运行。
