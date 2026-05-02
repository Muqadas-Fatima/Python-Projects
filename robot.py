import tkinter as tk

class Aroboy:
    def __init__(self, grid_size=5, start_position=(0, 0)):
        self.grid_size = grid_size
        self.position = start_position
        self.grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # 0 for empty space
        self.grid[start_position[0]][start_position[1]] = 1  # 1 for robot's position
        
        # Placing obstacles (1 represents an obstacle)
        self.place_obstacles()

    def place_obstacles(self):
        obstacles = [(1, 2), (2, 2), (3, 3), (4, 1)]  # Sample obstacle positions
        for obs in obstacles:
            self.grid[obs[0]][obs[1]] = -1  # -1 for obstacle

    def move_up(self):
        x, y = self.position
        if x > 0 and self.grid[x-1][y] != -1:  # Check if the move is valid
            self.grid[x][y] = 0  # Clear the current position
            self.position = (x-1, y)
            self.grid[x-1][y] = 1  # Move the robot up

    def move_down(self):
        x, y = self.position
        if x < self.grid_size - 1 and self.grid[x+1][y] != -1:
            self.grid[x][y] = 0
            self.position = (x+1, y)
            self.grid[x+1][y] = 1  # Move the robot down

    def move_left(self):
        x, y = self.position
        if y > 0 and self.grid[x][y-1] != -1:
            self.grid[x][y] = 0
            self.position = (x, y-1)
            self.grid[x][y-1] = 1  # Move the robot left

    def move_right(self):
        x, y = self.position
        if y < self.grid_size - 1 and self.grid[x][y+1] != -1:
            self.grid[x][y] = 0
            self.position = (x, y+1)
            self.grid[x][y+1] = 1  # Move the robot right

class AroboyGameGUI:
    def __init__(self, master, grid_size=5):
        self.master = master
        self.master.title("Aroboy Game")
        self.master.geometry("300x350")  # Set a fixed size for the window

        self.grid_size = grid_size
        self.aroboy = Aroboy(grid_size=grid_size)

        # Create the canvas to draw the grid
        self.canvas = tk.Canvas(self.master, width=250, height=250)
        self.canvas.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create buttons for moving the robot with padding
        self.btn_up = tk.Button(self.master, text="Up", command=self.move_up, width=10)
        self.btn_up.grid(row=1, column=1, pady=5)

        self.btn_left = tk.Button(self.master, text="Left", command=self.move_left, width=10)
        self.btn_left.grid(row=2, column=0, padx=5, pady=5)

        self.btn_right = tk.Button(self.master, text="Right", command=self.move_right, width=10)
        self.btn_right.grid(row=2, column=2, padx=5, pady=5)

        self.btn_down = tk.Button(self.master, text="Down", command=self.move_down, width=10)
        self.btn_down.grid(row=3, column=1, pady=5)

        self.update_grid()

    def move_up(self):
        self.aroboy.move_up()
        self.update_grid()

    def move_down(self):
        self.aroboy.move_down()
        self.update_grid()

    def move_left(self):
        self.aroboy.move_left()
        self.update_grid()

    def move_right(self):
        self.aroboy.move_right()
        self.update_grid()

    def update_grid(self):
        self.canvas.delete("all")  # Clear the canvas

        # Draw the grid with better padding and layout
        cell_size = 50  # Size of each grid cell
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x0, y0 = j * cell_size, i * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                color = "white"  # Default color for empty space

                if self.aroboy.grid[i][j] == -1:
                    color = "black"  # Color for obstacles
                elif self.aroboy.grid[i][j] == 1:
                    color = "green"  # Color for the robot

                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=f"({i},{j})", fill="black")

# Create the Tkinter window and start the game
if __name__ == "__main__":
    root = tk.Tk()
    game_gui = AroboyGameGUI(root)
    root.mainloop()
