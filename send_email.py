import smtplib
from email.message import EmailMessage
import configparser

def read_config(file_path):
    """
    从 .ini 配置文件中读取邮件设置。

    Args:
        file_path (str): 配置文件的路径。

    Returns:
        dict: 配置文件中的邮件设置。
    """
    config = configparser.ConfigParser()

    # 显式指定编码格式为 utf-8
    with open(file_path, 'r', encoding='utf-8') as file:
        config.read_file(file)
    return {
        'smtp_server': config['EMAIL']['smtp_server'],
        'port': int(config['EMAIL']['port']),
        'sender': config['EMAIL']['sender'].strip('"'),
        'recipient': config['EMAIL']['recipient'].strip('"'),
        'app_password': config['EMAIL']['app_password'].strip('"'),
        'subject': config['EMAIL']['subject'].strip('"'),
        'content': config['EMAIL']['content'].strip('"'),
        'timeout': int(config['EMAIL']['timeout'])
    }

def send_email(config):
    """
    根据配置发送邮件。

    Args:
        config (dict): 从配置文件中读取的邮件设置。
    
    Returns:
        str: 邮件发送成功或失败的消息。
    """
    # 创建邮件对象
    msg = EmailMessage()
    msg['Subject'] = config['subject']
    msg['From'] = config['sender']
    msg['To'] = config['recipient']
    msg.set_content(config['content'])

    try:
        # 连接到 SMTP 服务器并发送邮件
        with smtplib.SMTP(config['smtp_server'], config['port'], timeout=config['timeout']) as server:
            server.set_debuglevel(1)  # 启用调试模式，输出详细信息
            server.starttls()  # 启用 TLS 加密
            server.login(config['sender'], config['app_password'])  # 登录邮箱
            server.send_message(msg)  # 发送邮件
        return "邮件发送成功！"
    except Exception as e:
        return f"发送邮件失败：{e}"

def start():
    config = read_config('send_email.ini')
    result = send_email(config)
    print(result)

# 读取配置并发送邮件
if __name__ == "__main__":
    # 读取配置文件
    config = read_config('send_email.ini')
    
    # 调用发送邮件函数
    result = send_email(config)
    print(result)
