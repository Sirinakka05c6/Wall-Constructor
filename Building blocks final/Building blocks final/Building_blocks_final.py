import tkinter as tk
from tkinter import messagebox

class WallConstructorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wall Constructor")
        
        self.breadth_label = tk.Label(root, text="Breadth:")
        self.breadth_label.grid(row=0, column=0)
        self.breadth_entry = tk.Entry(root)
        self.breadth_entry.grid(row=0, column=1)
        
        self.height_label = tk.Label(root, text="Height:")
        self.height_label.grid(row=1, column=0)
        self.height_entry = tk.Entry(root)
        self.height_entry.grid(row=1, column=1)
        
        self.brick_sizes = ["Type1", "Type2", "Type3"]
        self.brick_sizes_dimension=[]
        self.brick_sizes_height=10
        self.color_labels = []
        self.quantity_labels = []
        self.quantity_entries = []
        self.color_entries=[]
        
        for idx, brick_size in enumerate(self.brick_sizes):
            label = tk.Label(root, text=f"{brick_size} Brick Color:")
            label.grid(row=idx+2, column=0)
            self.color_labels.append(label)
            
            label = tk.Label(root, text=f"size of {brick_size} Bricks:")
            label.grid(row=idx+2, column=2)
            self.quantity_labels.append(label)
            
            entry = tk.Entry(root)
            entry.grid(row=idx+2, column=3)
            self.quantity_entries.append(entry)
            self.brick_sizes_dimension.append(entry)

            entry = tk.Entry(root)
            entry.grid(row=idx+2, column=1)
            self.color_entries.append(entry)
        
        self.construct_button = tk.Button(root, text="Construct Wall", command=self.construct_wall)
        self.construct_button.grid(row=len(self.brick_sizes)+2, column=1)
          
    def construct_wall(self):
        try:
            breadth = int(self.breadth_entry.get())
            height = int(self.height_entry.get())
            
            brick_sizes_colors = []
            brick_quantities = []
            for idx, brick_size in enumerate(self.brick_sizes):
                color = str(self.color_entries[idx].get())
                brickdimension=int(self.brick_sizes_dimension[idx].get())
                quantity = int(self.quantity_entries[idx].get())
                if quantity > 0:
                    brick_sizes_colors.append((brick_size, color,brickdimension,quantity))
                    brick_quantities.append(quantity)
            
            if len(brick_sizes_colors) == 0:
                messagebox.showwarning("No Bricks", "Please enter quantities for at least one brick size.")
                return
            
            print(f"Wall Dimensions: {breadth} x {height}")
               
            self.construct_wall_visualization(breadth, height, brick_sizes_colors, brick_quantities)

            messagebox.showinfo("Success", "Wall construction details printed to the console.")
        except ValueError as ex:
            messagebox.showerror("Invalid Input", "Please enter valid numerical values for Breadth, Height, and Quantities.")

    
    def construct_wall_visualization(self, breadth, height, brick_sizes_colors, brick_quantities):
        wall = [[' ' for _ in range(breadth)] for _ in range(height)]
        row_counter = 0
        col_counter = 0
        
         # Create the canvas to draw the wall
        window = tk.Toplevel(root)
        canvas = tk.Canvas(window, width=breadth*10, height=height*10, bg="white")
        canvas.pack()

        # Create the wall using the provided bricks
        brick_index = 0
        temp_brickData=brick_sizes_colors
        current_y=0
        while (1>0):
            current_y=current_y+self.brick_sizes_height
            current_x=0
            temp_current_x=current_x
            temp_current_y=current_y
            while (1>0):
                    brick_size_color=temp_brickData[brick_index]
                    brick_color = brick_size_color[1]
                    brick_width=brick_size_color[2]
                    brick_quantity=brick_size_color[3]
                    brick_height=self.brick_sizes_height
                    
                    current_x1=temp_current_x+brick_width
                    current_y1=temp_current_y+brick_height
                    if (current_x1>=breadth):
                        break
                    canvas.create_rectangle(temp_current_x, temp_current_y, current_x1, current_y1, fill=brick_color)
                    print(str(temp_current_x)+","+str(temp_current_y)+","+str(current_x1)+","+str(current_y1))
                    temp_current_x=current_x1
                    temp_current_y=current_y1-brick_height
                    brick_index = (brick_index + 1) % 3
                   
            if (current_y>=height):
                break


root = tk.Tk()
app = WallConstructorApp(root)
root.mainloop()