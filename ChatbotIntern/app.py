from flask import Flask, render_template, request, jsonify
from chatbot import InternshipChatbot
import os

app = Flask(__name__)
chatbot = InternshipChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        if not data:
            return jsonify({
                'response': 'Invalid request format.',
                'intent': 'error'
            }), 400
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'response': 'Please enter a message.',
                'intent': 'error'
            }), 400
        
        response = chatbot.get_response(user_message)
        return jsonify(response)
    
    except Exception as e:
        return jsonify({
            'response': 'I apologize, but I encountered an error. Please try again.',
            'intent': 'error',
            'error': str(e)
        }), 500

@app.route('/reset', methods=['POST'])
def reset_conversation():
    chatbot.reset_context()
    return jsonify({'status': 'success', 'message': 'Conversation reset'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
