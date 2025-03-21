---
title: 访问您的学生虚拟机
---

# 访问您的学生虚拟机

!!! abstract "学习成果"

    通过本实践课程，您将能够：

    - 通过 SSH 和 WinSCP 访问您的学生虚拟机
    - 验证实践练习所需软件是否已安装
    - 确认您可以在本地学生虚拟机上访问本次培训的练习材料

## 引言

作为本地运行的 wis2box 培训课程的一部分，您可以在名为“WIS2-training”的本地培训网络上访问您的个人学生虚拟机。

您的学生虚拟机已预装以下软件：

- Ubuntu 22.0.4.3 LTS [ubuntu-22.04.3-live-server-amd64.iso](https://releases.ubuntu.com/jammy/ubuntu-22.04.3-live-server-amd64.iso)
- Python 3.10.12
- Docker 24.0.6
- Docker Compose 2.21.0
- 文本编辑器：vim, nano

!!! note

    如果您想在本地培训课程之外进行此培训，您可以使用任何云服务提供商提供自己的实例，例如：

    - GCP（谷歌云平台）VM 实例 `e2-medium`
    - AWS（亚马逊网络服务）ec2 实例 `t3a.medium`
    - Azure（微软）Azure 虚拟机 `standard_b2s`

    选择 Ubuntu Server 22.0.4 LTS 作为操作系统。
    
    创建您的虚拟机后，请确保已安装 python、docker 和 docker compose，如 [wis2box-software-dependencies](https://docs.wis2box.wis.wmo.int/en/latest/user/getting-started.html#software-dependencies) 所述。
    
    本次培训中使用的 wis2box 发布档案可以通过以下方式下载：

    ```bash
    wget https://github.com/wmo-im/wis2box/releases/download/1.0.0rc1/wis2box-setup-1.0.0rc1.zip
    unzip wis2box-setup-1.0.0rc1.zip
    ```
    
    您可以在 [https://github.com/wmo-im/wis2box/releases](https://github.com/wmo-im/wis2box/releases) 找到最新的 'wis2box-setup' 档案。

    本次培训使用的练习材料可以通过以下方式下载：

    ```bash
    wget https://training.wis2box.wis.wmo.int/exercise-materials.zip
    unzip exercise-materials.zip
    ```

    运行练习材料需要以下额外的 Python 包：

    ```bash
    pip3 install minio
    ```

    如果您在本地 WIS2 培训课程中使用提供的学生虚拟机，所需软件将已经安装。

## 在本地培训网络上连接到您的学生虚拟机

按照培训师提供的指示，将您的 PC 连接到 WIS2 培训期间在教室内广播的本地 Wi-Fi。

使用 SSH 客户端使用以下信息连接到您的学生虚拟机：

- **主机：（在面对面培训中提供）**
- **端口：22**
- **用户名：（在面对面培训中提供）**
- **密码：（在面对面培训中提供）**

!!! tip
    如果您不确定主机名/用户名或连接有问题，请联系培训师。

连接后，请更改您的密码以确保其他人无法访问您的虚拟机：

```bash
limper@student-vm:~$ passwd
更改 testuser 的密码。
当前密码：
新密码：
重新输入新密码：
passwd: 密码更新成功
```

## 验证软件版本

为了能够运行 wis2box，学生虚拟机应预装 Python、Docker 和 Docker Compose。

检查 Python 版本：
```bash
python3 --version
```
返回：
```console
Python 3.10.12
```

检查 Docker 版本：
```bash
docker --version
```
返回：
```console
Docker version 24.0.6, build ed223bc
```

检查 Docker Compose 版本：
```bash
docker compose version
```
返回：
```console
Docker Compose version v2.21.0
```

为确保您的用户可以运行 Docker 命令，您的用户已被添加到 `docker` 组。

测试您的用户是否可以运行 docker hello-world，运行以下命令：
```bash
docker run hello-world
```

这应该会拉取 hello-world 镜像并运行一个打印消息的容器。

检查您的输出中是否显示以下内容：

```console
...
Hello from Docker!
This message shows that your installation appears to be working correctly.
...
```

## 检查练习材料

检查您的主目录内容；这些是作为培训和实践课程的一部分使用的材料。

```bash
ls ~/
```
返回：
```console
exercise-materials  wis2box-1.0.0rc1
```

如果您的本地 PC 上安装了 WinSCP，您可以使用它连接到您的学生虚拟机，并检查您的主目录内容以及在您的虚拟机和本地 PC 之间下载或上传文件。

WinSCP 不是培训所必需的，但如果您想在本地 PC 上使用文本编辑器编辑虚拟机上的文件，它可能会很有用。

以下是使用 WinSCP 连接到您的学生虚拟机的方法：

打开 WinSCP 并点击“新站点”。您可以如下创建一个新的 SCP 连接到您的虚拟机：

<img alt="winscp-student-vm-scp.png" src="../../assets/img/winscp-student-vm-scp.png" width="400">

点击“保存”然后“登录”以连接到您的虚拟机。

您应该能够看到以下内容：

<img alt="winscp-student-vm-exercise-materials.png" src="../../assets/img/winscp-student-vm-exercise-materials.png" width="600">

## 结论

!!! success "恭喜！"
    在这个实践课程中，您学会了：

    - 通过 SSH 和 WinSCP 访问您的学生虚拟机
    - 验证实践练习所需软件是否已安装
    - 确认您可以在本地学生虚拟机上访问本次培训的练习材料