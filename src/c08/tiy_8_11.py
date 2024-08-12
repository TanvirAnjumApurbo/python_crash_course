def send_messages(messages, sent_messages):
    """Print a series of messages."""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ["Hello", "How are you?", "Goodbye"]
sent_messages = []

send_messages(messages[:], sent_messages)

print("Original messages list:", messages)
print("Sent messages list:", sent_messages)
