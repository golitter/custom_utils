- `Console()`类：可以自行设置是否打印，如果是则打印信息；否则则不打印信息。

  update（2025年1月24日）：添加windows系统上调用文件资源管理器打开目录。

- `Logger()`类：使用`logging`库对日志功能进行封装。

- `send_email.py`文件，使用gmail邮箱自动发送邮件，使用ini配置文件管理配置信息。

- `pre-commit`结合`ruff`的智能配置链。

- `pdbDebug.sh`：使用pdb进行调试备份调试内容及所得调试信息到一个文件内