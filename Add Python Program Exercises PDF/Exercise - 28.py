# Exercise - 28: Border Drawing
def drawBorder(width: int, height: int) -> None:
    """Draws the border of a rectangle with given width and height."""
    if width < 2 or height < 2:
        print("Width and height must be at least 2.")
        return
    
    # Top border
    print("+" + "-" * (width - 2) + "+")
    
    # Middle rows
    for _ in range(height - 2):
        print("|" + " " * (width - 2) + "|")
    
    # Bottom border
    print("+" + "-" * (width - 2) + "+")

drawBorder(25,10)