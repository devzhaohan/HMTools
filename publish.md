

# 发布python程序包到pypi
使用github action 当创建一个release的时候，github action会自动发布到pypi

1. 更改[pyproject.toml](pyproject.toml)中的版本号
``` bash
# 读取将pyproject.toml中的版本号，赋值给version变量，用于后续命令中，例如version = "0.0.19"，修改为version = "0.0.20"，这里的version = "0.0.19"，就是读取的pyproject.toml中的版本号，赋值给version变量，用于后续命令中
version=$(cat pyproject.toml | grep version | awk -F '"' '{print $2}')
echo $version

# 将version变量中的版本号，进行+1操作，例如version = "0.0.19"，修改为version = "0.0.20"
version=$(echo $version | awk -F '.' '{print $1"."$2"."$3+1}')
echo $version

# 将新的版本号，写入pyproject.toml中
sed -i "" "s/version = .*/version = \"$version\"/g" pyproject.toml

echo "new version: $version"
``` 

2. 查看当前分支状态
```shell
# 查看当前分支状态
git status
# 如果有未提交的更改，需要先提交这些更改才能创建发布版本。
```
2. 提交所有的更改
```shell
git commit -m 'chore: update'
```

3. 切换到主分支
```text
git checkout main
```

4. 创建新标记
```shell
# 创建一个新的标记（Tag）作为该发布版本的引用点
git tag -a v1.0.240110_1 -m "Version 1.0.240110_1"
# 其中v1.0.0表示版本号，-m参数指定了标记信息
```

5. 推送到github
```shell
# 将标记推送到远程仓库
git push origin --tags
```

6. 进入github，发布新的release
```shell
 open https://github.com/devzhaohan/HMTools 
```



