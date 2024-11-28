from transitions import Machine

class DialogSystem:
    # Define all states
    states = [
        "start",  # Initial state
        "smart_planning",  # SMART Planning state
        "behavioral_menu",  # User needs suggestions
        "check_in_offer"  # User doesn't want to proceed now
    ]

    def __init__(self):
        # Initialize the state machine
        self.machine = Machine(model=self, states=DialogSystem.states, initial="start")

        # Define transitions
        self.machine.add_transition("has_idea", "start", "smart_planning")  # Transition to SMART Planning

        self.machine.add_transition("needs_suggestions", "start", "behavioral_menu")  # Transition to Behavioral Menu

        self.machine.add_transition("decline", "start", "check_in_offer")  # Transition to Check-in Offer

