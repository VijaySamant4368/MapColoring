from graphs import *

m=punjab
mapVal=punjabValues

matrix = []                                                                                    #Making the matrix as lower triangle
for i in range(len(m)):
    matrix.append([])
    for j in range(len(m)):
        if j <= i:
            matrix[i].append(m[i][j])

colorcode = {0:"Not Yet Assigned",1: "RED", 2: "GREEN", 3: "BLUE",4:"YELLOW"}                                                                                                                                                           #,5:"PINK",6:"MAGENTA",7:"CYAN",8:"ORANGE",9:"BROWN",10:"PURPLE"}                   #wil use at last
colors = set([1])                                                                       #total colors

vertex_color = {"vertex1": 1}                                                   #Making a dict with vertex and their color
check = {"vertex1": [1]}                                                            #dict with vertex and its adjacent colors

for i in range(len(matrix) - 1):
    vertex = "vertex" + str(i + 2)
    vertex_color[vertex] = 0                                             #Filling the rest of dict
    check["vertex" + str(i + 2)] = []

complete=False

for vertex_n in range(len(matrix)):                                         #Row
    for edge in range(len(matrix[vertex_n])):                           #Column
        complete=False
        new_color = True                                                            #Is a new color required?

        
        if matrix[vertex_n][edge]:                                                #If they share edges
            check["vertex" + str(vertex_n + 1)].append(vertex_color["vertex" + str(edge + 1)])                  #Add unavailable colors to its dict

            
            for color in colors:
                if color not in check["vertex" + str(vertex_n + 1)]:                                        #It will look from start for a available color
                    vertex_color["vertex" + str(vertex_n + 1)] = color                                    #And if a color is available for it, it changes color
                    new_color = False                                                                                       #Now it doesn't need a new color for itself
                    break

                
            if new_color:                                                            #If all the current colors are available
                new_color_code = max(colors) + 1
                colors.add(new_color_code)
                vertex_color["vertex" + str(vertex_n + 1)] = new_color_code

    complete=True
    if complete:
        if vertex_color["vertex" + str(vertex_n + 1)] == 0:
            vertex_color["vertex" + str(vertex_n + 1)] = 1
            complete=False
            


print("Vertex colors:")                                           #Result     :)
for vertex, color_code in vertex_color.items():
    print(mapVal[vertex], ":", colorcode[color_code])

print("\nChromatic Number=",len(colors))
