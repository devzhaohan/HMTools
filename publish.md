
# 发布python程序包到pypi
使用github action 当创建一个release的时候，github action会自动发布到pypi
1. 查看当前分支状态
```shell
# 查看当前分支状态
git status
# 如果有未提交的更改，需要先提交这些更改才能创建发布版本。
```
2. 提交所有的更改
```shell
git commit -m 'chore: update'
```

3. 发布release
```shell
# 切换到主分支
git checkout main

#创建一个新的标记（Tag）作为该发布版本的引用点
git tag -a v1.0.0 -m "Version 1.0.0"
#其中v1.0.0表示版本号，-m参数指定了标记信息

# 将标记推送到远程仓库
git push origin --tags
```

4. 成功创建了一个新的发布版本


