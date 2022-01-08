


def gameWinner(colors):

    if len(set(colors)) == 1:
        
        if colors[0] == 'w':
            return "wendy"
        else:
            return "bob"
    
    w, b = colors.find('www'), colors.find('bbb')
    
    while b != -1 and w != -1:
        colors = colors[:w+1] + colors[w+2:] 
        colors = colors[:b+1] + colors[b+2:] 
    
        w, b = colors.find('www'), colors.find('bbb')

    if w == -1:
        return "bob"

    if b == -1:
        return  "wendy"
