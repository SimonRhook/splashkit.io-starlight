from splashkit import *

# Initialise quads with x1,y1,...,x4,y4
q1 = quad_from(400,200,300,300,300,0,200,200)
q2 = quad_from(400,210,310,300,600,300,400,390)
q3 = quad_from(200,400,300,300,300,600,400,400)
q4 = quad_from(200,390,290,300,0,300,200,210)

# Create Window
window1 = open_window("Fill Quad", 600, 600)
window2 = open_window("Fill Quad", 600, 600)
clear_screen(color_white())

fill_quad_on_window(window1, color_black(), q1)
fill_quad_on_window(window1, color_green(), q2)
fill_quad_on_window(window2, color_red(), q3)
fill_quad_on_window(window2, color_blue(), q4)

refresh_screen()
delay(5000)
close_all_windows()