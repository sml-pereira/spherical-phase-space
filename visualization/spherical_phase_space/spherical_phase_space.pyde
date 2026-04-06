add_library('sound')
add_library('peasycam')

import sps_utilities as u
import draw_utilities as d
import midi_utilities as m

# COLOCAR LINHAS DE APOIO À INTERPRETAÇÃO DE RESULTADOS!!!!!

# to define the radius (r) of the sphere, the amount of points in every sphere line (total), and the number of chords to represent simultaneously (n);
r = 700
total = 40
n = 7
point_counter = 0

# to read all the files needed to create the rpesentation;
f_phases = "phases_skk_III_4_5.txt"
f_pitch_classes = "phases_cs_4_5.txt"
f_centers = "cluster_center_III_movement.txt"
f_midi = "midi_list_III_movement.txt"
f_labels =  "labels_III_movement.txt"

# to calculate point coordinates that will constitute the sphere;
points_sphere = u.points_sphere(r, total)

# to read phases values and to calculate chord coordinates;
points_rads = u.points_rads(f_phases)
del points_rads[24]
del points_rads[32]
del points_rads[32]
del points_rads[32]
del points_rads[32]
del points_rads[33]
del points_rads[33]
del points_rads[33]
del points_rads[33]
del points_rads[33]
del points_rads[33]
del points_rads[33]
del points_rads[33]
del points_rads[34]
del points_rads[35]
del points_rads[35]
del points_rads[35]
points_cartesian = u.points_cartesian(r, points_rads)
pitches_rads = u.points_rads(f_pitch_classes)
pitches_cartesian = u.points_cartesian(r, pitches_rads)
# to import midi values for each chord in the piece
midi_list = m.midi_reader(f_midi)
del midi_list[24]
del midi_list[32]
del midi_list[32]
del midi_list[32]
del midi_list[32]
del midi_list[33]
del midi_list[33]
del midi_list[33]
del midi_list[33]
del midi_list[33]
del midi_list[33]
del midi_list[33]
del midi_list[33]
del midi_list[34]
del midi_list[35]
del midi_list[35]
del midi_list[35]

# to read cluster_center coordinates
cluster_center = u.cluster_center(f_centers)
cluster_letters = ["A", "B", "C"]

# to determine the cluster number of each chord
labels_list = u.labels_reader(f_labels)
del labels_list[24]
del labels_list[32]
del labels_list[32]
del labels_list[32]
del labels_list[32]
del labels_list[33]
del labels_list[33]
del labels_list[33]
del labels_list[33]
del labels_list[33]
del labels_list[33]
del labels_list[33]
del labels_list[33]
del labels_list[34]
del labels_list[35]
del labels_list[35]
del labels_list[35]
labels_without_repetition = []

# to determine the color of each chord;
color_list = u.color_generator()

# list to update values for path representation with structure [[s1, s2, s3], [t1, t2, t3], [c1, c2, c3]]
path_hud = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
update_values = [0.25, 255/(len(points_cartesian)/3), 1]

# list to update values for cluster movement representation
cluster_movement_combinations = [[0, 1, 0], [0, 1, 2], [0, 2, 0], [0, 2, 1], [1, 0, 1], [1, 0, 2], [1, 2, 1], [1, 2, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 2]]
cluster_movement_counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
max_index = []

# to define list with individual pitch class names
pitches_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def setup():
    global cam
    fullScreen(P3D)
    frameRate(60)
    textSize(r/20)
    cam = PeasyCam(this, r*3)
    cam.setMinimumDistance(r/2);
    cam.setMaximumDistance(r*5)
    

def draw():
    lights()
    background(255)
    
    # 1. to draw all the points that constitute the sphere;
    d.draw_sphere(points_sphere)
    
    # 2. to draw the reference lines and points;
    d.draw_references(r, f_phases, pitches_cartesian, pitches_names)
    
    # 3. to draw the cluster centers
    d.draw_cluster_centers(r, cluster_center, cluster_letters, color_list, point_counter)
    
    # 4. to draw chords in the sphere (Only 1 of the following options)    
    # 4.1) to draw numbered points with the respective cluster color;
    #d.draw_points(r, points_cartesian, color_list, labels_list, point_counter)
    
    # 4.2) to draw numbered points with their respective cluster color and lines between points;
    #d.draw_paths(r, points_cartesian, color_list, labels_list, point_counter)
    
    # 4.3) to draw only the last n points and lines in the spherical space;
    d.draw_n_paths(r, n, points_rads, points_cartesian, color_list, labels_list, point_counter)

    # 5. to draw the analysis tools on heads-up display;
    cam.beginHUD()
    # 5.1) to draw software name;
    d.software_name(r, f_phases)
    
    # 5.2) to draw paths representation;
    d.draw_paths_representation(r, cluster_center, color_list, cluster_letters, point_counter, path_hud)
        
    # 5.3) to draw cluster counter representation;
    d.draw_cluster_counter_representation(r, points_cartesian, labels_list, cluster_center, cluster_letters, color_list, point_counter)
    
    # 5.4) to draw cluster sequence;
    d.draw_cluster_sequence(r, color_list, cluster_letters, labels_without_repetition)
    
    # 5.5) to draw preferred cluster movements;
    d.draw_preferred_cluster_movements(r, cluster_letters, color_list, cluster_movement_combinations, cluster_movement_counters, max_index, labels_without_repetition)
    cam.endHUD()        


