#   All the functions required for phaseSpace_main.py are defined in this file.
#   Written in Python 3.7.

import os
import pathlib
import scipy.fftpack
import numpy as np
import music21
from itertools import combinations as cbn
from matplotlib import pyplot as plt


#
def set_directory():
    os.chdir(pathlib.Path(__file__).parent.absolute())


#1) Function that reads all the chords in one .xml file.
def sheet_music_reader(piece_name, print_option=""):
    """ This function creates a harmonic data set from any .xml file that contains all the chords in the piece. 
        It receives as arguments the name of the file to be analyzed and the word print as a string to show the sheet music.
        If the second argument is unexistent or any other word the sheet music does not appear."""
    #   substitute the word with the name of the .xml file to analyze
    xml = piece_name
    sheet = music21.corpus.parse(xml)
    #   reduces the sheet music to a salami version of each vertical moment
    salami_sheet = sheet.chordify()
    #   counts the number of the salami slices
    count = 1
    for each_chord in salami_sheet.recurse().getElementsByClass('Chord'):
        each_chord.addLyric(str(count))
        count += 1
    #   defines when the function should print the score
    if print_option == "print":
        salami_sheet.show()
    elif print_option == "":
        pass
    else:
        pass
    return salami_sheet


#2) Function that creates the MIDI list.
def midi_list_creator(salami_sheet, print_option=""):
    pitches_list = []
    midi_list = []
    chords_to_process = salami_sheet.recurse().getElementsByClass('Chord')
    for each_chord in chords_to_process:
        pitches_list.append(each_chord.pitches)
    for i in range(len(pitches_list)):
        midi_list.append([])
        for j in range(len(pitches_list[i])):
            midi_list[i].append(pitches_list[i][j].midi)
    #   defines when the function should print the list of pitch classes
    if print_option == "print":
        print(midi_list)
    elif print_option == "":
        pass
    else:
        pass
    return midi_list


#
def midi_list_exporter(midi_list, movement):
    with open("midi_list_" + str(movement) + "_movement" + ".txt", 'w') as filehandle:
        for listitem in midi_list:
            filehandle.write('%s\n' % listitem)
    


#2) Function that creates the pitch classes data structure.
def pitch_classes_creator(salami_chords, print_option="", start=0, end=None):
    """ This function transforms the salami chords in pitch classes in ascending order.
        It receives as arguments the salami chords and the word print as a string to show the list of pitch classes.
        If the second argument is unexistent or any other word the list does not appear."""
    pitch_class_dataset = []
    chords_to_process = salami_chords.recurse().getElementsByClass('Chord')
    #   process end of salami_chords to be used, in case it is not defined (all chords)
    if end is None:
        end = len(chords_to_process) 
    #   process start of salami_chords to be used, in case it is higher than the end (0 or change values)
    if start > end:
        if end == len(chords_to_process):
            start = 0
        else:
            tmp = start
            start = end
            end = start
    #   the cycle in the next lines appends to the pitch_class_dataset all the different pitches in all the salami slices of the chosen music piece
    for each_chord in chords_to_process:
        if start <= int(each_chord.lyrics[0].text) <= end:
            pitch_class_dataset.append(each_chord.normalOrder)
    #   the cycle in the next lines establishes ascending order in all pitch lists of the piece
    for i in range(len(pitch_class_dataset)):
        pitch_class_dataset[i].sort()
    #   defines when the function should print the list of pitch classes
    if print_option == "print":
        print(pitch_class_dataset)
    elif print_option == "":
        pass
    else:
        pass
    return pitch_class_dataset


#3) Function that transforms the pitch classes data structure in chroma vectors.
def pitch_classes_vector_creator(pitch_classes, print_option=""):
    """ This function transforms the pitch classes dataset in chroma vectors with twelve numbers where the number 0
        means that pitch class is not present and the number 1 menas it exists.
        It receives as arguments the pitch classes dataset and the word print as a string to show the list of chroma vectors.
        If the second argument is unexistent or any other word the list does not appear."""
    pitch_class_vector_dataset = []
    #   the cycle in the next lines tranforms the pitch lists in chroma vectors
    for i in range(len(pitch_classes)):
        pitch_class_vector_dataset.append([])
        for k in range(12):
            pitch_class_vector_dataset[i].append(0)
            if k == 11:
                break
        for j in range(len(pitch_classes[i])):
            pitch_class_vector_dataset[i][pitch_classes[i][j]] = 1
    #   defines when the function should print the list of all chroma vectors in the piece
    if print_option == "print":
        print(pitch_class_vector_dataset)
    elif print_option == "":
        pass
    else:
        pass
    return pitch_class_vector_dataset


#4) Function that prints the pitch classes histogram.
def pitch_classes_counter(salami_sheet):
    """ Function from the Music21 archive that prints an histogram that counts all the pitch classes in the piece.
        It receives as arguments the salami chords previously generated."""
    #   to call the Music21 function
    salami_sheet.plot("histogram", "pitchClass")


