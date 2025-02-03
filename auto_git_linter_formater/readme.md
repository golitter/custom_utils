# `pre-commit`

[python的pre-commit库的使用-CSDN博客](https://golemon.blog.csdn.net/article/details/145433704?spm=1001.2014.3001.5502)

```shell
pip install pre-commit
```

配置完成之后：

```shell
pre-commit install
```

# `ruff`

[python的ruff简单使用-CSDN博客](https://golemon.blog.csdn.net/article/details/145433813?spm=1001.2014.3001.5502)

```shell
conda install -c conda-forge ruff     

# pip
pip install ruff
```

运行检查：

```shell
ruff check .
```

运行检查并自动修复：

```shell
ruff check . --fix
```

代码格式化：

```shell
ruff format .
```

