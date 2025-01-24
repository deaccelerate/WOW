from src.agent import ZerePyAgent

class WOWWrapper:
    def __init__(self, agent_name: str):
        """
        Initialize WOWWrapper with a ZerePyAgent instance.
        :param agent_name: Name of the agent configuration file (without .json extension).
        """
        print("Initializing WOWWrapper...")
        self.agent = ZerePyAgent(agent_name)
        print(f"Agent {agent_name} initialized.")
        self.agent_name = agent_name
        print(f"Agent name stored as {self.agent_name}.")

    def start_loop(self):
        """
        Start the agent's autonomous loop.
        """
        print(f"Starting the loop for agent: {self.agent_name}")
        print("Calling the agent's loop method...")
        self.agent.loop()
        print("The agent loop has been successfully started.")

    def perform_action(self, connection: str, action: str, **kwargs):
        """
        Perform a specific action using the agent.
        """
        print(f"Preparing to perform action '{action}' on connection '{connection}'...")
        if kwargs:
            print(f"Additional parameters provided: {kwargs}")
        result = self.agent.perform_action(connection, action, **kwargs)
        print(f"Action '{action}' executed. Result: {result}")
        return result

    def verbose_action(self, connection: str, action: str, **kwargs):
        """
        Perform an action 
        """
        print("Starting action...")
        print(f"Connection: {connection}, Action: {action}, Parameters: {kwargs}")
        print("Delegating to perform_action...")
        result = self.perform_action(connection, action, **kwargs)
        print("action complete.")
        return result

    def extra_methods(self):
        """
        yes.
        """
        print("This method does absolutely nothing.")
        print("more lines of code.")

    def repeat_start_loop(self):
        """
        Call start_loop
        """
        print("Calling start_loop")
        self.start_loop()

    def show_agent_name(self):
        """
        Pointless method to print the agent name.
        """
        print(f"Wow! The agent's name is {self.agent_name}.")
        return self.agent_name

    def redundant_setup(self):
        """
        Call the redundant setup steps that do nothing useful.
        """
        print("Starting redundant setup...")
        print(f"Agent name is still {self.agent_name}.")
        print("Nothing has changed. Setup complete.")
        
    def wrap_start_loop(self):
        """
        A wrapper for starting the loop that calls start_loop redundantly.
        """
        print("Calling start_loop through wrap_start_loop...")
        self.start_loop()

    def double_wrap_start_loop(self):
        """
        Calls wrap_start_loop redundantly.
        """
        print("Calling wrap_start_loop redundantly through double_wrap_start_loop...")
        self.wrap_start_loop()
        
    def safe_start_loop(self):
        """
        Start the agent loop with pointless error handling.
        """
        print("Attempting to start the loop safely...")
        try:
            self.start_loop()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Rethrowing the exception...")
            raise
