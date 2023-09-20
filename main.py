import PySimpleGUI as sg

def convert_pos_to_pixel(cell):
    tl = cell[0] * CELL_SIZE, cell[1] * CELL_SIZE
    br = tl[0] + CELL_SIZE, tl[1] + CELL_SIZE
    return tl, br

FIELD_SIZE = 400
CELL_NUM = 10
CELL_SIZE = FIELD_SIZE / CELL_NUM


apple_pos = (0, 0)

sg.theme('Green')
field = sg.Graph(
    canvas_size = (FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left = (0, 0),
    graph_top_right = (FIELD_SIZE, FIELD_SIZE),
    background_color = 'black',
    pad = 10
)

layout = [[field]]

window = sg.Window('Snake', layout, return_keyboard_events = True)

while True:
    event, values = window.read(timeout = 10)

    if event == sg.WIN_CLOSED: break
    if event == 'Left:37': print('left')
    if event == 'Up:38': print('up')
    if event == 'Right:39': print('right')
    if event == 'Down:40': print('down')

    tl, br = convert_pos_to_pixel(apple_pos)
    field.DrawRectangle(tl, br, 'red')


window.close()