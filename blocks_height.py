# this program determines the height of a block pyramid from number of blocks used

blocks = int(input("Enter the number of blocks: "))
height = 0                      # initialize the height of the pyramid
blocks_per_layer = 1            # start from the top going down 

while blocks > 0:
    
    if blocks >= blocks_per_layer:      # check if blocks left are sufficient for a new layer
        blocks -= blocks_per_layer      # remove blocks required for that layer        
        height += 1                     # increase height of the pyramid
        blocks_per_layer += 1           # increase number of blocks per layer as intended for pyramid
        
    else:
        break
    

print("The height of the pyramid:", height)
