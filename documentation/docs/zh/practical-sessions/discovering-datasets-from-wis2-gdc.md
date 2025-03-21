---
title: 探索 WIS2 全球发现目录中的数据集
---

# 探索 WIS2 全球发现目录中的数据集

!!! abstract "学习成果！"

    在本实践课程结束时，您将能够：

    - 使用 pywiscat 从全球发现目录（GDC）中发现数据集

## 引言

在本课程中，您将学习如何从 WIS2 全球发现目录（GDC）中发现数据。

目前，以下 GDC 可用：

- 加拿大环境与气候变化部，加拿大气象服务： <https://wis2-gdc.weather.gc.ca>
- 中国气象局： <https://gdc.wis.cma.cn/api>
- 德国气象服务： <https://wis2.dwd.de/gdc>

在本地培训期间，会设置一个本地 GDC，以便参与者查询他们从 wis2box 实例发布的元数据。在这种情况下，培训师将提供本地 GDC 的 URL。

## 准备工作

!!! note
    开始前请登录到您的学生虚拟机。

## 安装 pywiscat

使用 `pip3` Python 包安装器在您的虚拟机上安装 pywiscat：
```bash
pip3 install pywiscat
```

!!! note

    如果遇到以下错误：

    ```
    WARNING: The script pywiscat is installed in '/home/username/.local/bin' which is not on PATH.
    考虑将此目录添加到 PATH 或者，如果您希望抑制此警告，请使用 --no-warn-script-location。
    ```

    那么运行以下命令：

    ```bash
    export PATH=$PATH:/home/$USER/.local/bin
    ```

    ...其中 `$USER` 是您在虚拟机上的用户名。

验证安装是否成功：

```bash
pywiscat --version
```

## 使用 pywiscat 查找数据

默认情况下，pywiscat 连接到加拿大的全球发现目录。让我们配置 pywiscat 通过设置 `PYWISCAT_GDC_URL` 环境变量来查询培训 GDC：

```bash
export PYWISCAT_GDC_URL=http://<local-gdc-host-or-ip>
```

让我们使用 [pywiscat](https://github.com/wmo-im/pywiscat) 查询作为培训一部分设置的 GDC。

```bash
pywiscat search --help
```

现在搜索 GDC 的所有记录：

```bash
pywiscat search
```

!!! question

    搜索返回了多少条记录？

??? success "点击以显示答案"
    返回的记录数取决于您查询的 GDC。使用本地培训 GDC 时，您应该看到记录数等于在其他实践课程中已导入到 GDC 的数据集数量。

让我们尝试使用关键词查询 GDC：

```bash
pywiscat search -q observations
```

!!! question

    结果的数据政策是什么？

??? success "点击以显示答案"
    所有返回的数据应指定为“核心”数据

尝试使用 `-q` 进行额外的查询

!!! tip

    `-q` 标志允许以下语法：

    - `-q synop`：查找包含单词 "synop" 的所有记录
    - `-q temp`：查找包含单词 "temp" 的所有记录
    - `-q "observations AND fiji"`：查找包含单词 "observations" 和 "fiji" 的所有记录
    - `-q "observations NOT fiji"`：查找包含单词 "observations" 但不包含 "fiji" 的所有记录
    - `-q "synop OR temp"`：查找同时包含 "synop" 或 "temp" 的所有记录
    - `-q "obs~"`：模糊搜索

    当搜索带有空格的术语时，请用双引号括起来。

让我们获取更多我们感兴趣的特定搜索结果的详细信息：

```bash
pywiscat get <id>
```

!!! tip

    使用上一次搜索的 `id` 值。


## 结论

!!! success "恭喜！"

    在这个实践课程中，您学会了：

    - 使用 pywiscat 从 WIS2 全球发现目录中发现数据集

