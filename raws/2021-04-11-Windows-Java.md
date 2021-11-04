<title>Windows平台Java开发环境配置</title>

在2021年, 我们应该抛弃古老的传统, 而用现代化的方法来安装Java.
<p align="right" >--不是鲁迅说的</p>

# 1. 安装方法

打开PowerShell, 输入以下命令:

```powershell
# 网络环境不好的话, 请使用代理
# $env:https_proxy='<host>:<port>'
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
scoop bucket add java
scoop update
scoop install microsoft-lts-jdk # 微软推出的 java 开发套件
# scoop install adopt8-hotspot # java 8
```

# 2. 为什么这样做

## 2.1 纯命令行

人们都或多或少接触过Linux.
在Linux下面安装软件, 基本只需要在命令行使用包管理器即可完成软件的查询, 安装, 更新和卸载.

Windows下同样也有包管理器, **Chocolatey**, **Scoop**, 以及微软自己的**winget**等等.
这里使用的就是**Scoop**, 你可以到它的[Github](https://github.com/lukesampson/scoop)页面了解更多.

虽然Windows的包管理器不可能完全覆盖Windows软件生态, 但对于开发人员来说, 其常用的软件肯定是优先纳入的.
除了Java, 你还可以用Scoop配置Golang, Python, GCC等环境.
只需要一行命令, 不用再自己去配置环境变量.

## 2.2 版本管理

你可以用Scoop同时安装几个jdk版本, 同样只需要一行命令:
```powershell
scoop reset <jdk_package_name>
```
就可以在不同版本之间切换.


同样的, 更新小版本号也仅需一行命令:
```powershell
scoop update <jdk_package_name>
```

## 2.3 规避法律风险

传统的方法总是会引导人们去下载安装**Oracle JDK**, 实际上这是有一定的法律风险的.
在生产环境下使用Oracle JDK是需要授权的.
虽然Oracle公司不一定会找上门来, 但还是要做一个遵纪守法的好公民的.

---

2021年11月04日更新

自JDK 17及以后, Oracle JDK可以免费商用了. 但还是不建议, 谁知道它会不会又改回去呢.

> Oracle 最新发布的 NFTC 许可 中撤回了 2018 年制定的要对 Oracle JDK 收取商用费用的决定，并且也将继续提供 Oracle OpenJDK 发行版。最新 NFTC 适用于最近发布的 Oracle JDK 17 和后续版本。Oracle 对此解释称，“在 GPL 下提供的 Oracle OpenJDK 构建版本是非常受欢迎的，但来自开发者、学术界和企业的反馈是，他们也希望在一个明确的自由条款许可下获得值得信赖、坚如磐石的 Oracle JDK。”并明确表示，新版 NFTC “包括商业和生产用途”，而且“只要不收费，允许再分发”。但调查表明，甲骨文的 JDK 发行版已不再是最受欢迎的 Java 发行版。开发人员们更喜欢 AdoptOpenJDK、亚马逊、微软等其他供应商的 OpenJDK 发行版。