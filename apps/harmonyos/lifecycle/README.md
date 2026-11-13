# 应用生命周期

ArkTS/HarmonyOS 生命周期学习工程。

## 来源与边界

原分支：`lifecycle`。详细提交与文件映射见 [迁移清单](../../../docs/migration-manifest.json)。

内部工程、资源和许可证保持原目录关系；同主题的不同实现保留各自边界。

## 内容导航

- [.gitignore](.gitignore)
- [AppScope/](AppScope/)
- [build-profile.json5](build-profile.json5)
- [code-linter.json5](code-linter.json5)
- [entry/](entry/)
- [hvigor/](hvigor/)
- [hvigorfile.ts](hvigorfile.ts)
- [oh-package-lock.json5](oh-package-lock.json5)
- [oh-package.json5](oh-package.json5)

## 环境与使用

在 DevEco Studio 中打开本目录，按 build-profile.json5 和 oh-package.json5 配置 SDK 与依赖。

从本模块或具体子工程目录启动。仓库没有统一运行入口，也没有统一依赖文件；不要将所有实验依赖装进同一个环境。

Python 示例建议先创建虚拟环境；优先使用选定子工程已有的 requirements.txt 或 setup.py。没有声明依赖的旧示例，按导入与实际 API 版本补齐，未推定统一版本。

涉及数据文件、模型权重、服务地址、摄像头或硬件的示例，需要先核对源码中的配置与路径。本次只重组资料并验证内容完整性，未宣称所有历史程序均可直接运行。
