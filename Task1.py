import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def Task1_fun():
    # Define the figure width and height
    fig_width = 13.45
    fig_height = 5.9


    def browse_file():
        global content
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            # File selected, open and read it
            with open(file_path, 'r') as file:
                content = file.read()

            # Call the open_file() function to process the file contents and plot
            open_file()
        else:
            message = "Where's the file?"
            messagebox.showinfo("Error", message)
            return

    def open_file():
        global content

        # Initialize two empty arrays to store the data
        x = []
        y = []

        for line in content.split('\n'):  # Split content into lines
            # Split each line into individual values based on spaces
            values = line.strip().split()

            # Ensure there are two values in each line
            if len(values) == 2:
                x.append(float(values[0]))
                y.append(float(values[1]))

        # Clear the previous figure (if any)
        for widget in frame_for_figure.winfo_children():
            widget.destroy()

        # Create a new figure
        fig, ax = plt.subplots(figsize=(fig_width, fig_height))

        # Plot the data
        ax.plot(x, y, label='Continuous Data')
        ax.scatter(x, y, label='Discrete Data', color='black', marker='o')

        # Add a horizontal line at y=0
        ax.axhline(0, color='gray', linestyle='--')

        # Draw vertical lines connecting each data point to the x-axis
        for i in range(len(x)):
            plt.plot([x[i], x[i]], [0, y[i]], 'r--')

        # Set the axis labels and title
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Signal 1')

        # Add a legend
        ax.legend()

        # Set the size of the frame to match the size of the figure
        frame_for_figure.config(width=fig_width, height=fig_height)

        # Create a canvas widget to display the figure
        canvas = FigureCanvasTkAgg(fig, master=frame_for_figure)
        canvas_widget = canvas.get_tk_widget()

        # Center the figure in the frame
        canvas_widget.pack(expand=True, fill=tk.BOTH)
        canvas.draw()


    # Create a single instance of tk.Tk()
    Task1_window = tk.Tk()
    Task1_window.title("Task 1")

    # Get the screen width and height
    screen_width = Task1_window.winfo_screenwidth()
    screen_height = Task1_window.winfo_screenheight()

    # Set the window dimensions to match the size of the figure
    Task1_window.geometry(f"{screen_width}x{screen_height}")

    frame_for_file = tk.LabelFrame(Task1_window, text="Waiting for the file..", padx=90, pady=10)
    frame_for_file.place(x=550, y=10)

    open_task_button = tk.Button(frame_for_file, text="Browse...", fg="white", bg="gray", font=("Arial", 12),
                                 command=browse_file)
    open_task_button.grid(row=0, column=0, padx=10, pady=10)

    frame_for_figure = tk.LabelFrame(Task1_window, text="The Figure", padx=0, pady=0)
    frame_for_figure.place(x=10, y=100)

    Task1_window.mainloop()