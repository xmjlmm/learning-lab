# 计算机专业课程

多组课程实验及 CDNet、YOLO 行人检测项目。

## 来源与边界

原分支：`Specialized_courses_computer_science`。详细提交与文件映射见 [迁移清单](../../docs/migration-manifest.json)。

内部工程、资源和许可证保持原目录关系；同主题的不同实现保留各自边界。

## 内容导航

- [CDNet-master/](CDNet-master/)
- [yolo-v3-person136-main/](yolo-v3-person136-main/)
- [实验七/](%E5%AE%9E%E9%AA%8C%E4%B8%83/)
- [实验三/](%E5%AE%9E%E9%AA%8C%E4%B8%89/)
- [实验九/](%E5%AE%9E%E9%AA%8C%E4%B9%9D/)
- [实验二/](%E5%AE%9E%E9%AA%8C%E4%BA%8C/)
- [实验五/](%E5%AE%9E%E9%AA%8C%E4%BA%94/)
- [实验八/](%E5%AE%9E%E9%AA%8C%E5%85%AB/)
- [实验六/](%E5%AE%9E%E9%AA%8C%E5%85%AD/)
- [实验十三/](%E5%AE%9E%E9%AA%8C%E5%8D%81%E4%B8%89/)
- [实验四/](%E5%AE%9E%E9%AA%8C%E5%9B%9B/)

## 环境与使用

CDNet 与 YOLO 的依赖不应强行统一；分别阅读子项目说明。

从本模块或具体子工程目录启动。仓库没有统一运行入口，也没有统一依赖文件；不要将所有实验依赖装进同一个环境。

Python 示例建议先创建虚拟环境；优先使用选定子工程已有的 requirements.txt 或 setup.py。没有声明依赖的旧示例，按导入与实际 API 版本补齐，未推定统一版本。

涉及数据文件、模型权重、服务地址、摄像头或硬件的示例，需要先核对源码中的配置与路径。本次只重组资料并验证内容完整性，未宣称所有历史程序均可直接运行。
