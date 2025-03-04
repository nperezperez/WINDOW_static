import pandas as pd
import numpy as np
#subtraction distance from central platform only for the rectangular layout
#central_platform = [[498000.0 - 7000.0, 5731000.0 - 1000.0], [497000.0- 7000.0, 5731000.0 - 1000.0]]
#central_platform = [[492000.0, 5733154.0], [490000.0, 5733154.0]]
#central_platform = [[484178.55, 5714990.05000000], [485178.550000000, 5714990.05000000]] # just below the point of rotation (turbine no. 1)
central_platform = [[484178.55, 5714990], [490000, 5718000]] # just below the point of rotation and the second one a bit more to right and up (turbine no. 1)
number_turbines_per_cable = [5,5,5]
#number_turbines_per_cable = [2,4,6]

Crossing_penalty = 0
Transmission = [[central_platform[i],[463000,5918000]] for i in range(len(central_platform))]
transm_electrical_efficiency = 0.95
coll_electrical_efficiency = 0.99

change_harbour = 0
change_grid = 0

distance_to_grid = 60000.0 + change_grid # [m]
distance_to_harbour = 40000.0 + change_harbour # [m]
onshore_transport_distance = 100000.0  # [m]
frequency = 50  # [Hz]
transmission_voltage = 220000.0  # [V]
grid_coupling_point_voltage = 169000.0  # [V]


# For irregular layouts.
#layout = [[489018.67134799104, 5732481.092962526], [496876.5443383232, 5720911.583873282], [490173.3212467482, 5730172.505372626], [486690.5708014349, 5731491.683866549], [495992.77909059206, 5731247.513344433], [493586.7062148562, 5732433.198089989], [497143.0288810941, 5731888.326633343], [497178.9928514493, 5730328.123674598], [493721.5590461568, 5723567.706729419], [495429.8912377162, 5722557.995137335], [501545.06484302174, 5718413.801584703], [488107.76445797394, 5729113.066005278], [497700.48057961545, 5721343.231973487], [497613.14431458706, 5729505.256091337], [496511.4359470264, 5727865.172030598], [486477.30514128204, 5730299.821484442], [492039.1521156723, 5728011.861653671], [485854.11409825826, 5731458.321148184], [495565.88442162395, 5730564.952871052], [500842.77890160214, 5725008.960717181], [496759.19871427066, 5725113.208586694], [494787.9565470143, 5733630.495374347], [488818.7928852734, 5728357.399527002], [496804.62852301355, 5731308.784972399], [500240.3018632536, 5720557.281450064], [498556.3527848189, 5728046.607289715], [497951.6205480873, 5735696.155828064], [496618.4713281408, 5724060.51331711], [491564.2073907313, 5727538.645297818], [489803.04105169396, 5733743.980292318], [498646.3630454295, 5718725.133159074], [495721.7288682312, 5730042.3591934005], [497870.4720648653, 5727254.585517116], [496356.392833195, 5727555.994285831], [502538.4846251395, 5727725.873504472], [497772.74666698044, 5727063.550136338], [492714.0814664129, 5732330.078663796], [498748.5282998368, 5727565.460574184], [494117.7176596929, 5727098.180551026], [495249.8702888293, 5721857.916321603], [495926.9945340257, 5730680.872655159], [498353.0967371227, 5719016.682195326], [490708.9301162896, 5728509.518450938], [499836.64091457677, 5725862.242573442], [492275.2180891694, 5731466.362872274], [498896.56989206315, 5724006.897113606], [488050.30959815363, 5733006.424521751], [501195.7796733222, 5724399.632219845], [495401.14339511906, 5733870.087872595], [495702.26417546615, 5726502.8479581615], [491857.54547759774, 5727577.091735072], [495491.77891537145, 5726911.491255578], [498523.4447645283, 5730291.595432291], [489894.08079791634, 5729170.97289646], [494704.1929549164, 5729484.927716574], [495218.84837050096, 5730991.969836552], [488208.43945440673, 5733616.812026962], [495435.9520043639, 5721704.19444942], [499343.8876197888, 5726053.97786974], [501204.7991938091, 5720193.383644688], [500210.4302292379, 5720847.553993943], [495022.54955978546, 5729550.580237141], [499343.8961168045, 5737052.545925328], [499815.21295330895, 5726370.655152855], [496860.9923168109, 5727676.415624094], [489389.75176131754, 5733448.749612316], [489377.5746340195, 5727658.331114849], [493977.0989782048, 5732565.117191991], [497981.15115075576, 5728419.768548878], [497656.2016298627, 5735283.802703779], [495759.2482513679, 5734571.612351648], [489987.8598907735, 5731632.805385739], [492737.7181044308, 5735012.893803772], [488068.1860254896, 5733663.5780655155]]
# layout = [[0.0, 0.0], [882.0, 0.0], [1764.0, 0.0], [0.0, 882.0], [882.0, 882.0], [1764.0, 882.0], [0.0, 1764.0], [882.0, 1764.0], [1764.0, 1764.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]


df1 = pd.read_csv('Input/power_value.txt', header=None)
p = df1[0][0]

#### For a 1 GW farm ###

# power = [10.0, 10.99, 12.05, 12.99, 14.08, 14.93, 16.13, 17.24, 18.18, 19.23, 20.0, 22.73]
# n_t = [100, 91, 83, 77, 71, 67, 62, 58, 55, 52, 50, 44]
# print(p)
# arr = np.asarray(power)
# idx = (np.abs(arr - p)).argmin()
# N = n_t[idx]



