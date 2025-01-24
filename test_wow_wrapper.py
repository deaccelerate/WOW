from wow_wrapper import WOWWrapper

def test_wow_wrapper():
    # Step 1: Initialize WOWWrapper
    print("\n--- Initializing WOWWrapper ---")
    wow = WOWWrapper("example_agent")

    # Step 2: Test core functionality
    print("\n--- Testing Core Functionality ---")
    try:
        wow.start_loop()
    except KeyboardInterrupt:
        print("\nLoop interrupted as expected.")

    # Step 3: Test perform_action
    print("\n--- Testing perform_action ---")
    response = wow.perform_action(
        connection="twitter",
        action="post-tweet",
        text="Hello from WOWWrapper test!"
    )
    print(f"perform_action response: {response}")

    # Step 4: Test redundant methods
    print("\n--- Testing Redundant Methods ---")
    wow.verbose_action("twitter", "post-tweet", text="Verbose tweet action.")
    wow.extra_methods()
    wow.redundant_setup()
    wow.wrap_start_loop()
    wow.double_wrap_start_loop()

    # Step 5: Test safe_start_loop
    print("\n--- Testing safe_start_loop ---")
    try:
        wow.safe_start_loop()
    except Exception as e:
        print(f"Error handled in safe_start_loop: {e}")

    # Step 6: Test pointless methods
    print("\n--- Testing Pointless Methods ---")
    agent_name = wow.show_agent_name()
    print(f"Agent name retrieved: {agent_name}")

if __name__ == "__main__":
    test_wow_wrapper()
