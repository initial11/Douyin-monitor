#!/usr/bin/python
# coding:utf-8

# @FileName:    main.py
# @Time:        2024/1/2 22:27
# @Author:      bubu
# @Project:     douyinLiveWebFetcher

import threading
import logging
from config.config import Config
from core.live_monitor import LiveMonitor
from core.user_monitor import UserMonitor
from utils.logger import setup_logger

def main():
    # 设置日志
    logger = setup_logger()
    logger.info("启动抖音直播间监控系统")
    
    # 创建直播间监控线程
    room_monitors = []
    for room_id in Config.MONITOR_ROOMS:
        monitor = LiveMonitor(room_id)
        thread = threading.Thread(target=monitor.start, daemon=True)
        room_monitors.append((monitor, thread))
        thread.start()
        logger.info(f"启动直播间监控线程: {room_id}")
    
    # 创建用户监控线程
    user_monitor = UserMonitor()
    user_thread = threading.Thread(target=user_monitor.start, daemon=True)
    user_thread.start()
    logger.info("启动用户监控线程")
    
    try:
        # 等待所有线程
        for _, thread in room_monitors:
            thread.join()
        user_thread.join()
    except KeyboardInterrupt:
        logger.info("收到退出信号，正在关闭...")
    except Exception as e:
        logger.error(f"程序运行出错: {e}")
    finally:
        logger.info("程序已退出")

if __name__ == '__main__':
    main()
