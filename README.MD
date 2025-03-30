# 抖音直播间监控系统

## 项目简介
这是一个基于WebSocket的抖音直播间监控系统，可以同时监控多个直播间和特定用户的行为，并通过企业微信应用发送通知。

## 主要功能
1. 多直播间监控
   - 支持同时监控多个直播间
   - 实时获取直播间状态

2. 用户行为监控
   - 监控用户开播提醒
   - 监控用户发送的弹幕
   - 监控用户进入直播间
   - 监控用户送礼物
   - 监控用户连麦

3. 企业微信通知
   - 通过企业微信应用发送各类提醒
   - 支持自定义通知模板

## 项目结构
```
douyin_monitor/
├── config/
│   ├── __init__.py
│   ├── config.py          # 配置文件
│   └── wework_config.py   # 企业微信配置
├── core/
│   ├── __init__.py
│   ├── live_monitor.py    # 直播间监控核心
│   ├── user_monitor.py    # 用户监控核心
│   └── wework_notify.py   # 企业微信通知
├── utils/
│   ├── __init__.py
│   ├── logger.py         # 日志工具
│   └── helpers.py        # 辅助函数
├── protobuf/             # 协议文件
├── main.py              # 主程序入口
└── requirements.txt     # 项目依赖
```

## 环境要求
- Python 3.7+
- Node.js v18.2.0
- protoc 版本：libprotoc 25.1

## 配置说明
1. 在 `config/config.py` 中配置：
   - 监控的直播间ID列表
   - 监控的用户ID列表
   - 企业微信应用ID
   - 企业微信密钥
   - 通知接收人列表
   - 其他系统配置


## 使用说明
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 配置企业微信应用：
   - 在企业微信管理后台创建应用
   - 获取应用ID和密钥
   - 配置到 `config/config.py`

3. 运行程序：
   ```bash
   python main.py
   ```

## 注意事项
1. 本项目仅用于学习研究交流
2. 请遵守抖音平台的使用规则
3. 合理使用企业微信通知，避免频繁发送
