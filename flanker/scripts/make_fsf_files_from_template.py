import os
import glob

# find list of all participant folders
participant_list = glob.glob('../sub-*')

# order the participants
participant_list.sort()

# removing the `../`
for i in range(len(participant_list)):
    participant_list[i] = participant_list[i].replace('../', '')

run_list = ['run-1', 'run-2']


template_fsf = 'level_1_template.fsf'

# nested loop -- do this for each participant, for each run
for participant in participant_list:
    for run in run_list:
        # define the path of the output fsf file
        participant_run_specific_fsf = f'fsf_files/{participant}_{run}_level1.fsf'

        # define what to replace in the template
        replacements = {"SUBNUM":participant, 
                        'RUN_NUM': run}
        with open(template_fsf) as infile: 
            # outfile = useable fsf file that is being created for every subject and every run 
            with open(participant_run_specific_fsf, 'w') as outfile:
                for line in infile:
                    # This code will make new fsf files that replace all of the wild cards we made above!  
                    for src, target in replacements.items():
                        line = line.replace(src, target)
                    outfile.write(line)