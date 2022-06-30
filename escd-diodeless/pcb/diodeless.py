import pcbnew

OFFSET = pcbnew.wxPointMM(21.0, 50.0)
PITCH = 19.05

buttons = [
  {'id':  1, 'x': 0, 'y': 0, 'offset-x': 0,   'offset-y':  0, 'unit': 1.5, 'orientation': 0},
  {'id':  2, 'x': 0, 'y': 1, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 90},
  {'id':  3, 'x': 0, 'y': 2, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 90},
  {'id':  4, 'x': 0, 'y': 3, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 90},
                                                                          
  {'id':  5, 'x': 1, 'y': 1, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},
  {'id':  6, 'x': 1, 'y': 2, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},
  {'id':  7, 'x': 1, 'y': 3, 'offset-x': 0,   'offset-y':  0, 'unit': 1,   'orientation': 0},
                                                                          
  {'id':  8, 'x': 2, 'y': 1, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
  {'id':  9, 'x': 2, 'y': 2, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
  {'id': 10, 'x': 2, 'y': 3, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
                                                                          
  {'id': 12, 'x': 3, 'y': 1, 'offset-x': 0,   'offset-y': -PITCH / 4, 'unit': 1,   'orientation': 0},
  {'id': 13, 'x': 3, 'y': 2, 'offset-x': 0,   'offset-y': -PITCH / 4, 'unit': 1,   'orientation': 0},
  {'id': 14, 'x': 3, 'y': 3, 'offset-x': 0,   'offset-y': -PITCH / 4, 'unit': 1,   'orientation': 0},
                                                                          
  {'id': 16, 'x': 4, 'y': 1, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
  {'id': 17, 'x': 4, 'y': 2, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
  {'id': 18, 'x': 4, 'y': 3, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': 0},
                                                                          
  {'id': 20, 'x': 5, 'y': 1, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': -90},
  {'id': 21, 'x': 5, 'y': 2, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': -90},
  {'id': 22, 'x': 5, 'y': 3, 'offset-x': 0,   'offset-y': -PITCH / 8, 'unit': 1,   'orientation': -90},
                                                                          
  {'id': 11, 'x': 2, 'y': 4, 'offset-x': PITCH - 4.5,   'offset-y':  0, 'unit': 1,   'orientation': 0},
  {'id': 15, 'x': 3, 'y': 4, 'offset-x': PITCH - 4.5,   'offset-y':  0, 'unit': 1,   'orientation': 0},
  {'id': 19, 'x': 4, 'y': 4, 'offset-x': 7.39 - 0.0 + PITCH / 2, 'offset-y':  2.3, 'unit': 1,   'orientation': -102}, 
  {'id': 23, 'x': 5, 'y': 4, 'offset-x': 8.52 - 0.0 + PITCH / 2, 'offset-y': 12.6, 'unit': 1.5, 'orientation': -120},
]

# 168, 150


pcb = pcbnew.GetBoard()

# switches, diodes, LEDs
def setParts():
  for b in buttons:
    sw = pcb.FindFootprintByReference('SW%d' % b['id'])
    sw.SetPosition(OFFSET + pcbnew.wxPointMM(
      b['x'] * PITCH + b['offset-x'] + (b['unit'] - 1) * PITCH * 0.5,
      b['y'] * PITCH + b['offset-y']
    ))
    sw.SetOrientation(b['orientation'] * 10)
  
  # Elite-C
  sw4 = pcb.FindFootprintByReference('SW4')
  u1 = pcb.FindFootprintByReference('U1')
  # u1.SetPosition(sw4.GetPosition() + pcbnew.wxPointMM(PITCH / 2 - 0.5, PITCH + 4.4))
  u1.SetPosition(sw4.GetPosition() + pcbnew.wxPointMM(PITCH / 2 - 0.5, PITCH + 6.8))
  # u1.SetPosition(sw4.GetPosition() + pcbnew.wxPointMM(PITCH / 2 - 0.5, PITCH + 7.8))
  
  # Jack
  sw20 = pcb.FindFootprintByReference('SW20')
  j1 = pcb.FindFootprintByReference('J1')
  j1.SetOrientation(-900)
  j1.SetPosition(sw20.GetPosition() + pcbnew.wxPointMM(7.7, -17.83125))

def refresh():
  setParts()
  pcbnew.Refresh()

def setHoles():
  h1  = pcb.FindFootprintByReference('H1')
  h1.SetPosition(pcbnew.wxPoint(30525000, 60025000))

  h2  = pcb.FindFootprintByReference('H2')
  h2.SetPosition(pcbnew.wxPoint(30525000, 97625000))
  
  h3  = pcb.FindFootprintByReference('H3')
  h3.SetPosition(pcbnew.wxPoint(78150000, 114300000))

  h4  = pcb.FindFootprintByReference('H4')
  h4.SetPosition(pcbnew.wxPoint(88175000, 76193750))

  h5  = pcb.FindFootprintByReference('H5')
  h5.SetPosition(pcbnew.wxPoint(126339600, 127711200))

  h6  = pcb.FindFootprintByReference('H6')
  h6.SetPosition(pcbnew.wxPoint(97075000, 47955000))

  h7  = pcb.FindFootprintByReference('H7')
  h7.SetPosition(pcbnew.wxPoint(122555000, 54610000))

  h8  = pcb.FindFootprintByReference('H8')
  h8.SetPosition(pcbnew.wxPoint(14605000, 146700000))

  h9  = pcb.FindFootprintByReference('H9')
  h9.SetPosition(pcbnew.wxPoint(58865000, 133000000))

  h10  = pcb.FindFootprintByReference('H10')
  h10.SetPosition(pcbnew.wxPoint(14605000, 119300000))

  h11  = pcb.FindFootprintByReference('H11')
  h11.SetPosition(pcbnew.wxPoint(122555000, 41300000))
