from flask import Blueprint, jsonify
from config.ai_key import MOONSHOT_API_KEY

# 创建一个蓝图
chat_bp = Blueprint('chat', __name__)

# 定义蓝图中的路由
@chat_bp.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message=MOONSHOT_API_KEY)