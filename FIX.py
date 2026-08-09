import time
import customtkinter
import subprocess
import tkinter as tk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

def start_button_click():
    slabel.configure(text="Status: Starting")
    app.update()
    time.sleep(2)
    run_fix()

def quit_button_click():
    app.quit()

def run_fix():
    slabel.configure(text="Status: Running Fix")
    app.update()
    
    # Create a Text widget for console output
    console_output = tk.Text(app, height=10, width=40, wrap=tk.WORD)
    console_output.pack(pady=10, padx=10)
    
    try:
        # Define the commands to run
        commands = [
            "Del /S /F /Q %temp%",
            "Del /S /F /Q %Windir%\\Temp",
            "Del /S /F /Q C:\\WINDOWS\\Prefetch",
            "ipconfig /release",
            "ipconfig /flushdns",
            "ipconfig /renew"
        ]
        
        for command in commands:
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            for line in process.stdout:
                console_output.insert(tk.END, line)
                console_output.see(tk.END)  # Auto-scroll to the end
                app.update()
        
        slabel.configure(text="Status: Finished")
        app.update()
        start_button.configure(text="Quit", font=("Helvetica", 30), command=quit_button_click)
        app.update()
    except Exception as e:
        console_output.insert(tk.END, str(e))
        slabel.configure(text="Status: Error")
        app.update()

app = customtkinter.CTk()
app.title("PRO | Lag Remover")
app.iconbitmap('lag.ico')
# Set window dimensions and position
window_width = 400
window_height = 500  # Increased height for console output
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create a label
label = customtkinter.CTkLabel(app, text="Remove Lag..!", font=("Helvetica", 30))
label.pack(pady=20)

start_button = customtkinter.CTkButton(app, text="Fix", font=("Helvetica", 30), command=start_button_click)
start_button.pack(pady=20)

slabel = customtkinter.CTkLabel(app, text="", font=("Helvetica", 20))
slabel.pack(pady=50)

app.mainloop()
