# File created by Leonardo Cencetti on 1/29/21
import argparse
import glob
import os
import re
from datetime import datetime

template = '([0-9]+)'

parser = argparse.ArgumentParser(
    description='Renames SVG plots downloaded from flight-review with their correct title. Works only if you download all plots sequentially, MAIN + PID, using SVG Crowbar 2. Copy this script in the same folder as the plots.')
parser.add_argument('--real', action='store_true', help='Whether the files are coming from a real or simulated drone')
args = parser.parse_args()

name_map = [
    'gps_position',
    'altitude_estimate',
    'roll_angle',
    'roll_angular_rate',
    'pitch_angle',
    'pitch_angular_rate',
    'yaw_angle',
    'yaw_angular_rate',
    'local_position_x',
    'local_position_y',
    'local_position_z',
    'velocity',
    'actuator_controls_0',
    'actuator_outputs',
    'raw_acceleration',
    'vibration_metrics',
    'acceleration_power_spectral_density',
    'raw_angular_speed',
    'raw_magnetic_field_strength',
    'gps_uncertainty',
    'gps_noise_and_jamming',
    'thrust_and_magnetic_field',
    'power',
    'temperature',
    'estimator_watchdog',
    'rc_quality',
    'sampling_regularity',
    'pid_roll_angular_rate',
    'pid_step_response_roll_rate',
    'pid_pitch_angular_rate',
    'pid_step_response_pitch_rate',
    'pid_yaw_angular_rate',
    'pid_step_response_yaw_rate',
    'pid_step_response_roll_angle',
    'pid_step_response_pitch_angle'
]

if args.real:
    name_map.insert(12, 'manual_control_input')
    name_map.insert(14, 'actuator_outputs_aux')
    name_map.insert(26, 'cpu_ram')

now = datetime.now()

current_time = now.strftime("%H_%M_%S")
os.mkdir(current_time)
for f in glob.glob("*.svg"):
    id = 0
    if match := re.search(template, f):
        id = int(match.group(1))

    os.rename(f, current_time + '/' + str(id) + '_' + name_map[id] + '.' + f.rsplit('.', 1)[1])

