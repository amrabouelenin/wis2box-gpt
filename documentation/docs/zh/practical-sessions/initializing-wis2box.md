---
title: 初始化 wis2box
---

# 初始化 wis2box

!!! abstract "学习成果"

    在本实践课程结束时，您将能够：

    - 运行 `wis2box-create-config.py` 脚本创建初始配置
    - 启动 wis2box 并检查其组件的状态
    - 在浏览器中访问 **wis2box-webapp**、API、MinIO UI 和 Grafana 仪表板
    - 使用 MQTT Explorer 连接到本地的 **wis2box-broker**

!!! note

    当前的培训材料使用的是 wis2box-1.0.0rc1。
    
    如果您在本地培训课程之外运行此培训，请参阅 [accessing-your-student-vm](accessing-your-student-vm.md) 了解如何下载和安装 wis2box 软件堆栈的指南。

## 准备工作

使用您的用户名和密码登录到指定的 VM，并确保您位于 `wis2box-1.0.0rc1` 目录中：

```bash
cd ~/wis2box-1.0.0rc1
```

## 创建初始配置

wis2box 的初始配置需要：

- 一个包含配置参数的环境文件 `wis2box.env`
- 由环境变量 `WIS2BOX_HOST_DATADIR` 定义的主机上的目录，用于主机和 wis2box 容器之间的共享

可以使用 `wis2box-create-config.py` 脚本来创建您的 wis2box 的初始配置。

它将询问您一系列问题以帮助设置您的配置。

脚本完成后，您将能够查看和更新配置文件。

按以下方式运行脚本：

```bash
python3 wis2box-create-config.py
```

### wis2box-host-data 目录

脚本将要求您输入用于 `WIS2BOX_HOST_DATADIR` 环境变量的目录。

请注意，您需要定义此目录的完整路径。

例如，如果您的用户名是 `username`，则目录的完整路径为 `/home/username/wis2box-data`：

```{.copy}
username@student-vm-username:~/wis2box-1.0.0rc1$ python3 wis2box-create-config.py
请输入用于 WIS2BOX_HOST_DATADIR 的目录：
/home/username/wis2box-data
将设置用于 WIS2BOX_HOST_DATADIR 的目录为：
    /home/username/wis2box-data
这是正确的吗？(y/n/exit)
y
已创建目录 /home/username/wis2box-data。
```

### wis2box URL

接下来，您将被要求输入您的 wis2box 的 URL。这是用于访问 wis2box 网络应用程序、API 和 UI 的 URL。

请使用 `http://<your-hostname-or-ip>` 作为 URL。

```{.copy}
请输入 wis2box 的 URL：
 对于本地测试，URL 是 http://localhost
 若要启用远程访问，URL 应指向托管 wis2box 的服务器的公共 IP 地址或域名。
http://username.wis2.training
将设置 wis2box 的 URL 为：
  http://username.wis2.training
这是正确的吗？(y/n/exit)
```

### WEBAPP、STORAGE 和 BROKER 密码

在提示输入 `WIS2BOX_WEBAPP_PASSWORD`、`WIS2BOX_STORAGE_PASSWORD`、`WIS2BOX_BROKER_PASSWORD` 时，您可以选择生成随机密码，并定义您自己的密码。

不用担心记住这些密码，它们将被存储在您的 wis2box-1.0.0rc1 目录中的 `wis2box.env` 文件中。

### 查看 `wis2box.env`

脚本完成后检查当前目录中 `wis2box.env` 文件的内容：

```bash
cat ~/wis2box-1.0.0rc1/wis2box.env
```

或通过 WinSCP 检查文件的内容。

!!! question

    `wis2box.env` 文件中 WISBOX_BASEMAP_URL 的值是什么？

??? success "点击以显示答案"

    WIS2BOX_BASEMAP_URL 的默认值是 `https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`。

    此 URL 指向 OpenStreetMap 瓦片服务器。如果您想使用不同的地图提供商，可以将此 URL 更改为指向不同的瓦片服务器。

!!! question 

    `wis2box.env` 文件中 WIS2BOX_STORAGE_DATA_RETENTION_DAYS 环境变量的值是多少？

??? success "点击以显示答案"

    WIS2BOX_STORAGE_DATA_RETENTION_DAYS 的默认值是 30 天。如果您愿意，可以将此值更改为不同的天数。
    
    wis2box-management 容器每天运行一次 cronjob，从 `wis2box-public` 存储桶和 API 后端删除超过 WIS2BOX_STORAGE_DATA_RETENTION_DAYS 定义的天数的数据：
    
    ```{.copy}
    0 0 * * * su wis2box -c "wis2box data clean --days=$WIS2BOX_STORAGE_DATA_RETENTION_DAYS"
    ```

!!! note

    `wis2box.env` 文件包含定义您的 wis2box 配置的环境变量。有关更多信息，请参阅 [wis2box-documentation](https://docs.wis2box.wis.wmo.int/en/latest/reference/configuration.html)。

    除非您确定要进行的更改，请不要编辑 `wis2box.env` 文件。不正确的更改可能导致您的 wis2box 停止工作。

    不要与任何人分享您的 `wis2box.env` 文件的内容，因为它包含敏感信息，如密码。