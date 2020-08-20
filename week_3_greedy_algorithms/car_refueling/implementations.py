def fast_algorithm(self, *args, **kwargs):
    distance = kwargs.get("distance")
    tank_cap = kwargs.get("tank_cap")
    stations = kwargs.get("stations")

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


def working_algorithm(self, *args, **kwargs):
    distance = kwargs.get("distance")
    tank_cap = kwargs.get("tank_cap")
    stations = kwargs.get("stations")

    result = "awesome"

    return result
