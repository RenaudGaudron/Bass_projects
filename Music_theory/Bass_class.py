class Bass_class:
# Python class defining an object with several attributes: the number of strings, number of frets and tuning of the bass. Several methods are then defined to perform calculations on instances of the Bass_class class.
    
    Notes_English = ['A', 'A♯/B♭', 'B', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭']  # Ordered notes of the 12 tone chromatic scale - English version
    Notes_German = ['A', 'A♯/B', 'H', 'C', 'C♯/D♭', 'D', 'D♯/E♭', 'E', 'F', 'F♯/G♭', 'G', 'G♯/A♭']  # Ordered notes of the 12 tone chromatic scale - German version
    Notes_Latin = ['la', 'la♯/si♭', 'si', 'do', 'do♯/re♭', 're', 're♯/mi♭', 'mi', 'fa', 'fa♯/sol♭', 'sol', 'sol♯/la♭']  # Ordered notes of the 12 tone chromatic scale - Neo-latin version
    
    Intervals =['Perfect Unison', 'Minor Second', 'Major Second', 'Minor Third', 'Major Third', 'Perfect Fourth', 'Augmented Fourth/Dimished Fifth', 'Perfect Fifth', 'Minor Sixth', 'Major Sixth', 'Minor Seventh', 'Major Seventh', 'Octave'] # Main name for intervals by increasing number of semitones
    
    special_frets = [3, 5, 7, 9, 15, 17, 19, 21]  # Frets where there is a dot on the fretboard
    octave_frets = [12, 24]  # Frets where there is a double dot on the fretboard
    
    char1 = '\x1b[6;30;42m'  # Green background
    char2 = '\x1b[6;30;43m' # Orange background
    char_norm = '\x1b[0m'  # Normal background color

    def __init__(self, n_strings=None, n_frets=None, conv=1):     # Initialisation - called whenever an instance is created
        # n_strings: number of strings
        # n_frets: number of frets
        # convention: convention used for the notes (1: English, 2: German, 3: Neo-Latin)

        min_string = 4  # Minimum number of strings
        max_string = 6  # Maximum number of strings
        min_fret = 0  # Minimum number of frets
        max_fret = 24  # Maximum number of frets

        # Notes names are defined using the desired convention
        if conv==1:
            self.Notes = Bass_class.Notes_English
        elif conv==2:
            self.Notes = Bass_class.Notes_German
        else:
            self.Notes = Bass_class.Notes_Latin

        if n_strings is None:  # If there is no specified value
            print('The number of strings was set to 4')
            self.n_strings = 4  # Standard number of strings set to 4
        elif n_strings not in range(min_string, max_string + 1):  # If the specified value is outside of the admissible range
            raise ValueError('The number of strings was set to {val}. Please select a value comprised between 4 and 6.'.format(val=n_strings))
        else:  # If the specified value is within the admissible range
            self.n_strings = n_strings  # Number of strings

        if n_frets is None:  # If there is no specified value
            print('The number of frets was set to 12')
            self.n_frets = 12  # Standard number of frets set to 12
        elif n_frets not in range(min_fret, max_fret + 1):   # If the specified value is outside of the admissible range
            raise ValueError('The number of frets was set to {val}. Please select a value comprised between 0 and 24.'.format(val=n_frets))
        else: # If the specified value is within the admissible range
            self.n_frets = n_frets  # Number of frets

        # Set the tuning for 4, 5 or 6 strings
        if self.n_strings == 4:
            self.tuning = [self.Notes[7], self.Notes[0], self.Notes[5], self.Notes[10]]
        elif self.n_strings == 5:
            self.tuning = [self.Notes[2], self.Notes[7], self.Notes[0], self.Notes[5], self.Notes[10]]
        elif self.n_strings == 6:
            self.tuning = [self.Notes[2], self.Notes[7], self.Notes[0], self.Notes[5], self.Notes[10], self.Notes[3]]

    def bass_info(self):  # Provides information about the instance
        print('\nYour bass has {a} strings tuned to {b} and has {c} frets'.format(a=self.n_strings, b=self.tuning, c=self.n_frets))

    def Note_from_pos(self, s, f):  # Returns the note located on string s and on fret f
        open_note = self.tuning[s - 1]  # Note of the corresponding open string
        index_ON = self.Notes.index(open_note)  # Index of the open string in the Notes array
        answer = self.Notes[(index_ON + f) % len(self.Notes)]
        return answer

    def Index_note(self, note, string_number):  # Getting the index or indices of a note on string number n°string_number
        open_note = self.tuning[string_number - 1]  # Note of the corresponding open string
        index_ON = self.Notes.index(open_note)  # Index of the open string in the Notes array
        string_notes = [self.Notes[(index_ON + i) % len(self.Notes)] for i in range(0, self.n_frets + 1)]  # Contains all ordered notes on the string of interest
        note_indices = [ind for ind, x in enumerate(string_notes) if x == note]
        return note_indices
        
    def bass_chart(self, dict_color):  # Returns the bass chart with highlighted notes - only one colour
        # dict_color contains a dictionary where the key corresponds to the string number and the corresponding value
        # is a list containing all frets to be highlighted for that string.

        chart = str()  # Used to store the chart

        # Creating the bass chart
        for i in reversed(range(0, len(self.tuning))):  # For every string (reversed because the string with the highest number is printed first, followed by the second highest, etc.)

            # Adding fret n°0 
            chart_temp =' '*(8-len(self.tuning[i])) # Padding depending on the number of characters used to write the open note. This ensures that all strings are vertically aligned
            if str(i+1) in dict_color.keys() and 0 in dict_color[str(i+1)]: # If the string and fret n°0 are in the dictionary
                chart_temp += Bass_class.char1 + str(self.tuning[i]) + Bass_class.char_norm + '|'  # Different colour for reference note, in that case the open note of the string
            else: # If the combination (string, fret) is not in the dictionary
                chart_temp += str(self.tuning[i]) + '|'  # Normal colour
                
            # Adding additional frets                    
            for j in range(1, self.n_frets + 1):  
                
                # For special frets represented by a dot on the fretboard
                if j in Bass_class.special_frets:
                    if str(i+1) in dict_color.keys() and j in dict_color[str(i+1)]:  # If the string and fret are in the dictionary
                        chart_temp += Bass_class.char1 +  '-o-'  + Bass_class.char_norm + '|'   # Different colour for reference note
                    else: # If the combination (string, fret) is not in the dictionary
                        chart_temp += '-o-|'   # Normal colour
                    
                # For octave frets represented by a double dot on the fretboard                        
                elif j in Bass_class.octave_frets:
                    if str(i+1) in dict_color.keys() and j in dict_color[str(i+1)]:  # If the string and fret are in the dictionary
                        chart_temp += Bass_class.char1 +  '-8-'  + Bass_class.char_norm + '|'   # Different colour for reference note
                    else: # If the combination (string, fret) is not in the dictionary
                        chart_temp += '-8-|'   # Normal colour 
                    
                # For normal frets represented by a dash on the fretboard                                            
                else:
                    if str(i+1) in dict_color.keys() and j in dict_color[str(i+1)]:   # If the string and fret are in the dictionary
                        chart_temp += Bass_class.char1 +  '---'  + Bass_class.char_norm + '|'   # Different colour for reference note
                    else: # If the combination (string, fret) is not in the dictionary
                        chart_temp += '---|'   # Normal colour
                    
            chart += chart_temp +'\n' # Adding the line corresponding to one string to the chart variable
        print(chart) # Printing the entire chart

                
    def bass_chart_2col(self, string_number, fret_number, string_number_2, fret_number_2):  
        # Returns the bass chart with two highlighted notes. 
        # The first note, on string n°string_number and fret n°fret_number, is colored in blue
        # The second note, on string n°string_number_2 and fret n°fret_number_2, is colored in red

        chart = str()  # Used to store the chart

        # Creating the bass chart
        for i in reversed(range(0, len(self.tuning))):  # For every string (reversed because the string with the highest number is printed first, followed by the second highest, etc.)
            
            # Adding fret n°0 
            chart_temp =' '*(8-len(self.tuning[i])) # Padding depending on the number of characters used to write the open note. This ensures that all strings are vertically aligned
            if i+1==string_number and fret_number==0: # If the first reference note is located on that string and on fret 0
                chart_temp += Bass_class.char1 + str(self.tuning[i]) + Bass_class.char_norm  + '|' # Different colour for reference note n°1
            elif i+1==string_number_2 and fret_number_2==0:  # If the second reference note is located on that string and on fret 0
                chart_temp += Bass_class.char2 + str(self.tuning[i]) + Bass_class.char_norm  + '|'  # Different colour for reference note n°2
            else:
                chart_temp += str(self.tuning[i]) + '|'  # Normal colour 
                
            # Adding additional frets    
            for j in range(1, self.n_frets + 1):  # Loop over the fret numbers
                
                # For special frets represented by a dot on the fretboard
                if j in Bass_class.special_frets: 
                    if i+1==string_number and j==fret_number:  # If the first reference note is located on that string and on that fret
                        chart_temp += Bass_class.char1 + '-o-' + Bass_class.char_norm + '|'  # Different colour for reference note n°1
                    elif i+1==string_number_2 and j==fret_number_2: # If the second reference note is located on that string and on that fret
                        chart_temp += Bass_class.char2 + '-o-' + Bass_class.char_norm  + '|'  # Different colour for reference note n°2
                    else:
                        chart_temp += '-o-|' # Normal colour
                        
                # For octave frets represented by a double dot on the fretboard                        
                elif j in Bass_class.octave_frets:
                    if i+1==string_number and j==fret_number: # If the first reference note is located on that string and on that fret
                        chart_temp += Bass_class.char1 + '-8-' + Bass_class.char_norm + '|'  # Different colour for reference note n°1
                    elif i+1==string_number_2 and j==fret_number_2: # If the second reference note is located on that string and on that fret
                        chart_temp += Bass_class.char2 + '-8-' + Bass_class.char_norm + '|'  # Different colour for reference note n°2
                    else:
                        chart_temp += '-8-|'  # Normal colour
                        
                # For normal frets represented by a dash on the fretboard                        
                else:
                    if i+1==string_number and j==fret_number:  # If the first reference note is located on that string and on that fret
                        chart_temp += Bass_class.char1 + '---' + Bass_class.char_norm  + '|'  # Different colour for reference note n°1
                    elif i+1==string_number_2 and j==fret_number_2: # If the second reference note is located on that string and on that fret
                        chart_temp += Bass_class.char2 + '---' + Bass_class.char_norm  + '|' # Different colour for reference note n°2
                    else:
                        chart_temp += '---|'  # Normal colour
                        
            chart += chart_temp +'\n' # Adding the line corresponding to one string to the chart variable
        print(chart) # Printing the entire chart