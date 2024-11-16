from flask import Flask, request, jsonify
from settings import settings_manager
from game_core import command_parser

app = Flask(__name__)

settings = settings_manager.load_settings()

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.json.get('command')
    response = command_parser.parse_command(command, settings)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)