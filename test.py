from pyray import *
init_window(800, 450, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_text("Hello world", 190, 200, 20, BLUE)
    draw_text("BYE world", 200, 300, 15, GREEN)
    # draw_cube( vector3, 200, 200, 200, WHITE)
    end_drawing()
    draw_line(0,0,50,400,YELLOW)
    draw_rectangle(0, 300, 800, 150, WHITE)
close_window()
