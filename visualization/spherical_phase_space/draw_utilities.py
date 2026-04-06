# notas iniciais

# to draw all the points that constitute the sphere
def draw_sphere(points_sphere):
    strokeWeight(1.5)
    stroke(0)
    for i in range(len(points_sphere)):
        point(points_sphere[i][0], 
              points_sphere[i][1], 
              points_sphere[i][2])
 
               
# to draw the reference lines and points;
def draw_references(r, f_phases, pitches_cartesian, pitches_names):
    # to draw reference lines
    strokeWeight(1)
    stroke(0)
    line(0, 0, r - 25, 
         0, 0, r + 50)
    line(0, 0, -1 * (r - 25), 
         0, 0, -1 * (r + 50))
    line(r - 25, 0, 0, 
         r + 50, 0, 0)
    line(-1 * (r - 25), 0, 0, 
         -1 * (r + 50), 0, 0)
    line(0, r - 25, 0, 
         0, r + 50, 0)    
    line(0, -1 * (r - 25), 0, 0, 
         -1 * (r + 50), 0)
    # to draw reference text
    textSize(r/30)
    textAlign(CENTER)
    fill(0)
    text("phi" + f_phases[17] + " -pi", 
         0, -10, r + 55)
    text("phi" + f_phases[17] + " pi", 
         0, 10, -1 * (r + 55))
    text("phi" + f_phases[15] + " 0", 
         -1 * (r + 55), -10, 0)
    text("phi" + f_phases[15] + " pi/-pi", 
         r + 60, -10, 0)
    text("phi" + f_phases[15] + " -pi/2", 
         0, r + 70, 0)
    text("phi" + f_phases[15] + " pi/2", 
         0, -1 * (r + 70), 0)
    # to draw reference pitches
    textSize(r/24)
    textAlign(CENTER)
    fill(0)
    for i in range(len(pitches_cartesian)):
        text(pitches_names[i], 
             pitches_cartesian[i][0], 
             pitches_cartesian[i][1], 
             pitches_cartesian[i][2])
    

# to draw the cluster centers
def draw_cluster_centers(r, cluster_center, cluster_letters, color_list, point_counter):
    strokeWeight(r/40)
    textSize(r/20)
    textAlign(CENTER)
    for i in range(len(cluster_center)):
        stroke(color_list[i][0], 
               color_list[i][1], 
               color_list[i][2])
        fill(color_list[i][0], 
             color_list[i][1], 
             color_list[i][2])
        point(cluster_center[i][0], 
              cluster_center[i][1], 
              cluster_center[i][2])
        if point_counter == 0:
            text("cluster center " + cluster_letters[i], 
                 cluster_center[i][0], 
                 cluster_center[i][1] + (r/13), 
                 cluster_center[i][2])
            

# to draw numbered points with the respective cluster color;
def draw_points(r, points_cartesian, color_list, labels_list, point_counter):
    textSize(r/12)
    textAlign(CENTER)
    if point_counter <= len(points_cartesian):
        for i in range(len(points_cartesian) - (len(points_cartesian) - point_counter)):
            fill(color_list[labels_list[i]][0], 
                 color_list[labels_list[i]][1], 
                 color_list[labels_list[i]][2])
            text(str(i+1), 
                 points_cartesian[i][0], 
                 points_cartesian[i][1] - r/40, 
                 points_cartesian[i][2])
            strokeWeight(r/85)
            stroke(color_list[labels_list[i]][0], 
                   color_list[labels_list[i]][1], 
                   color_list[labels_list[i]][2])
            point(points_cartesian[i][0], 
                  points_cartesian[i][1], 
                  points_cartesian[i][2])
    else:
        for i in range(len(points_cartesian)):
            fill(color_list[labels_list[i]][0], 
                 color_list[labels_list[i]][1], 
                 color_list[labels_list[i]][2])
            text(str(i+1), 
                 points_cartesian[i][0], 
                 points_cartesian[i][1] - r/40, 
                 points_cartesian[i][2])
            strokeWeight(r/85)
            stroke(color_list[labels_list[i]][0], 
                   color_list[labels_list[i]][1], 
                   color_list[labels_list[i]][2])
            point(points_cartesian[i][0], 
                  points_cartesian[i][1], 
                  points_cartesian[i][2])


