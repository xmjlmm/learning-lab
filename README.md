# learning-lab

学校课程、算法练习、实验与独立项目的统一导航。内容从原仓库 36 个分支的当前提交整理而来，按主题分目录，并保留来源与原始内容。

## 内容导航

| 目录 | 内容 |
| --- | --- |
| [algorithms](algorithms/README.md) | 算法与竞赛 |
| [python](python/README.md) | Python 学习 |
| [tools](tools/README.md) | 工具与实验管理 |
| [ai](ai/README.md) | 人工智能课程 |
| [vision](vision/README.md) | 计算机视觉 |
| [audio](audio/README.md) | 音频与语音 |
| [robotics](robotics/README.md) | 机器人与规划 |
| [modeling](modeling/README.md) | 数学建模 |
| [visualization](visualization/README.md) | 数据可视化 |
| [games](games/README.md) | 游戏开发 |
| [web](web/README.md) | Web 框架 |
| [desktop](desktop/README.md) | 桌面界面 |
| [databases](databases/README.md) | 数据库 |
| [apps](apps/README.md) | 独立应用 |
| [third_party](third_party/README.md) | 第三方项目副本 |
| [archive](archive/README.md) | 历史训练输出、缓存与工程元数据 |

## 开始使用

1. 从上表选择主题，再进入模块 README。
2. Python 课程按单个示例或子工程准备独立环境；HarmonyOS 工程在 DevEco Studio 中打开具体应用目录。
3. 数据集、模型、服务和硬件按模块说明配置；本仓库不是一个统一应用。

## 整理与核对

- [分支迁移表与整理规则](docs/BRANCH-MAP.md)
- [完整文件迁移与校验清单](docs/migration-manifest.json)
- [验证报告](docs/VALIDATION.md)
- [复查脚本](scripts/verify_migration.py)：在仓库根目录运行 `python scripts/verify_migration.py`。
- [维护约定](CONTRIBUTING.md)
- [第三方与许可说明](NOTICE.md)

原分支名和历史拼写记录在迁移表中；新目录采用稳定主题名称。原文件内容保留，重复来源在清单中指向同一个文件。
