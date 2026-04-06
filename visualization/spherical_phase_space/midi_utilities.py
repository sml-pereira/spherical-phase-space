
# Generates a list of strings
def midi_reader(file_name):
    # 
    midi_list = []
    # open file and read the content in a list
    with open(file_name, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            midi_list.append(currentPlace)
    
    for i in range(len(midi_list)):
        midi_list[i] = midi_list[i].split(", ")
        if len(midi_list[i]) == 1:
            midi_list[i][0] = midi_list[i][0].replace("]", "")
        for j in range(len(midi_list[i])):
            if j == 0:
                midi_list[i][j] = midi_list[i][j].replace("[", "")
            elif j == len(midi_list[i]) - 1:
                midi_list[i][j] = midi_list[i][j].replace("]", "")
    return midi_list