#5) Function that prints the interval classes histogram.
def interval_class_counter(salami_sheet):
    """ Function that prints an histogram to count all the interval classes in the piece.
        It receives as arguments the salami chords previously generated."""
    #   to create all the required data structures
    interval_vector_list = []
    interval_vector_sum = []
    interval_vector_labels = []
    x = [1, 2, 3, 4, 5, 6]
    #   to count the occurrences of each interval class in every chord
    for each_chord in salami_sheet.recurse().getElementsByClass('Chord'):
        interval_vector_list.append(each_chord.intervalVector)
    #   to count all the occurrences of each interval class
    interval_vector_sum = [sum(i) for i in zip(*interval_vector_list)]
    #   to generate the labels to be printed in the histogram
    for i in range(len(interval_vector_sum)):
        interval_vector_labels.append("n = " + str(interval_vector_sum[i]))
    #   to draw the graph
    plt.bar(x, interval_vector_sum, align = 'center')
    plt.xlabel('Interval Classes')
    plt.ylabel('Occurrences')
    #   to print the required labels in the graph
    for i in range(len(x)):
        plt.text(x = x[i]-0.3, y = interval_vector_sum[i] + max(interval_vector_sum)/100, s = interval_vector_labels[i], size = 9)


#6) Function that calculates the fft of pitch class sets and considers only the most relevant elements for the chroma vectors of the piece.
def fft_calculator(chroma_vectors, print_option=""):
    """ This function calculates the fft of pitch class sets given a certain chroma vector, and, afterwards, considers only
        the elements 1, 2, 3, 4, 5 and 6 wich are representative of the relevant interval classes.
        It receives as arguments the chroma vector dataset and the word print as a string to show the list of the relevant FFT values.
        If the second argument is unexistent or any other word the list does not appear."""
    fft_dataset = []
    fft_dataset_transformed = []
    #   calculates the fft values given a 12 element chroma vector
    fft_dataset = scipy.fftpack.fft(chroma_vectors)
    #   the cycle in the next lines creates the fft_dataset_transformed wich is the list with the required elements of the FFT. The elements 1, 2, 3, 4, 5, and 6
    for fft_vector in fft_dataset:
        fft_dataset_transformed.append([complex(np.real(fft_vector[index])/np.real(fft_vector[0]), np.imag(fft_vector[index])/np.real(fft_vector[0])) for index in range(1,7)])
    #   defines when the function should print the list fft_dataset_transformed
    if print_option == "print":
        print(fft_dataset_transformed)
    elif print_option == "":
        pass
    else:
        pass
    return fft_dataset_transformed


#7) Function that calculates the magnitudes for the FFT elements.
def magnitude_calculator(fft_dataset, print_option=""):
    """ This function calculates the magnitudes for each of the elements given by the FFT of pitch class sets.
        It receives as arguments the FFT transformed dataset, in order to only calculate the magnitudes for the required
        FFT elements, and the word print as a string to show the list of magnitudes."""
    #   to calculate magnitudes
    magnitudes = np.absolute(fft_dataset)
    #   defines when the function should print the list of magnitudes
    if print_option == "print":
        print(magnitudes)
    elif print_option == "":
        pass
    else:
        pass
    return magnitudes


#8) Function that calculates the phases for the FFT elements
def phases_calculator(fft_dataset, print_option=""):
    """ This function calculates the phases for each of the elements given by the FFT of pitch class sets.
        It receives as arguments the FFT transformed dataset, in order to only calculate the phases for the required
        FFT elements, and the word print as a string to show the list of phases."""
    #   to calculate phases
    phases = np.angle(fft_dataset)
    #   defines when the function should print the list of phases.
    if print_option == "print":
        print(phases)
    elif print_option == "":
        pass
    else:
        pass
    return phases




def phases_exporter(phases, movement, print_1, print_2):
        new_list = []
        for i in range(len(phases)):
            new_list.append([])
            new_list[i].append(phases[i][print_1 - 1])
            new_list[i].append(phases[i][print_2 - 1])
        with open("phases_skk_" + str(movement) + "_" + str(print_1) + "_" + str(print_2) + ".txt", 'w') as filehandle:
            for listitem in new_list:
                filehandle.write('%s\n' % listitem)
   




#9) Function that generates one random color for each chord of the piece
def color_definition(phases):
    """ This function generates as much random colors as the number of chords in the piece.
        It receives only one argument wich is the phases dataset."""
    #   to generate the random colors
    colors = [np.random.rand(3,) for i in range(len(phases))]
    return colors


#10) Function that defines the size of the window to print all the graphs.
def window_size(x, y):
    """ This function defines the size of the window that will print all the information needed.
        It receives as arguments the x and y size values for the window, respectively."""
    #   to define the x and y window sizw values
    plt.rcParams['figure.figsize'] = (x, y)


