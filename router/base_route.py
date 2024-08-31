from flask import Blueprint, jsonify
import time
from config.ai_key import MOONSHOT_API_KEY

# 创建一个蓝图
base_bp = Blueprint('base', __name__)

# 定义蓝图中的路由
@base_bp.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({
            "data": time.time(),
            "code": 'code',
            "message": 'message'
        })