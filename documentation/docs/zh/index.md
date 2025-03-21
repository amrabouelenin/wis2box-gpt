---
title: 主页
---

<img alt="WMO logo" src="assets/img/wmo-logo.png" width="200">
# WIS2 in a box 培训

WIS2 in a box ([wis2box](https://docs.wis2box.wis.wmo.int)) 是世界气象组织(WMO) WIS2节点的一个自由和开源(FOSS)参考实现。该项目提供了一个即插即用的工具集，用于使用基于标准的方法摄取、处理和发布天气/气候/水数据，符合WIS2原则。wis2box还提供对WIS2网络中所有数据的访问。wis2box旨在为数据提供者降低进入门槛，提供数据发现、访问和可视化的基础设施和服务。

本培训提供了关于wis2box项目各个方面的逐步解释以及多个练习，帮助您发布和下载WIS2的数据。培训以概述演示和实践练习的形式提供。

参与者将能够使用示例测试数据和元数据，以及整合他们自己的数据和元数据。

本培训涵盖了广泛的主题（安装/设置/配置、发布/下载数据等）。

## 目标和学习成果

本培训的目标是熟悉以下内容：

- WIS2架构的核心概念和组件
- WIS2中用于发现和访问的数据和元数据格式
- wis2box架构和环境
- wis2box的核心功能：
    - 元数据管理
    - 数据摄取和转换为BUFR格式
    - MQTT代理用于WIS2消息发布
    - HTTP端点用于数据下载
    - API端点用于程序化访问数据

## 导航

左侧导航提供了整个培训的目录。

右侧导航提供了特定页面的目录。

## 先决条件

### 知识

- 基本的Linux命令（见[备忘单](cheatsheets/linux.md)）
- 网络和互联网协议的基本知识

### 软件

本培训需要以下工具：

- 运行Ubuntu OS的实例（在本地培训会议期间由WMO培训师提供），见[访问您的学生VM](practical-sessions/accessing-your-student-vm.md#introduction)
- SSH客户端访问您的实例
- 在您的本地机器上的MQTT Explorer
- SCP和FTP客户端从您的本地机器复制文件

## 约定

!!! question

    这样标记的部分邀请您回答一个问题。

您还会注意到文本中有提示和注释部分：

!!! tip

    提示分享如何最好地完成任务。

!!! note

    注释提供了关于实践课程所涵盖主题的额外信息，以及如何最好地完成任务。

示例如下所示：

配置
``` {.yaml linenums="1"}
my-collection-defined-in-yaml:
    type: collection
    title: my title defined as a yaml attribute named title
    description: my description as a yaml attribute named description
```

需要在终端/控制台上输入的代码片段表示为：

```bash
echo 'Hello world'
```

运行中的容器名称（运行的镜像）用**粗体**表示。

## 培训地点和材料

培训内容、wiki和问题跟踪器在GitHub上管理，网址为[https://github.com/wmo-im/wis2box-training](https://github.com/wmo-im/wis2box-training)。

## 打印材料

这个培训可以导出为PDF。要保存或打印这个培训材料，请转到[打印页面](print_page)，然后选择
文件 > 打印 > 保存为PDF。

## 练习材料

练习材料可以从[exercise-materials.zip](/exercise-materials.zip)压缩文件下载。

## 支持

对于问题/错误/建议或对本培训的改进/贡献，请使用[GitHub问题跟踪器](https://github.com/wmo-im/wis2box-training/issues)。

所有wis2box的错误、增强和问题可以在[GitHub](https://github.com/wmo-im/wis2box/issues)上报告。

如需额外支持或有问题，请联系 wis2-support@wmo.int。

如常，wis2box的核心文档始终可以在[https://docs.wis2box.wis.wmo.int](https://docs.wis2box.wis.wmo.int)找到。

欢迎并鼓励贡献！