#11) Function that makes all the calculations to show the chords as points in all the phase space possibilities.
def plot_in_all_phase_spaces(phases, magnitudes, phase_scope=[1, 2, 3, 4, 5, 6], c='b'):
    """ This function makes all the calculations needed to show all the chords in one piece as points in all
        phase spaces possibilities.
        It receives as arguments the phases dataset, the magnitudes dataset, the phase_scope list wich is the number 
        of combinations to be shown, and the colors dataset, respectively."""
    spaces = list(cbn(phase_scope, 2))
    fig, axarr = plt.subplots(5, 6, sharex=True, sharey=True)
    plt.xlim(-3.5, 3.5)
    plt.ylim(-3.5, 3.5)
    for space in spaces:
        xs = []
        ys = []
        x, y = space
        colors = []
        for i in range(len(phases)):
            if magnitudes[i][x-1] != 0 and magnitudes[i][y-1] != 0:
                xs.append(phases[i][x-1])
                ys.append(phases[i][y-1])
                if len(c) > 1:
                    colors.append(c[i])
                else:
                    colors.append(c)
        axarr[x - 1, y - 1].scatter(xs, ys, c=colors)
        axarr[x - 1, y - 1].set_title('phi_{} vs. phi_{}'.format(x, y))


#12) Function that makes all the calculations to show the path of chords in all the phase space possibilities.
def path_in_all_phase_spaces(phases, magnitudes, phase_scope=[1, 2, 3, 4, 5, 6], c='b'):
    """ This function makes all the calculations needed to show the path of chords in one piece in all the
        phase spaces possibilities.
        It receives as arguments the phases dataset, the magnitudes dataset, the phase_scope list wich is the number 
        of combinations to be shown, and the colors dataset, respectively."""
    spaces = list(cbn(phase_scope, 2))
    fig, axarr = plt.subplots(5, 6, sharex=True, sharey=True)
    plt.xlim(-3.5, 3.5)
    plt.ylim(-3.5, 3.5)
    for space in spaces:
        xs = []
        ys = []
        x, y = space
        colors = []
        for i in range(len(phases)):
            if magnitudes[i][x-1] != 0 and magnitudes[i][y-1] != 0:
                xs.append(phases[i][x-1])
                ys.append(phases[i][y-1])
                if len(c) > 1:
                    colors.append(c[i])
                else:
                    colors.append(c)
        xs = np.array(xs)
        ys = np.array(ys)
        axarr[x - 1, y - 1].quiver(xs[:-1], ys[:-1], xs[1:] - xs[:-1], ys[1:] - ys[:-1], color=colors, scale_units='xy', angles='xy', scale=1)
        plt.title('phi_{} vs. phi_{} phase space'.format(x, y))


#13) Function that makes all the calculations to show the chords as points in one specific phase space.
def plot_just_one_phase_space(phases, magnitudes, space_x, space_y, c='b', text=False, start=0):
    """ This function makes all the calculations needed to show all the chords in one piece as points in one
        specific phase space.
        It receives as arguments the phases dataset, the magnitudes dataset, the phase component to represent
        in the x axis, the phase component to represent in the y axis and the colors dataset, respectively."""
    fig, _ = plt.subplots()
    xs = []
    ys = []
    colors = []
    for i in range(len(phases)):
        if magnitudes[i][space_x-1] != 0 and magnitudes[i][space_y-1] != 0:
            xs.append(phases[i][space_x-1])
            ys.append(phases[i][space_y-1])
            if len(c) > 1:
                colors.append(c[i])
            else:
                colors.append(c)
            if text:
                plt.text(xs[-1], ys[-1], str(start + i), color=colors[-1]) 
    if not text:
        plt.scatter(xs, ys, c=colors)
    plt.xlim(-3.5, 3.5)
    plt.ylim(-3.5, 3.5)
    plt.title('phi_{} vs. phi_{} phase space'.format(space_x, space_y))


#14) Function that makes all the calculations to show the path of chords in one specific phase space.
def path_just_one_phase_space(phases, magnitudes, space_x, space_y, c='b'):
    """ This function makes all the calculations needed to show the chords path in one piece for one
        specific phase space.
        It receives as arguments the phases dataset, the magnitudes dataset, the phase component to represent
        in the x axis, the phase component to represent in the y axis and the colors dataset, respectively."""
    fig, _ = plt.subplots()
    xs = []
    ys = []
    colors = []
    for i in range(len(phases)):
        if magnitudes[i][space_x-1] != 0 and magnitudes[i][space_y-1] != 0:
            xs.append(phases[i][space_x-1])
            ys.append(phases[i][space_y-1])
            if len(c) > 1:
                colors.append(c[i])
            else:
                colors.append(c)
    xs = np.array(xs)
    ys = np.array(ys)
    plt.quiver(xs[:-1], ys[:-1], xs[1:] - xs[:-1], ys[1:] - ys[:-1], color=colors, scale_units='xy', angles='xy', scale=1, width = 0.004, headlength = 4)
    plt.xlim(-3.5, 3.5)
    plt.ylim(-3.5, 3.5)
    plt.title('phi_{} vs. phi_{} phase space'.format(space_x, space_y))


#15) Function that prints all the required graphs.
def show_graphs():
    """This function prints all the required graphs."""
    #   to print all the required graphs
    plt.show()