# to draw numbered points with their respective cluster color and lines between points;
def draw_paths(r, points_cartesian, color_list, labels_list, point_counter):
    textSize(r/12)
    textAlign(CENTER)
    if point_counter <= len(points_cartesian):
        for i in range(len(points_cartesian) - (len(points_cartesian) - point_counter)):
            fill(color_list[labels_list[i]][0], 
                 color_list[labels_list[i]][1], 
                 color_list[labels_list[i]][2])
            text(str(i+1), 
                 points_cartesian[i][0], 
                 points_cartesian[i][1] - r/40, 
                 points_cartesian[i][2])
            strokeWeight(r/85)
            stroke(color_list[labels_list[i]][0], 
                   color_list[labels_list[i]][1], 
                   color_list[labels_list[i]][2])
            point(points_cartesian[i][0], 
                  points_cartesian[i][1], 
                  points_cartesian[i][2])
            if i >= 1:
                strokeWeight(1)
                line(points_cartesian[i - 1][0], 
                     points_cartesian[i - 1][1], 
                     points_cartesian[i - 1][2], 
                     points_cartesian[i][0], 
                     points_cartesian[i][1], 
                     points_cartesian[i][2])
    else:
        for i in range(len(points_cartesian)):
            fill(color_list[labels_list[i]][0], 
                 color_list[labels_list[i]][1], 
                 color_list[labels_list[i]][2])
            text(str(i+1), 
                 points_cartesian[i][0], 
                 points_cartesian[i][1] - r/40, 
                 points_cartesian[i][2])
            strokeWeight(r/85)
            stroke(color_list[labels_list[i]][0], 
                   color_list[labels_list[i]][1], 
                   color_list[labels_list[i]][2])
            point(points_cartesian[i][0], 
                  points_cartesian[i][1], 
                  points_cartesian[i][2])
            if i >= 1:
                strokeWeight(1)
                line(points_cartesian[i - 1][0], 
                     points_cartesian[i - 1][1], 
                     points_cartesian[i - 1][2], 
                     points_cartesian[i][0], 
                     points_cartesian[i][1], 
                     points_cartesian[i][2])
                
                
