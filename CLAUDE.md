# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库概述

这是一个 Python 脚本的测试/沙盒仓库，用于存放算法练习和实验性代码。所有文件均为独立的 Python 脚本，无依赖关系。

## 运行代码

所有脚本均可直接用 Python 运行，无需额外依赖：

```bash
python file1.py   # 两数之和（索引版本）
python file2.py   # 三数之和
python file3.py   # 两数之和（数值版本）
python file4.py   # 简单打印
```

## 注意事项

- `.gitignore` 中忽略了 `file1.py`，对该文件的修改不会被 `git add` 跟踪（需 `-f` 才能强制添加）
- 远端仓库地址：`git@github.com:pppllh/testrep.git`，单分支 `main`
