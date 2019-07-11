# EmailTool
这个脚本的目的就是给各个参议员发邮件 
# 杜绝HR 1044!!!!!!!
# 国人要团结！！！

Prerequisite: 

首先先安装
# python3.5

这个脚本暂时只支持gmail发送！如果不用gmail的小伙伴麻烦注册一下

首先要去Google account里面设置一下less secure 

要把这个给disable才可以用
https://myaccount.google.com/u/3/lesssecureapps



run
```
python3 sendEmail.py
```

如果说emailList里面有漏掉什么的某个参议员的邮件的话
parse_last_name.py这个python文件可以帮你把议员的名字生成一个字典的数据结构的
```
"{"<last_name>", "<email>"}
```

在directories.txt底下,
然后复制粘贴到emailList.py　里面进行发送

## 想改模板的各位可以在Message.txt里面改

注意不要把第一行的{} 和最后一行的{}删掉了。


新的白宫请愿签名链接：
Do not pass BIlls S.386 or H.R.1044! Do not pass Bills S.386 or H.R.1044 for U.S. worker and racial diversity!!
https://petitions.whitehouse.gov/petition/do-not-pass-bills-s386-or-hr1044-do-not-pass-bills-s386-or-hr1044-us-worker-and-racial-diversity 19
