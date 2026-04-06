# phaseSpace_main.py
# Written in Python 3.7.

import phaseSpace_utilities as ps

def main():

    #
    ps.set_directory()

    #   to read the .xml file and to transform that information in chroma vectors.
    salami_sheet = ps.sheet_music_reader("asd", "option - print")

    midi_list = ps.midi_list_creator(salami_sheet, "option - print")
    #ps.midi_list_exporter(midi_list, "V")

    pitch_class_dataset = ps.pitch_classes_creator(salami_sheet, "option - print", start = 1)
    pitch_classes_vector_dataset = ps.pitch_classes_vector_creator(pitch_class_dataset, "option - print")

    #   to show the histograms that counts all the pitch classes and interval classes in the piece.
    #ps.pitch_classes_counter(salami_sheet)
    #ps.interval_class_counter(salami_sheet)

    #   to calculate the FFT of pitch class sets and magnitudes and phases.
    fft_dataset_transformed = ps.fft_calculator(pitch_classes_vector_dataset, "option - print")
    magnitudes = ps.magnitude_calculator(fft_dataset_transformed, "print")

    phases = ps.phases_calculator(fft_dataset_transformed, "option - print")


    #ps.phases_exporter(phases, "cs", 1, 5)


    #   to create random colors for each chord of the piece.
    colors = ps.color_definition(phases)
    
    #   to define the window size where the results will appear.
    ps.window_size(15, 15)

    #   to show all the chords as points in every phase space possibility and in one specific phase space.
    #ps.plot_in_all_phase_spaces(phases, magnitudes, phase_scope=[1,2,3,4,5,6], c=colors)
    #ps.plot_just_one_phase_space(phases, magnitudes, 4, 5, c=colors, text=False, start=0)

    #   to show the chords path in every phase space possibility and in one specific phase space.
    #ps.path_in_all_phase_spaces(phases, magnitudes, phase_scope=[1,2,3,4,5,6], c=colors)
    #ps.path_just_one_phase_space(phases, magnitudes, 4, 5, c=colors)

    #   to print the required graphs.
    ps.show_graphs()

if __name__ == "__main__":
    main()
