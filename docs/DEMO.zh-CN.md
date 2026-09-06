# 总体演示使用指南

[直接打开在线中文演示](https://zxq309.github.io/cowmata/demo/?lang=zh)，也可按以下方式离线使用同一页面。

## 1. 离线交互总览

克隆后用浏览器打开 `demo/index.html`，即可切换中英文、选择处理环节、切换示意场景、拖动时间游标。页面不需要安装依赖、不访问外部数据，也不启动后端。

也可在仓库根目录执行 `python -m http.server 8000 --bind 127.0.0.1`，访问 `http://127.0.0.1:8000/demo/`。

曲线与区间均为合成展示数据，帮助理解职责和数据格式，不运行模型、不展示真实牛只记录、不产生已标定风险结果。数据缺失不解释为低风险。

## 2. 调用真实组件演示

把识别仓克隆到总体仓旁边，按识别仓说明安装环境。有权限的成员可再克隆私有决策仓并安装。运行器不会自行下载源码或私有数据。

Windows PowerShell，在总体仓根目录执行（替换为实际 Python 环境）：

```powershell
python scripts/run_component_demos.py --recognition-python ../cowmata-tailring/.venv/Scripts/python.exe --out runs/component-demo.json

# 已有决策仓权限且完成安装时：
python scripts/run_component_demos.py --recognition-python ../cowmata-tailring/.venv/Scripts/python.exe --include-risk --risk-python ../cowmata-risk/.venv/Scripts/python.exe
```

Linux/macOS 使用对应的 `.venv/bin/python`。目录不在默认相邻位置时，用 `--workspace /path/to/parent` 指定包含组件目录的父目录。

识别演示使用其内置会话实际加载模型；决策演示在自己的合成 V2 包上执行两个证据模块。**两者使用不同输入、独立运行，不是融合端到端预测。** 输出报告记录实际提交号、退出码和结果；环境缺失时提前失败，组件执行出错时返回非零状态。

## 3. 尚待开发

共同事件适配、已标定融合策略及完整牧场部署仍待开发。见[路线图](ROADMAP.md)和[接口提案](INTERFACES.md)。`components.json` 登记选定组件基线，不代表兼容认证。
