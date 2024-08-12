def send_messages(messages, sent_messages):
    """Print a series of messages."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ['hello', 'goodbye', 'good morning', 'good night']
sent_messages = []

send_messages(messages, sent_messages)
