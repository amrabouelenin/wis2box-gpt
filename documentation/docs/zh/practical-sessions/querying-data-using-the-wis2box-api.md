```markdown
---
title: 使用 wis2box API 查询数据
---

# 使用 wis2box API 查询数据

!!! abstract "学习成果"
    在本实践课程结束时，您将能够：

    - 使用 wis2box API 查询和筛选您的站点
    - 使用 wis2box API 查询和筛选您的数据

## 引言

wis2box API 提供了一种机器可读的方式，用于发现和查询已经输入到 wis2box 中的数据。该 API 基于 OGC API - Features 标准，并使用 [pygeoapi](https://pygeoapi.io) 实现。

wis2box API 提供以下集合的访问：

- 站点
- 发现元数据
- 数据通知
- 每个配置的数据集一个集合，存储来自 bufr2geojson 的输出（需要在数据映射配置中启用插件 `bufr2geojson` 来填充数据集合中的项目）。

在这个实践课程中，您将学习如何使用数据 API 浏览和查询已经输入到 wis2box 中的数据。

## 准备

!!! note
    在您的网络浏览器中导航到 wis2box API 登陆页面：

    `http://<your-host>/oapi`

<img alt="wis2box-api-landing-page" src="../../assets/img/wis2box-api-landing-page.png" width="600">

## 检查集合

从登陆页面，点击 'Collections' 链接。

!!! question
    在结果页面上您看到多少个数据集合？您认为每个集合代表什么？

??? success "点击以显示答案"
    应该显示 4 个集合，包括“站点”，“发现元数据”和“数据通知”

## 检查站点

从登陆页面，点击 'Collections' 链接，然后点击 'Stations' 链接。

<img alt="wis2box-api-collections-stations" src="../../assets/img/wis2box-api-collections-stations.png" width="600">

点击 'Browse' 链接，然后点击 'json' 链接。

!!! question
    返回了多少个站点？将这个数字与 `http://<your-host>/wis2box-webapp/station` 中的站点列表进行比较。

??? success "点击以显示答案"
    API 中的站点数量应该与您在 wis2box webapp 中看到的站点数量相等。

!!! question
    我们如何查询单个站点（例如 `Balaka`）？

??? success "点击以显示答案"
    使用 `http://<your-host>/oapi/collections/stations/items?q=Balaka` 查询 API。

!!! note
    上述示例基于马拉维测试数据。尝试针对您在之前练习中输入的站点进行测试。

## 检查观测数据

!!! note
    上述示例基于马拉维测试数据。尝试针对您在练习中输入的观测数据进行测试。

从登陆页面，点击 'Collections' 链接，然后点击 '来自马拉维的地面天气观测' 链接。

<img alt="wis2box-api-collections-malawi-obs" src="../../assets/img/wis2box-api-collections-malawi-obs.png" width="600">

点击 'Queryables' 链接。

<img alt="wis2box-api-collections-malawi-obs-queryables" src="../../assets/img/wis2box-api-collections-malawi-obs-queryables.png" width="600">

!!! question
    哪个可查询项用于按站点标识符过滤？

??? success "点击以显示答案"
    正确的可查询项是 `wigos_station_identifer`。

导航回前一页（即 `http://<your-host>/oapi/collections/urn:wmo:md:mwi:mwi_met_centre:surface-weather-observations`）

点击 'Browse' 链接。

!!! question
    我们如何可视化 JSON 响应？

??? success "点击以显示答案"
    通过点击页面右上角的 'JSON' 链接，或在网络浏览器中向 API 请求添加 `f=json`。

检查观测数据的 JSON 响应。

!!! question
    返回了多少条记录？

!!! question
    我们如何将响应限制为 3 条观测数据？

??? success "点击以显示答案"
    在 API 请求中添加 `limit=3`。

!!! question
    我们如何按最新的观测数据对响应进行排序？

??? success "点击以显示答案"
    在 API 请求中添加 `sortby=-resultTime`（注意 `-` 符号表示降序排序）。对于按最早的观测数据排序，更新请求以包含 `sortby=resultTime`。

!!! question
    我们如何按单个站点过滤观测数据？

??? success "点击以显示答案"
    在 API 请求中添加 `wigos_station_identifier=<WSI>`。

!!! question
    我们如何以 CSV 格式接收观测数据？

??? success "点击以显示答案"
    在 API 请求中添加 `f=csv`。

!!! question
    我们如何显示单个观测数据（id）？

??? success "点击以显示答案"
    使用针对观测数据的 API 请求中的特征标识符，查询 API `http://<your-host>/oapi/collections/{collectionId}/items/{featureId}`，其中 `{collectionId}` 是您的观测数据集合的名称，`{itemId}` 是感兴趣的单个观测的标识符。

## 结论

!!! success "恭喜！"
    在这个实践课程中，您学会了：

    - 使用 wis2box API 查询和筛选您的站点
    - 使用 wis2box API 查询和筛选您的数据

```