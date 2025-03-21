---
title: 在 WIS2 通知中添加 GTS 头部信息
---

# 在 WIS2 通知中添加 GTS 头部信息

!!! abstract "学习成果"

    在本实践课程结束时，您将能够：
    
    - 配置文件名与 GTS 头部信息之间的映射
    - 使用与 GTS 头部信息匹配的文件名导入数据
    - 在 WIS2 通知中查看 GTS 头部信息

## 引言

在向 WIS2 过渡阶段中希望停止在 GTS 上的数据传输的 WMO 成员需要在他们的 WIS2 通知中添加 GTS 头部信息。这些头部信息使得 WIS2 到 GTS 网关能够将数据转发到 GTS 网络。

这允许已迁移到使用 WIS2 节点发布数据的成员禁用他们的 MSS 系统，并确保他们的数据仍然可以供尚未迁移到 WIS2 的成员使用。

WIS2 通知消息中需要添加 GTS 属性作为额外的属性。GTS 属性是一个包含了数据转发到 GTS 网络所需的 GTS 头部信息的 JSON 对象。

```json
{
  "gts": {
    "ttaaii": "FTAE31",
    "cccc": "VTBB"
  }
}
```

在 wis2box 中，您可以通过提供一个名为 `gts_headers_mapping.csv` 的额外文件来自动向 WIS2 通知添加这些信息，该文件包含将 GTS 头部信息映射到传入文件名所需的信息。

这个文件应该放在由 `WIS2BOX_HOST_DATADIR` 在您的 `wis2box.env` 中定义的目录中，并应包含以下列：

- `string_in_filepath`：文件名中的一部分字符串，将用于匹配 GTS 头部信息
- `TTAAii`：要添加到 WIS2 通知的 TTAAii 头部
- `CCCC`：要添加到 WIS2 通知的 CCCC 头部

## 准备工作

确保您有 SSH 访问权限到您的学生 VM，并且您的 wis2box 实例正在运行。

确保您已使用 MQTT Explorer 连接到您的 wis2box 实例的 MQTT 代理。您可以使用公共凭据 `everyone/everyone` 连接到代理。

确保您已经打开了一个网页浏览器，通过访问 `http://<your-host>:3000` 查看您实例的 Grafana 仪表板。

## 创建 `gts_headers_mapping.csv`

要在您的 WIS2 通知中添加 GTS 头部信息，需要一个 CSV 文件来映射 GTS 头部信息到传入的文件名。

CSV 文件应该命名为（确切地）`gts_headers_mapping.csv` 并且应该放在由 `WIS2BOX_HOST_DATADIR` 在您的 `wis2box.env` 中定义的目录中。

## 练习 1：提供一个 `gts_headers_mapping.csv` 文件
    
将文件 `exercise-materials/gts-headers-exercises/gts_headers_mapping.csv` 复制到您的 wis2box 实例并放在由 `WIS2BOX_HOST_DATADIR` 在您的 `wis2box.env` 中定义的目录中。

```bash
cp ~/exercise-materials/gts-headers-exercises/gts_headers_mapping.csv ~/wis2box-data
```

然后重启 wis2box-management 容器以应用更改：

```bash
docker restart wis2box-management
```

## 练习 2：导入带有 GTS 头部信息的数据

将文件 `exercise-materials/gts-headers-exercises/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt` 复制到由 `WIS2BOX_HOST_DATADIR` 在您的 `wis2box.env` 中定义的目录中：

```bash
cp ~/exercise-materials/gts-headers-exercises/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt ~/wis2box-data
```

然后登录到 **wis2box-management** 容器：

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

从 wis2box 命令行中，我们可以将样本数据文件 `A_SMRO01YRBK171200_C_EDZW_20240717120502.txt` 导入到特定数据集中，如下所示：

```bash
wis2box data ingest -p /data/wis2box/A_SMRO01YRBK171200_C_EDZW_20240717120502.txt --metadata-id urn:wmo:md:not-my-centre:core.surface-based-observations.synop
```

确保将 `metadata-id` 选项替换为您数据集的正确标识符。

检查 Grafana 仪表板以查看数据是否正确导入。如果您看到任何警告或错误，尝试修复它们并重复 `wis2box data ingest` 命令。

## 练习 3：查看 WIS2 通知中的 GTS 头部信息

转到 MQTT Explorer 并检查您刚刚导入的数据的 WIS2 通知消息。

WIS2 通知消息应包含您在 `gts_headers_mapping.csv` 文件中提供的 GTS 头部信息。

## 结论

!!! success "恭喜！"
    在这个实践课程中，您学会了如何：
      - 向您的 WIS2 通知添加 GTS 头部信息
      - 通过您的 wis2box 安装验证 GTS 头部信息是否可用