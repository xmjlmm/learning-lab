# 分支迁移表

快照日期：2026-11-13。以提交 SHA 固定来源；每个原文件均记录 Git blob SHA-1、SHA-256、新路径与原文件模式。

| 原分支 | 原提交 | 主要新目录 | 文件数 |
| --- | --- | --- | --- |
| Algorithms | `91dbad48e1bbd3eba04ac21853769bb79f2cf8fd` | algorithms/fundamentals | 68 |
| Algorithms_and_Data_Structures | `b5a824dae7e90d9f97fcf2ffb8d0ca4e7462d65c` | algorithms/data-structures | 44 |
| Blue_Bridge_Cup | `de581468f822cf81de8bfc37cb8c626ed9c89e48` | algorithms/blue-bridge-cup | 35 |
| Foundations_of_Collective_Intelligence | `db05c144469ebc106579236b2d1f1c7019401271` | ai/swarm-intelligence | 21 |
| Interface | `09b3713f4c3c8af31ebcade7c19863479a13c7fa` | 拆分至 Web、GUI、数据库、Python 和工具；重复内容合并 | 263 |
| Machine_Learning | `7b0110627cae8e51427068cfb7a9e5469f82fad0` | ai/machine-learning | 468 |
| Open_AutoGLM_main | `61860c7d2a2f60987d6c3c7ad03d7e787d455c9c` | third_party/open-autoglm | 37 |
| Opencv_python | `8024e6c8e2f70a97ada1e497e65b3585736f2958` | vision/opencv | 18 |
| Specialized_courses_ai_special | `481d91561280d4e204a5b563e11d3528720f3992` | ai/ai-specialization | 48 |
| Specialized_courses_computer_science | `694213509fa133e9dde251bea436e720962981cd` | ai/computer-science-course | 276 |
| Speech_Recognition | `bffa075e8503838d7ae230a23eec7bf13119bf5f` | audio/speech-recognition | 8 |
| agricultureapp | `7171de8092463361714b47e359eea0accbf5fac1` | apps/harmonyos/agriculture | 71 |
| basic_learning | `db0368b9fa3489bb6e05836858ee3b6d4ea0c713` | python/basics | 31 |
| birthday | `6c10559821292240ff28d35a9d1f2a432eb54e1f` | apps/web/birthday | 61 |
| bug | `033f1e30d2496ff05d8174b0abab1c75233e50b8` | python/web-scraping | 3 |
| dedp_learning_knowledge | `4773a9afd490c7ef0170e6f110d3907c42ad7840` | python/language-features | 35 |
| deep_learning_school | `cfdbf81e7562ab17c025de9fc11c4d9536e33d7c` | ai/deep-learning-course | 20 |
| handing_detect | `5b1d2b17ae9a7f91f14b5a03ad019e7a319f688a` | vision/hand-gesture | 1 |
| image_compressed | `429e9f4275b54ea8c246af0bf1420b23b2176b76` | apps/harmonyos/image-compression | 113 |
| leetcode | `9aaa00b828ac074b75e2603ebe9df6b72e66e073` | algorithms/leetcode | 59 |
| lifecycle | `542ae308ecc0238c5dae0155230abcee0b450300` | apps/harmonyos/lifecycle | 37 |
| main | `4310fb82c812a6a54e65a0643b65a1a7793f539f` | docs/original-main-README.md | 1 |
| mathematical_modeling | `a61d8d6b0e37e3c96a3822a3f41c3af4f2fc974b` | modeling/competitions | 146 |
| meaningful | `35d1e027b45df06294ae3b5937f85600b3f07e27` | apps/creative | 7 |
| path_planning | `337f9808d530bb149dea6e6b66829e915ad50aeb` | robotics/path-planning | 31 |
| plt | `3ca567bce1e7ee2b76a9613213625a45b389ceb6` | visualization/plots | 12 |
| practice | `d950943a61f9c012ff410b0e74829dc2ca421e05` | python/practice | 56 |
| pygame | `84f4c4ba93ca49628d1cf2833e5ed2cf14693c74` | games/pygame | 9 |
| python_periphery | `30e5c59e74f7a4b55118c7b79c86d3500d09d4ab` | third_party/python-periphery | 50 |
| pywechat | `cfc058fc60bb2bdace580b36b6cd2d0b3e9050bd` | third_party/pywechat | 45 |
| robomaster | `7e411e994ec65899e94dd3e2abc0438ea1530bcc` | robotics/robomaster | 15 |
| script | `27dc8d4725c375c827a1fa93c1692be126a8571b` | python/testing | 26 |
| tensorflow | `718583609556d2674386e1771ab5ea83e1eedc92` | ai/tensorflow | 22 |
| the_third_warehouse | `9ea29b6ef8e9951362e7b73fd31da03cbd7ff2d3` | python/misc | 25 |
| tqdm | `e0e9274578e9f38574acb45e582249a1bd1cb892` | tools/tqdm | 8 |
| xalpha | `76cbd672c7fc58f3a41d8aa1ae8be3415dfd7d9c` | third_party/xalpha | 84 |

## 合并规则

Interface 的基础学习、练习、tqdm、the_third_Warehouse 与杂七杂八，分别与对应来源逐文件比较；路径与内容都一致才复用同一目标文件，共合并 108 个重复来源。不同独立工程中的重复资源不跨工程去重。

机器学习分支的好用的工具拆至 tools/ml-experiments；run-* 输出归 archive/training-runs。__pycache__、.idea、.vs、.hvigor 与 .DS_Store 归 archive/generated。原始 README.md 以 README.upstream.md 保留。

## 版本与后续维护

HarmonyOS 的 entry/build 历史构建输出也归入 archive/generated，原文件仍记录在清单中。

整理分支以 origin/main 为基线，保留原始远程分支引用及提交历史；本次不改写历史，也不删除远程分支。旧路径的查找从迁移清单开始，完整旧工程通过原提交恢复。

后续按模块目录维护；功能开发可用 feature/<模块>/<内容> 分支，不再用长期分支隐藏互不相关的课程。HarmonyOS、第三方库和独立网页具备独立工程边界，可在需要单独发布时再拆仓。

第三方项目的许可证、原 README 与内部目录保留；没有添加覆盖全仓库的统一许可证。外部依赖版本、资源路径及硬件行为未在本次统一修复。