# to draw only the last n points and lines in the spherical space
def draw_n_paths(r, n, points_rads, points_cartesian, color_list, labels_list, point_counter):
    textAlign(LEFT)
    textSize(r/12)
    if 0 < point_counter <= n:
        for i in range(point_counter):
            fill(color_list[labels_list[i]][0], 
                 color_list[labels_list[i]][1], 
                 color_list[labels_list[i]][2])
            text(str(i+1), 
                 points_cartesian[i][0], 
                 points_cartesian[i][1] - r/40, 
                 points_cartesian[i][2])
            
            strokeWeight(r/85)
            stroke(color_list[labels_list[i]][0], 
                   color_list[labels_list[i]][1], 
                   color_list[labels_list[i]][2])
            point(points_cartesian[i][0], 
                  points_cartesian[i][1], 
                  points_cartesian[i][2])
            if i >= 1:
                strokeWeight(1)
                line(points_cartesian[i - 1][0], 
                     points_cartesian[i - 1][1], 
                     points_cartesian[i - 1][2], 
                     points_cartesian[i][0], 
                     points_cartesian[i][1], 
                     points_cartesian[i][2])
    elif n < point_counter <= len(points_cartesian):
        for i in range(n):
            fill(color_list[labels_list[point_counter - 1 - i]][0], 
                 color_list[labels_list[point_counter - 1 - i]][1], 
                 color_list[labels_list[point_counter - 1 - i]][2])
            text(str(point_counter - i), 
                 points_cartesian[point_counter - 1 - i][0], 
                 points_cartesian[point_counter - 1 - i][1] - r/40, 
                 points_cartesian[point_counter - 1 - i][2])
            strokeWeight(r/85)
            stroke(color_list[labels_list[point_counter - 1 - i]][0], 
                   color_list[labels_list[point_counter - 1 - i]][1], 
                   color_list[labels_list[point_counter - 1 - i]][2])
            point(points_cartesian[point_counter - 1 - i][0], 
                  points_cartesian[point_counter - 1 - i][1], 
                  points_cartesian[point_counter - 1 - i][2])
            #to draw the last n-1 lines
            for i in range(n-1):
                strokeWeight(1)
                stroke(color_list[labels_list[point_counter - 1 - i]][0], 
                       color_list[labels_list[point_counter - 1 - i]][1], 
                       color_list[labels_list[point_counter - 1 - i]][2])
                line(points_cartesian[point_counter - i - 2][0], 
                     points_cartesian[point_counter - i - 2][1], 
                     points_cartesian[point_counter - i - 2][2], 
                     points_cartesian[point_counter - i - 1][0], 
                     points_cartesian[point_counter - i - 1][1], 
                     points_cartesian[point_counter - i - 1][2])
    elif point_counter > len(points_cartesian):
        for i in range(len(points_cartesian)):
            fill(color_list[labels_list[i]][0], 
                 color_list[labels_list[i]][1], 
                 color_list[labels_list[i]][2])
            text(str(i+1), points_cartesian[i][0], 
                 points_cartesian[i][1] - r/40, 
                 points_cartesian[i][2])
            strokeWeight(r/85)
            stroke(color_list[labels_list[i]][0], 
                   color_list[labels_list[i]][1], 
                   color_list[labels_list[i]][2])
            point(points_cartesian[i][0], 
                  points_cartesian[i][1], 
                  points_cartesian[i][2])
    # to draw the phase coordinates alongside the points;
    textSize(r/20)
    fill(0)
    if point_counter <= len(points_cartesian):
        if point_counter > 0 and point_counter < 10:
            text(" (" + str(round(points_rads[point_counter - 1][0], 2)) + ", " + str(round(points_rads[point_counter - 1][1], 2)) + ")", 
                 points_cartesian[point_counter - 1][0] + 32, 
                 points_cartesian[point_counter - 1][1] - 28, 
                 points_cartesian[point_counter - 1][2])
        elif point_counter >= 10:
            text(" (" + str(round(points_rads[point_counter - 1][0], 2)) + ", " + str(round(points_rads[point_counter - 1][1], 2)) + ")", 
                 points_cartesian[point_counter - 1][0] + 65, 
                 points_cartesian[point_counter - 1][1] - 28, 
                 points_cartesian[point_counter - 1][2])
            

# to draw software name;        
def software_name(r, f_phases):
    textSize(r/27)
    textAlign(LEFT)
    fill(0)
    text("spherical phase space", 
         width/6.5, 
         height/12)
    text("phi " + f_phases[15] + "/" + f_phases[17], 
         width/6.5, 
         height/12 + 50)
    text("v_0.2", 
         width/6.5, 
         height/12 + 100)
    

