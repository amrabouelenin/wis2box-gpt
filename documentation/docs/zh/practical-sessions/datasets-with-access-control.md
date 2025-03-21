---
title: 设置带访问控制的推荐数据集
---

# 设置带访问控制的推荐数据集

!!! abstract "学习成果"
    在本实践课程结束时，您将能够：

    - 创建一个数据政策为“推荐”的新数据集
    - 向数据集添加访问令牌
    - 验证未使用访问令牌无法访问数据集
    - 将访问令牌添加到 HTTP 头部以访问数据集

## 引言

在 WMO 中不被视为“核心”数据集的数据集可以选择配置访问控制政策。wis2box 提供了一种机制，可以向数据集添加访问令牌，这将阻止用户在不提供 HTTP 头部中的访问令牌的情况下下载数据。

## 准备工作

确保您拥有对学生虚拟机的 SSH 访问权限，并且您的 wis2box 实例正在运行。

确保您已使用 MQTT Explorer 连接到 wis2box 实例的 MQTT 代理。您可以使用公共凭据 `everyone/everyone` 连接到代理。

确保您的浏览器已打开并通过 `http://<your-host>/wis2box-webapp` 访问您实例的 wis2box-webapp。

## 练习 1：创建一个数据政策为“推荐”的新数据集

转到 wis2box-webapp 中的“数据集编辑器”页面并创建一个新数据集。使用与之前实践课程相同的中心 ID，并使用模板='surface-weather-observations/synop'。

点击“确定”继续。

在数据集编辑器中，将数据政策设置为“推荐”（注意，更改数据政策将更新“主题层级”）。
用一个描述性名称替换自动生成的“本地 ID”，例如 'recommended-data-with-access-control':

<img alt="create-dataset-recommended" src="../../assets/img/create-dataset-recommended.png" width="800">

继续填写空间属性和联系信息所需的字段，并“验证表单”以检查是否有错误。

最后，使用之前创建的认证令牌提交数据集，并检查新数据集是否已在 wis2box-webapp 中创建。

检查 MQTT-explorer，看看您是否收到了在主题 `origin/a/wis2/<your-centre-id>/metadata` 上宣布新的发现元数据记录的 WIS2 通知消息。

## 练习 2：向数据集添加访问令牌

登录到 wis2box-management 容器，

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

在容器内的命令行中，您可以使用 `wis2box auth add-token` 命令来保护一个数据集，使用 `--metadata-id` 标志来指定数据集的元数据标识符和作为参数的访问令牌。

例如，向元数据标识符为 `urn:wmo:md:not-my-centre:core.surface-based-observations.synop` 的数据集添加访问令牌 `S3cr3tT0k3n`：

```bash
wis2box auth add-token --metadata-id urn:wmo:md:not-my-centre:reco.surface-based-observations.synop S3cr3tT0k3n
```

退出 wis2box-management 容器：

```bash
exit
```

## 练习 3：向数据集发布一些数据

将文件 `exercise-materials/access-control-exercises/aws-example2.csv` 复制到由 `WIS2BOX_HOST_DATADIR` 在您的 `wis2box.env` 中定义的目录：

```bash
cp ~/exercise-materials/access-control-exercises/aws-example2.csv ~/wis2box-data
```

然后使用 WinSCP 或命令行编辑器编辑文件 `aws-example2.csv`，并更新输入数据中的 WIGOS 站点标识符，以匹配您 wis2box 实例中的站点。

接下来，转到 wis2box-webapp 中的站点编辑器。对于您在 `aws-example2.csv` 中使用的每个站点，更新“主题”字段以匹配您在上一个练习中创建的数据集的“主题”。

这个站点现在将与两个主题关联，一个用于“核心”数据集，一个用于“推荐”数据集：

<img alt="edit-stations-add-topics" src="../../assets/img/edit-stations-add-topics.png" width="600">

您将需要使用您的 `collections/stations` 令牌来保存更新的站点数据。

接下来，登录到 wis2box-management 容器：

```bash
cd ~/wis2box-1.0.0rc1
python3 wis2box-ctl.py login
```

从 wis2box 命令行中，我们可以将样本数据文件 `aws-example2.csv` 导入到特定数据集中，如下所示：

```bash
wis2box data ingest -p /data/wis2box/aws-example2.csv --metadata-id urn:wmo:md:not-my-centre:reco.surface-based-observations.synop
```

确保提供正确的数据集元数据标识符，并**检查您在 MQTT Explorer 中是否收到 WIS2 数据通知**，在主题 `origin/a/wis2/<your-centre-id>/data/recommended/surface-based-observations/synop` 上。

检查 WIS2 通知消息中的规范链接，并复制/粘贴该链接到浏览器中尝试下载数据。

您应该看到 403 Forbidden 错误。

## 练习 4：将访问令牌添加到 HTTP 头部以访问数据集

为了演示访问数据集需要访问令牌，我们将使用命令行功能 `wget` 重现您在浏览器中看到的错误。

在您的学生 VM 的命令行中，使用您从 WIS2 通知消息中复制的规范链接的 `wget` 命令。

```bash
wget <canonical-link>
```

您应该看到 HTTP 请求返回 *401 Unauthorized*，数据未被下载。

现在将访问令牌添加到 HTTP 头部以访问数据集。

```bash
wget --header="Authorization: Bearer S3cr3tT0k3n" <canonical-link>
```

现在数据应该被成功下载。

## 结论

!!! success "恭喜！"
    在这个实践课程中，您学会了：

    - 创建一个数据政策为“推荐”的新数据集
    - 向数据集添加访问令牌
    - 验证未使用访问令牌无法访问数据集
    - 将访问令牌添加到 HTTP 头部以访问数据集