import glob
import os

# find list of all participant folders
participant_list = glob.glob('../sub-*')

# order the participants
participant_list.sort()


# run bet to skullstrip: bet <input> <output> [options]

# loop through participants
for participant in participant_list:
    participant_id = participant.replace('../', '')
    input = f'{participant}/anat/{participant_id}_T1w.nii.gz'
    output = f'{participant}/anat/{participant_id}_T1w_brain.nii.gz'
    cmd = f'bet {input} {output}'
    os.system(cmd)