def keyPressed():
    global point_counter
    global max_index
    if point_counter <= len(points_cartesian) + 1:
        # 1. to define what happens when the UP key is pressed;
        if keyCode == UP and point_counter < len(points_cartesian) + 1:
            # 1.1) to update point_counter value;
            point_counter += 1
            # 1.2) to update values of the path hud representation;
            if point_counter > 1 and point_counter <= len(points_cartesian):
                if labels_list[point_counter - 2] == 0 and labels_list[point_counter - 1] == 1 or labels_list[point_counter - 2] == 1 and labels_list[point_counter - 1] == 0:
                    for i in range(3):
                        path_hud[i][0] += update_values[i]
                elif labels_list[point_counter - 2] == 1 and labels_list[point_counter - 1] == 2 or labels_list[point_counter - 2] == 2 and labels_list[point_counter - 1] == 1:
                    for i in range(3):
                        path_hud[i][1] += update_values[i]
                elif labels_list[point_counter - 2] == 2 and labels_list[point_counter - 1] == 0 or labels_list[point_counter - 2] == 0 and labels_list[point_counter - 1] == 2:
                    for i in range(3):
                        path_hud[i][2] += update_values[i]
            #1.3) to update values of the sequence of clusters hud representation;
            if point_counter == 1:
                labels_without_repetition.append(labels_list[point_counter - 1])
            elif point_counter > 1 and point_counter <= len(points_cartesian):
                if labels_list[point_counter - 2] != labels_list[point_counter - 1]:
                    labels_without_repetition.append(labels_list[point_counter - 1])    
            # 1.4) to update values of the prefered cluster movements hud representation;
            if len(labels_without_repetition) >= 3 and point_counter <= len(points_cartesian):
                if labels_list[point_counter - 2] != labels_list[point_counter - 1]:
                    if labels_without_repetition[-3] == 0 and labels_without_repetition[-2] == 1 and labels_without_repetition[-1] == 0:
                        cluster_movement_counters[0] += 1
                    elif labels_without_repetition[-3] == 0 and labels_without_repetition[-2] == 1 and labels_without_repetition[-1] == 2:
                        cluster_movement_counters[1] += 1
                    elif labels_without_repetition[-3] == 0 and labels_without_repetition[-2] == 2 and labels_without_repetition[-1] == 0:
                        cluster_movement_counters[2] += 1
                    elif labels_without_repetition[-3] == 0 and labels_without_repetition[-2] == 2 and labels_without_repetition[-1] == 1:
                        cluster_movement_counters[3] += 1
                    elif labels_without_repetition[-3] == 1 and labels_without_repetition[-2] == 0 and labels_without_repetition[-1] == 1:
                        cluster_movement_counters[4] += 1
                    elif labels_without_repetition[-3] == 1 and labels_without_repetition[-2] == 0 and labels_without_repetition[-1] == 2:
                        cluster_movement_counters[5] += 1
                    elif labels_without_repetition[-3] == 1 and labels_without_repetition[-2] == 2 and labels_without_repetition[-1] == 1:
                        cluster_movement_counters[6] += 1
                    elif labels_without_repetition[-3] == 1 and labels_without_repetition[-2] == 2 and labels_without_repetition[-1] == 0:
                        cluster_movement_counters[7] += 1
                    elif labels_without_repetition[-3] == 2 and labels_without_repetition[-2] == 0 and labels_without_repetition[-1] == 1:
                        cluster_movement_counters[8] += 1
                    elif labels_without_repetition[-3] == 2 and labels_without_repetition[-2] == 0 and labels_without_repetition[-1] == 2:
                        cluster_movement_counters[9] += 1
                    elif labels_without_repetition[-3] == 2 and labels_without_repetition[-2] == 1 and labels_without_repetition[-1] == 0:
                        cluster_movement_counters[10] += 1
                    elif labels_without_repetition[-3] == 2 and labels_without_repetition[-2] == 1 and labels_without_repetition[-1] == 2:
                        cluster_movement_counters[11] += 1
            # 1.5) to determine the indexes of the max elements in the cluster movement counters list;
            if len(labels_without_repetition) >= 3 and point_counter <= len(points_cartesian):
                m = max(cluster_movement_counters)
                max_index = [i for i, j in enumerate(cluster_movement_counters) if j == m]
                while len(max_index) > 2:
                    del max_index[-1]
                print(cluster_movement_counters)
            # 1.6) to play the respective chord;
            if point_counter <= len(midi_list):
                for i in range(len(midi_list[point_counter - 1])):
                    f = SoundFile(this, midi_list[point_counter - 1][i] + ".wav")
                    f.play()
                    
        # 2. to define what happens when the DOWN key is pressed;
        elif keyCode == DOWN and point_counter > 0:
            # 2.1) to update point_counter value;
            point_counter -= 1
            # 2.2) to update values of the path hud representation;
            if point_counter > 1 and point_counter <= len(points_cartesian) - 1:
                if labels_list[point_counter - 1] == 0 and labels_list[point_counter] == 1 or labels_list[point_counter - 1] == 1 and labels_list[point_counter] == 0:
                    for i in range(3):
                        path_hud[i][0] -= update_values[i]
                elif labels_list[point_counter - 1] == 1 and labels_list[point_counter] == 2 or labels_list[point_counter - 1] == 2 and labels_list[point_counter] == 1:
                    for i in range(3):
                        path_hud[i][1] -= update_values[i]
                elif labels_list[point_counter - 1] == 2 and labels_list[point_counter] == 0 or labels_list[point_counter - 1] == 0 and labels_list[point_counter] == 2:
                    for i in range(3):
                        path_hud[i][2] -= update_values[i]
           # 2.3) to update values of the prefered cluster movements hud representation;         
            if len(labels_without_repetition) >= 3 and point_counter < len(points_cartesian):
                if labels_list[point_counter - 1] != labels_list[point_counter]:
                    if labels_without_repetition[-3] == 0 and labels_without_repetition[-2] == 1 and labels_without_repetition[-1] == 0:
                        cluster_movement_counters[0] -= 1
                    elif labels_without_repetition[-3] == 0 and labels_without_repetition[-2] == 1 and labels_without_repetition[-1] == 2:
                        cluster_movement_counters[1] -= 1
                    elif labels_without_repetition[-3] == 0 and labels_without_repetition[-2] == 2 and labels_without_repetition[-1] == 0:
                        cluster_movement_counters[2] -= 1
                    elif labels_without_repetition[-3] == 0 and labels_without_repetition[-2] == 2 and labels_without_repetition[-1] == 1:
                        cluster_movement_counters[3] -= 1
                    elif labels_without_repetition[-3] == 1 and labels_without_repetition[-2] == 0 and labels_without_repetition[-1] == 1:
                        cluster_movement_counters[4] -= 1
                    elif labels_without_repetition[-3] == 1 and labels_without_repetition[-2] == 0 and labels_without_repetition[-1] == 2:
                        cluster_movement_counters[5] -= 1
                    elif labels_without_repetition[-3] == 1 and labels_without_repetition[-2] == 2 and labels_without_repetition[-1] == 1:
                        cluster_movement_counters[6] -= 1
                    elif labels_without_repetition[-3] == 1 and labels_without_repetition[-2] == 2 and labels_without_repetition[-1] == 0:
                        cluster_movement_counters[7] -= 1
                    elif labels_without_repetition[-3] == 2 and labels_without_repetition[-2] == 0 and labels_without_repetition[-1] == 1:
                        cluster_movement_counters[8] -= 1
                    elif labels_without_repetition[-3] == 2 and labels_without_repetition[-2] == 0 and labels_without_repetition[-1] == 2:
                        cluster_movement_counters[9] -= 1
                    elif labels_without_repetition[-3] == 2 and labels_without_repetition[-2] == 1 and labels_without_repetition[-1] == 0:
                        cluster_movement_counters[10] -= 1
                    elif labels_without_repetition[-3] == 2 and labels_without_repetition[-2] == 1 and labels_without_repetition[-1] == 2:
                        cluster_movement_counters[11] -= 1
            # 2.4) to determine the indexes of the max elements in the cluster movement counters list;
            if len(labels_without_repetition) >= 3 and point_counter < len(points_cartesian):
                if all(i == cluster_movement_counters[0] for i in cluster_movement_counters) == False:
                    m = max(cluster_movement_counters)
                    max_index = [i for i, j in enumerate(cluster_movement_counters) if j == m]
                    while len(max_index) > 2:
                        del max_index[-1]
            # 2.5) to update values of the sequence of clusters hud representation;
            if point_counter < len(points_cartesian):
                if labels_list[point_counter - 1] != labels_list[point_counter]:
                    del labels_without_repetition[-1]        
            # 2.6) to play the respective chord;
            if point_counter > 0:
                for i in range(len(midi_list[point_counter - 1])):
                    f = SoundFile(this, midi_list[point_counter - 1][i] + ".wav")
                    f.play()
            
    
def mouseClicked():
    if point_counter > 0 and point_counter <= len(midi_list):
        for i in range(len(midi_list[point_counter - 1])):
            f = SoundFile(this, midi_list[point_counter - 1][i] + ".wav")
            f.play()    
        