# #### For a 600 MW farm ###
# power = [10.0, 10.53, 11.11, 11.54, 12.0, 12.5, 13.04, 14.29, 15.0, 16.22, 17.14, 18.18, 19.35, 20.0, 22.22]
# n_t = [60, 57, 54, 52, 50, 48, 46, 42, 40, 37, 35, 33, 31, 30, 27]
# print(p)
# arr = np.asarray(power)
# idx = (np.abs(arr - p)).argmin()
# N = n_t[idx]



# #### For a 800 MW farm ###

# power = [10.0, 11.11, 12.12, 12.5, 13.11, 13.56, 14.04, 14.55, 15.09, 16.0, 17.02, 18.18, 19.05, 20.0, 22.22]
# n_t = [80, 72, 66, 64, 61, 59, 57, 55, 53, 50, 47, 44, 42, 40, 36]
# print(p)
# arr = np.asarray(power)
# idx = (np.abs(arr - p)).argmin()
# N = n_t[idx]

#### For a 1 GW farm (more points) ###

power = [10.0, 10.99, 12.05, 12.99, 13.51, 14.08, 14.49, 14.93, 15.62, 16.13, 16.67, 17.24, 18.18, 19.23, 20.0, 22.73]
n_t = [100, 91, 83, 77, 74, 71, 69, 67, 64, 62, 60, 58, 55, 52, 50, 44]
print(p)
arr = np.asarray(power)
idx = (np.abs(arr - p)).argmin()
N = n_t[idx]

#### For a 1200 MW farm ###
# power = [10.0, 11.01, 12.0, 13.04, 14.12, 15.0, 15.58, 16.0, 16.67, 17.14, 17.65, 18.18, 18.46, 19.05, 20.0, 22.22]
# n_t = [120, 109, 100, 92, 85, 80, 77, 75, 72, 70, 68, 66, 65, 63, 60, 54]
# print(p)
# arr = np.asarray(power)
# idx = (np.abs(arr - p)).argmin()
# N = n_t[idx]

#### For a 1400 MW farm ###
# power = [10.0, 11.02, 12.07, 13.08, 14.0, 15.05, 16.09, 16.67, 17.07, 17.5, 18.18, 18.67, 19.18, 20.0, 22.22]
# n_t = [140, 127, 116, 107, 100, 93, 87, 84, 82, 80, 77, 75, 73, 70, 63]
# print(p)
# arr = np.asarray(power)
# idx = (np.abs(arr - p)).argmin()
# N = n_t[idx]

### for fixed area case, directly read number of turbines ###
# df1 = pd.read_csv('Input/N_t.txt', header=None)
# N = df1[0][0]

#filename = 'Input/Rectangular_layout_' + str(N) + 'turbines_4D.dat'
#filename = 'Input/Rectangular_layout_' + str(N) + 'turbines_5D.dat'
#filename = 'Input/Rectangular_layout_' + str(N) + 'turbines_6D.dat'
#filename = 'Input/Rectangular_layout_' + str(N) + 'turbines_7D.dat'
#filename = 'Input/1400MW/Rectangular_layout_' + str(N) + 'turbines_7D.dat'
#filename = 'Input/Rectangular_layout_' + str(N) + 'turbines_8D.dat'
#filename = 'Input/Rectangular_layout_' + str(N) + 'turbines_9D.dat'
#print(filename)
#filename = 'Input/Rectangular_layout_' + str(N) + 'turbines_area200.dat'
#filename = 'Input/700MW/Rectangular_layout_' + str(N) + 'turbines_700MW.dat'



filename = 'Input/Square_layout_' + str(N) + 'turbines_baseline.dat'
# filename = 'Input/Square_layout_' + str(N) + 'turbines_1200MW.dat'
# filename = 'Input/Square_layout_' + str(N) + 'turbines_area200.dat'
#filename = 'Input/Fixedarea_150/spacing_5D/Square_layout_' + str(N) + 'turbines_area150.dat'
# filename = 'Input/Fixedpower/Square_layout_' + str(N) + 'turbines_5D.dat'

# Use only in case of a standard rectangular layout. Built using standard spacing for HKW and the IEA 15 MW -240 m turbine
df = pd.read_csv(filename, delimiter=' ')


layout = []
for index, rows in df.iterrows():
    # Create list for the current row
    my_list = [rows.x, rows.y]
    # append the list to the final list
    layout.append(my_list)


n_turbines = len(layout)



max_n_turbines = n_turbines

number_substations = 2
max_n_substations = 2
max_n_branches = max_n_turbines_p_branch = max_n_turbines
cable_types = [[95, 300, 206], [120, 340, 221], [150, 375, 236], [185, 420, 256], [240, 480, 287], [300, 530, 316], [400, 590, 356], [500, 655, 406], [630, 715, 459], [800, 775, 521], [1000, 825, 579]]  # List of cable types: [Cross section [mm^2], Capacity [A], Cost [EUR/m]] in increasing order (maximum 3 cable types)

#cable_types = [[95, 410, 206], [120, 465, 221], [150, 520, 236], [185, 585, 256], [240, 670, 287], [300, 750, 316], [400, 840, 356], [500, 940, 406], [630, 1050, 459], [800, 1160, 521], [1000, 1265, 579]]  # List of cable types: [Cross section [mm^2], Capacity [A], Cost [EUR/m]] in increasing order (maximum 3 cable types)
#https://new.abb.com/docs/default-source/ewea-doc/xlpe-submarine-cable-systems-2gm5007.pdf





# For regular layouts only use the parameters below.
downwind_spacing = 2100.0  # [m]
crosswind_spacing = 1000.0  # [m]
odd_row_shift_spacing = 0.0  # [m] How many meters to shift every other row in the crosswind direction.
layout_angle = 30.0  # [m] Rotation angle of the entire layout.
