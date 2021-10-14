# entr0pia.github.io
风沐白的个人博客

# 模板说明

## 特点
配置简单, 近乎纯文本, 专注于写作

## 配置
1. 复制以下文件和目录到自己的仓库 <br>
    ```
    .github
    main.py
    LICENSE
    ```
2. 修改 ```.github/workflows/update.yml``` 中的 ```user.email``` 和 ```user.email```
3. 根据[ Github 文档](https://docs.github.com/cn/actions/security-guides/automatic-token-authentication)创建令牌

## 规范
1. 文章使用 markdown 书写, 存储在 ```raws``` 路径下
2. 命名格式为 ```年-月-日-*.md```, 如 ```2020-07-22-hyper-V and VirtualBox.md```
3. Markdown 文件第一行必须声明标题, 如 ```<title>Windows 10 (2004) 启用wsl2, 并与VirtualBox 6.0+共存</title>```
4. 图片路径为相对路径, 但路径前必须加 ```/```, 否则网页无法显示图片