# to draw paths representation;
def draw_paths_representation(r, cluster_center, color_list, cluster_letters, point_counter, path_hud):
    textSize(r/20)
    textAlign(CENTER)
    for i in range(len(cluster_center)):
        fill(color_list[i][0], 
             color_list[i][1], 
             color_list[i][2])
        if i == 0:
            text(cluster_letters[i], 
                 width/5, 
                 height/2 - 100)
        elif i == 1:
            text(cluster_letters[i], 
                 width/5 - 125, 
                 height/2 + 100)
        elif i == 2:
            text(cluster_letters[i], 
                 width/5 + 125, 
                 height/2 + 100)
    textSize(r/30)
    fill(0)
    if point_counter > 1:
        # for line between group I and II
        strokeWeight(path_hud[0][0])
        stroke(0, path_hud[1][0])
        line(width/5 - 15, 
             height/2 - 110, 
             width/5 - 125, 
             height/2 + 65)
        if path_hud[1][0] != 0:
            text(str(path_hud[2][0]), 
                 width/5 - 95, 
                 height/2 - 15)
        # for line between group I and III
        strokeWeight(path_hud[0][1])
        stroke(0, path_hud[1][1])
        line(width/5 - 109, 
             height/2 + 88, 
             width/5 + 103, 
             height/2 + 88)
        if path_hud[1][1] != 0:
            text(str(path_hud[2][1]), 
                 width/5, 
                 height/2 + 120)
        # for line between group III and I
        strokeWeight(path_hud[0][2])
        stroke(0, path_hud[1][2])
        line(width/5 + 125, 
             height/2 + 65, 
             width/5 + 15, 
             height/2 - 110)
        if path_hud[1][2] != 0:
            text(str(path_hud[2][2]), 
                 width/5 + 95, 
                 height/2 - 15)
            

# to draw cluster counter representation;
def draw_cluster_counter_representation(r, points_cartesian, labels_list, cluster_center, cluster_letters, color_list, point_counter):
    textSize(r/20)
    textAlign(RIGHT)
    if point_counter >= 0 and point_counter <= len(points_cartesian):
        list_I = []
        list_II = []
        list_III = []
        for i in range(point_counter):
            if labels_list[i] == 0:
                list_I.append("true")
            elif labels_list[i] == 1:
                list_II.append("true")
            elif labels_list[i] == 2:
                list_III.append("true")
        for i in range(len(cluster_center)):
            fill(color_list[i][0], 
                 color_list[i][1], 
                 color_list[i][2])
            if i == 0:
                text(cluster_letters[i] + " - " + str(len(list_I)), 
                     width/1.285, 
                     height/5)
            elif i == 1:
                text(cluster_letters[i] + " - " + str(len(list_II)), 
                     width/1.285, 
                     height/5 + 45)
            elif i == 2:
                text(cluster_letters[i] + " - " + str(len(list_III)), 
                     width/1.285, 
                     height/5 + (2*45))
    else:
        list_I = []
        list_II = []
        list_III = []
        for i in range(len(points_cartesian)):
            if labels_list[i] == 0:
                list_I.append("true")
            elif labels_list[i] == 1:
                list_II.append("true")
            elif labels_list[i] == 2:
                list_III.append("true")
        for i in range(len(cluster_center)):
            fill(color_list[i][0], 
                 color_list[i][1], 
                 color_list[i][2])
            if i == 0:
                text(cluster_letters[i] + " - " + str(len(list_I)), 
                     width/1.285, 
                     height/5)
            elif i == 1:
                text(cluster_letters[i] + " - " + str(len(list_II)), 
                     width/1.285, 
                     height/5 + 45)
            elif i == 2:
                text(cluster_letters[i] + " - " + str(len(list_III)), 
                     width/1.285, 
                     height/5 + (2*45))
                

