<title>分享我的 NekoSMS 正则表达式</title>

初始发布日期: 2021-10-15

# 1. NekoSMS 介绍

NekoSMS 是一个用于屏蔽短信的 Xposed 插件, 支持正则表达式, 通配符等多种屏蔽方式. 适配 Android 4.4-11. 项目主页 [github.com/apsun/NekoSMS](https://github.com/apsun/NekoSMS).

*额外的, [QKSMS](https://github.com/moezbhatti/qksms) (一个开源短信息 App) 将在未来加入正则屏蔽功能.*

# 2. 我的正则表达式

## 2.1 订阅类短信

**黑名单规则:** ```[退回复拒].{0,2}[退回订拒关定TDQX]|TD```

**说明:** 覆盖我遇到过的各种订阅类短信. 至于为什么 ```TD``` 要单独摘出来, 似乎是会导致误杀, 具体是什么我忘了.

## 2.2 引导加垃圾微信号的短信

**目标示例:** 
> 【顺丰快递】风沐白，祝贺您成为小米优选用户，+㜫： **855317522505** 送一个小米空气炸锅（免递）终止明天！

显然, 这是一个含有境外号码的垃圾短信.

**白名单规则:**

```(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[0-35-9]\d{2}|4(?:0\d|1[0-2]|9\d))|9[0-35-9]\d{2}|6[2567]\d{2}|4(?:(?:10|4[01])\d{3}|[68]\d{4}|[579]\d{2}))\d{6}```

```(?:\+?86)?0(?:(?:(?:(?:10|2[^6])|3(?:1[^1]|35|49|5\d|7[^1789]|9[^079])|4(?:1[^0134]|2[179]|3[^0-2]||5[^01]|6[4789]|7\d|8[23])|5(?:3[^12]|4[36]|5[^1]|6[12346]|7[280]|80|9[^015])|6(?:3[1235]|6[0238]|9[12])|7(?:01|(?:1|7)\d|2[248]|3[^123]|4[3-6]|5[^457]|6[02368]|9[^1])|8(?:1[23678]|2[567]|3\d|5[4-9]|7[^1]|8[3678]|9[1-7])|9(?:1[^08]|(?:3|7|9)\d|4[13]|5[1-5]|0[^0457]))-?\d{7})|(?:3(?:11|7[179])|4(?:[135]1|32)|5(?:1\d|2[37]|3[12]|51|7[^028]|9[15])|7(?:31|5[457]|69|91)|8(?:[57]1|98))-?\d{8})```

**黑名单规则:**

```\d{8,}```

**说明:**

由于正则不能很好的表达```排除```这一语义, 所以使用```白名单(更高优先级)+黑名单```的方式. 判断逻辑如下:<br>
![判断逻辑](/imgs/2021-10-15/Snipaste_2021-10-15_10-52-31.jpg)<br>
如果你没见过 **7** 位数字的验证码, 可以将黑名单规则中的 **8** 改为 **7**;<br>
如果你不希望短信中出现任何号码, 可以不使用白名单规则;<br>
如果你希望对出现在短信中的号码有更严格的限制, 请参考 [github.com/VincentSit/ChinaMobilePhoneNumberRegex](https://github.com/VincentSit/ChinaMobilePhoneNumberRegex), 本文的规则就出自那里.