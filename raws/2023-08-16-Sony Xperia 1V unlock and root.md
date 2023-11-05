<title>Sony Xperia 1V 刷机经验/教程/记录</title>

初始发布日期: 2023-08-16

# 1. 软件准备

> 建议每次刷机前检查所有软件的更新. 除非你的设备已经EOL, 那样选择距离系统版本的发布日期最近的版本  
> 有人曾说*能用不就行了*. 那么如何判断能不能用呢? **刷成砖的时候就不能用了**

## 1.1 adb tools

推荐使用包管理器, 例如:

```
scoop install adb
```

## 1.2 Newflasher

下载地址: [Newflasher | XDA](https://forum.xda-developers.com/t/tool-newflasher-xperia-command-line-flasher.3619426/#:~:text=com/munjeni/newflasher-,Attachments,-newflasher_v57.zip)

## 1.3 unsin

下载地址: [unsin | XDA](https://forum.xda-developers.com/t/tool-unsin-sin-v3-v4-v5-unpacker-v1-13.3128106/)

## 1.4 XperiFirm

下载地址: [XperiFirm | XDA](https://forum.xda-developers.com/t/tool-xperifirm-xperia-firmware-downloader-v5-6-5.2834142/)


# 2. 安装驱动程序

> 仅使用 `adb` 命令是不需要驱动的. Linux 应该也不需要

## 2.1 adb 驱动

下载地址: [Xperia 1 V driver](https://developer.sony.com/file/download/xperia-1-v-driver/)

只需要安装一次, 以后使用 `fastboot` 命令时(即**蓝灯**模式), 在`设备管理器/其他设备/Android` 的右键菜单更新驱动, 在本机驱动列表中找到 `Sony sa0200`


## 2.2 GordonGate flash 驱动

双击运行 `Newflasher`, 询问你是否需要 ` GordonGate flash driver` 时选*是*. 安装同目录下出现的 `Sony_Mobile_Software_Update_Drivers_x64_Setup.msi`

同理, 只需要安装一次, 以后再进入**绿灯**模式时, 在本机驱动列表中找到 `SOMC flash device`

# 3. 刷机 & root

> **千万不要凭借以往的经验刷机**

1. 重置手机. **不要在引导界面设置锁屏密码**
2. 解锁. 参考官方教程 [How to unlock bootloader](https://developer.sony.com/open-source/aosp-on-xperia-open-devices/get-started/unlock-bootloader/how-to-unlock-bootloader/). **不要在引导界面设置锁屏密码**
3. 制作 `Magsik` 镜像. 在 XperiFirm 下载的 ROM 中, 找到 `init_boot_X-****.sin` 的文件, 用 unsin 提取 img 文件, 然后用 Magisk 修补 img 镜像. **注意: 骁龙 8g2 机型要刷入的是 `init_boot` 分区**
4. 刷入修补得到的 img 镜像  
   i. `adb reboot fastboot` 或在**蓝灯**模式下执行 `fastboot reboot fastboot`  
   ii. `fastboot flash init_boot <path_to_patched_init_boot.img>`  
   iii. `fastboot reboot`. **不要在引导界面设置锁屏密码**
5. **进入桌面后再设置锁屏密码和指纹**. 如果不能设置, 请还原 `init_boot` 镜像并回锁 (`fastboot oem lock`), 然后从第1步重新开始 (注意, 这里是个循环过程, 直到锁屏密码没有问题为止)

# PS

1. 刷入错误的 Magisk 模块导致的 bootloop 救砖命令: `adb wait-for-device shell magisk --remove-modules`
2. 使用 Newflasher 线刷系统时, 要认真阅读选项, 不要凭借经验瞎按 `y` 和 `n`
3. 为了减少麻烦, 执行重置系统等会格式化 `data` 分区的操作前退出谷歌账号
4. 如果不需要解锁root, 而遇到了锁屏密码的问题, 可以参考**第3节**, 跳过解锁相关步骤即可
