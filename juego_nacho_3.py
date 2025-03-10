import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de la Pelotita")

# Dimensiones del canvas
canvas_width = 400
canvas_height = 300

# Crear el canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Dibujar la raqueta
paddle_width = 100
paddle_height = 10
paddle_x = canvas_width // 2 - paddle_width // 2
paddle_y = canvas_height - paddle_height - 30
paddle = canvas.create_rectangle(paddle_x, paddle_y, paddle_x + paddle_width, paddle_y + paddle_height, fill="blue")

# Dibujar la pelota
ball_diameter = 20
ball_x = canvas_width // 2 - ball_diameter // 2
ball_y = canvas_height // 2 - ball_diameter // 2
ball = canvas.create_oval(ball_x, ball_y, ball_x + ball_diameter, ball_y + ball_diameter, fill="red")

# Velocidad de la pelota
ball_dx = 3
ball_dy = -3

# Mover la pelota
def move_ball():
    global ball_dx, ball_dy
    canvas.move(ball, ball_dx, ball_dy)
    ball_coords = canvas.coords(ball)
    
    # Rebotar contra las paredes
    if ball_coords[0] <= 0 or ball_coords[2] >= canvas_width:
        ball_dx = -ball_dx
    if ball_coords[1] <= 0:
        ball_dy = -ball_dy
    
    # Rebotar contra la raqueta
    paddle_coords = canvas.coords(paddle)
    if (ball_coords[3] >= paddle_coords[1] and
        ball_coords[2] >= paddle_coords[0] and
        ball_coords[0] <= paddle_coords[2]):
        ball_dy = -ball_dy
    
    # Fin del juego si la pelota cae
    if ball_coords[3] > canvas_height:
        canvas.create_text(canvas_width // 2, canvas_height // 2, text="Game Over", font=("Arial", 24), fill="black")
        return
    
    root.after(20, move_ball)

# Mover la raqueta
def move_paddle(event):
    x = event.x
    if x < canvas_width - paddle_width and x > 0:
        canvas.coords(paddle, x, paddle_y, x + paddle_width, paddle_y + paddle_height)

# Asignar el control del ratón a la raqueta
canvas.bind("<Motion>", move_paddle)

# Iniciar el movimiento de la pelota
move_ball()

# Iniciar el loop principal de la ventana
root.mainloop()
