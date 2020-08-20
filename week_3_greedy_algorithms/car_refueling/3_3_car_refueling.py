# python3
import sys


def compute_min_refills(distance, tank, stops):
    distance = distance
    tank_cap = tank
    stations = stops

    stops = 0
    stations_reversed = sorted(stations, reverse=True)
    last_station = 0

    # can make it without stop
    if tank_cap - distance >= 0:
        return 0

    while distance >= 0:
        made_station = False
        for i, station in enumerate(stations_reversed):
            if (last_station + tank_cap) - station >= 0:
                # decrease distance
                distance -= station

                # remove all stations not needed
                stations_reversed = stations_reversed[0:i]

                # set last station stop
                last_station = station

                # increase stops
                stops += 1

                # set made it to a station
                made_station = True
                break

        if not made_station:
            return -1

    return stops


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
