# pywechat 项目副本

微信自动化库及嵌套历史副本。

## 来源与边界

原分支：`pywechat`。详细提交与文件映射见 [迁移清单](../../docs/migration-manifest.json)。

内部工程、资源和许可证保持原目录关系；同主题的不同实现保留各自边界。

## 内容导航

- [111.py](111.py)
- [__init__.py](__init__.py)
- [LICENSE](LICENSE)
- [pics/](pics/)
- [pywechat/](pywechat/)
- [pywechat-main/](pywechat-main/)
- [requirements.txt](requirements.txt)
- [setup.cfg](setup.cfg)
- [setup.py](setup.py)

## 环境与使用

保留外层与 pywechat-main 的完整结构；按原始文档选择一个版本使用，避免混装。

从本模块或具体子工程目录启动。仓库没有统一运行入口，也没有统一依赖文件；不要将所有实验依赖装进同一个环境。

Python 示例建议先创建虚拟环境；优先使用选定子工程已有的 requirements.txt 或 setup.py。没有声明依赖的旧示例，按导入与实际 API 版本补齐，未推定统一版本。

涉及数据文件、模型权重、服务地址、摄像头或硬件的示例，需要先核对源码中的配置与路径。本次只重组资料并验证内容完整性，未宣称所有历史程序均可直接运行。

## 原始说明

原作者说明保存在 [README.upstream.md](README.upstream.md)，其中的相对资源链接仍以当前目录为根。原项目许可证保留，依赖和运行细节优先结合原文与源码查看。
