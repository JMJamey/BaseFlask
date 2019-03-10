from flask import Flask
from .models import db

# 新建app对象
app = Flask(__name__)
# 加载配置信息，其中有数据库的配置信息，包含在SQLALCHEMY_DATABASE_URI中
app.config.from_object('config')

# 初始化db,并创建models中定义的表格
with app.app_context(): # 添加这一句，否则会报数据库找不到application和context错误
    db.init_app(app) # 初始化db
    db.create_all() # 创建所有未创建的table


# 注册蓝图
from web.users import users as user_blueprint
app.register_blueprint(user_blueprint)

from web.index import index as index_blueprint
app.register_blueprint(index_blueprint)
