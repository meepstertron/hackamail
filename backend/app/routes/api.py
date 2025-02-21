from flask import Blueprint, jsonify

bp = Blueprint('api', __name__)

# Use this for general api routes (like ones that are just too small to be in their own file)
# Example:

@bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})