# to draw cluster sequence;
def draw_cluster_sequence(r, color_list, cluster_letters, labels_without_repetition):
    # to draw title and the ractangle;
    textSize(r/38)
    textAlign(CENTER)
    fill(0)
    text("cluster sequence:", 
         width/1.33, 
         height/2)
    strokeWeight(2)
    stroke(0)
    fill(255)
    rect(width/1.365, height/1.9, 120, 62)
    # to define conditions in order to represent last cluster movements inside and around the rectangle;
    textSize(r/20)
    if len(labels_without_repetition) == 1:
        fill(color_list[labels_without_repetition[0]][0], 
             color_list[labels_without_repetition[0]][1], 
             color_list[labels_without_repetition[0]][2])
        text(str(cluster_letters[labels_without_repetition[0]]), 
             width/1.323, 
             height/1.76)
    elif len(labels_without_repetition) == 2:
        for i in range(2):
            j = (i+1) * (-1)
            fill(color_list[labels_without_repetition[j]][0], 
                 color_list[labels_without_repetition[j]][1], 
                 color_list[labels_without_repetition[j]][2])
            text(str(cluster_letters[labels_without_repetition[j]]), 
                 width/1.312 - (i*35), 
                 height/1.76)
    elif len(labels_without_repetition) == 3:
        for i in range(3):
            j = (i+1) * (-1)
            fill(color_list[labels_without_repetition[j]][0], 
                 color_list[labels_without_repetition[j]][1], 
                 color_list[labels_without_repetition[j]][2])
            text(str(cluster_letters[labels_without_repetition[j]]), 
                 width/1.30 - (i*35), 
                 height/1.76)
    elif len(labels_without_repetition) == 4:
        for i in range(3):
            j = (i+1) * (-1)
            fill(color_list[labels_without_repetition[j]][0], 
                 color_list[labels_without_repetition[j]][1], 
                 color_list[labels_without_repetition[j]][2])
            text(str(cluster_letters[labels_without_repetition[j]]), 
                 width/1.30 - (i*35), 
                 height/1.76)
        fill(color_list[labels_without_repetition[-4]][0], 
             color_list[labels_without_repetition[-4]][1], 
             color_list[labels_without_repetition[-4]][2])
        text(str(cluster_letters[labels_without_repetition[-4]]), 
             width/1.385, 
             height/1.76)
    elif len(labels_without_repetition) == 5:
        for i in range(3):
            j = (i+1) * (-1)
            fill(color_list[labels_without_repetition[j]][0], 
                 color_list[labels_without_repetition[j]][1], 
                 color_list[labels_without_repetition[j]][2])
            text(str(cluster_letters[labels_without_repetition[j]]), 
                 width/1.30 - (i*35), 
                 height/1.76)
        for i in range(2):
            j = (i+4) * (-1)
            fill(color_list[labels_without_repetition[j]][0], 
                 color_list[labels_without_repetition[j]][1], 
                 color_list[labels_without_repetition[j]][2])
            text(str(cluster_letters[labels_without_repetition[j]]), 
                 width/1.385 - (i*35), 
                 height/1.76)
    elif len(labels_without_repetition) >= 6:
        for i in range(3):
            j = (i+1) * (-1)
            fill(color_list[labels_without_repetition[j]][0], 
                 color_list[labels_without_repetition[j]][1], 
                 color_list[labels_without_repetition[j]][2])
            text(str(cluster_letters[labels_without_repetition[j]]), 
                 width/1.30 - (i*35), 
                 height/1.76)
        for i in range(2):
            j = (i+4) * (-1)
            fill(color_list[labels_without_repetition[j]][0], 
                 color_list[labels_without_repetition[j]][1], 
                 color_list[labels_without_repetition[j]][2])
            text(str(cluster_letters[labels_without_repetition[j]]), 
                 width/1.385 - (i*35), 
                 height/1.76)
        fill(0)
        text("...",  
             width/1.435, 
             height/1.76)
        
        
# to draw preferred cluster movements;
def draw_preferred_cluster_movements(r, cluster_letters, color_list, cluster_movement_combinations, cluster_movement_counters, max_index, labels_without_repetition):
    if len(labels_without_repetition) >= 3:
        # to draw tittle;
        textSize(r/38)
        fill(0)
        text("movement patterns:", 
             width/1.34, 
             height/1.56)
        # to draw preferred cluster movements;
        for i in range(len(max_index)):
            for k in range(3):
                textSize(r/13)
                fill(color_list[cluster_movement_combinations[max_index[i]][k]][0], 
                     color_list[cluster_movement_combinations[max_index[i]][k]][1], 
                     color_list[cluster_movement_combinations[max_index[i]][k]][2])
                text(cluster_letters[cluster_movement_combinations[max_index[i]][k]], 
                     width/1.41 + (k*50), 
                     height/1.42 + (i*75))
            textSize(r/18)
            fill(0)
            text(" - " + str(cluster_movement_counters[max_index[i]]), 
                 width/1.3, 
                 height/1.43 + (i*75))
