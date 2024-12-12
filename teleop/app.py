from flask import Flask, request, jsonify
import teleop_hand  # Import your script

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run_teleop_hand():
    # Call the main function in your script
    # Adjust this based on how your script is structured
    result = teleop_hand.main()
    return jsonify({'status': 'Teleoperation started', 'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
