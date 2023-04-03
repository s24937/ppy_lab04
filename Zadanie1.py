import math


def panel_calc(len_floor, wid_floor, len_panel, wid_panel, num_panel_in_package):
    floor_area = (wid_floor * len_floor) * 1.1
    panel_area = (wid_panel * len_panel)
    number_of_panels = floor_area / panel_area
    return "" + str(math.ceil(number_of_panels / num_panel_in_package)) + ""


print("Potrzeba : " + str(panel_calc(4, 4, 1, 0.20, 10)))
