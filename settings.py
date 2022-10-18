import logging
import os

mysql_host = os.getenv('MYSQL_HOST', 'localhost')
mysql_user = os.getenv('MYSQL_USER', 'word')
mysql_password = os.getenv('MYSQL_PASSWORD', '')
mysql_db_name = "calendar"
mysql_pool_name = "calendar"
mysql_pool_size = int(os.getenv('MYSQL_POOL_SIZE', 10))

log_format = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
log_level = logging.INFO
is_dev = os.getenv('IS_DEV', 1)
if int(is_dev) == 1:
    log_level = logging.DEBUG
logging.basicConfig(level=log_level, format=log_format)

pregnancy_period_week = 40
days_of_week = 7
pregnancy_period = days_of_week * pregnancy_period_week
pregnancy_examination = {
    "8": "全套抽血，艾滋，乙肝，梅毒，肝胆 B 超(空腹); NT，预约四维彩超，泌尿 B 超，心电图",
    "16": "唐氏筛查，无创 DNA产前诊断咨询",
    "20": "常规 B 超",
    "24": "糖耐量，四维 B 超，艾滋，乙肝，梅毒(空腹)",
    "28": "脐血流，四维彩超",
    "30": "常规 B 超",
    "32": "肝功和胆汁酸，血尿常规，脐血流(空腹)",
    "34": "胎监，脐血流，心电图",
    "36": "胎监，常规 B 超",
    "37": "胎监，血尿常规，艾滋，乙肝，梅毒，B 超，羊水监测",
    "38": "胎监，常规 B 超",
    "39": "胎监，常规 B 超，羊水监测",
    "40": "胎监，常规 B 超",
}
