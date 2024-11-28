from flask import Flask, render_template, request, jsonify
import csv
from states import DialogSystem

dialog = DialogSystem()
app = Flask(__name__)


@app.route('/')
def index():
    # Serve the HTML page
    return render_template('index.html') # Renders your UI

@app.route('/respond', methods=['POST'])
def respond():
    user_input = request.json.get('message')
    response = "I didn't understand that. Could you please rephrase?"  # Default fallback response


    # Handle transitions based on the current state and user input
    if dialog.state == "start":
        if user_input in ["yes", "i have an idea"]:  # Transition to SMART Planning
            dialog.has_idea()
            response = "Great! Let’s create a SMART behavioral plan. What’s your idea?"

        elif user_input in ["not sure", "maybe"]:  # Transition to Behavioral Menu
            dialog.needs_suggestions()
            response = "Here are some ideas to consider: [Behavioral Menu]"

        elif user_input in ["no", "not now"]:  # Transition to Check-in Offer
            dialog.decline()
            response = "That’s fine. Would you like me to check in with you later?"

        else:
            response = "I'm sorry, I didn't understand that. Please respond with Yes, No, or Not Sure."

    elif dialog.state == "smart_planning":
        # Example: Handle input for SMART Planning
        response = "What is your SMART plan? (e.g., What? When? Where?)"

    elif dialog.state == "behavioral_menu":
        # Example: Provide suggestions for Behavioral Menu
        response = "Here are some suggestions: Take a walk, drink more water, or meditate for 5 minutes."

    elif dialog.state == "check_in_offer":
        # Example: Handle response in Check-in Offer state
        response = "I’ll check in with you next time. Take care!"

    return jsonify({"response": response})

@app.route('/save', methods=['POST'])
def save_user_data():
    data = request.json  # Assumes JSON payload
    with open('data/users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['response']])
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)



