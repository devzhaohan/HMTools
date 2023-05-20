

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

#删除dist目录中老版本号的文件
rm -rf dist/*
``` 

``` bash
# 打包
python -m build
# venv/bin/python -m build
``` 

``` bash
# 上传
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
# venv/bin/python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/* 
# 当提示Enter your username: 时，自动输入pypi的账号名

# 当提示Enter your password: 时，输入pypi的账号密码

``` 

