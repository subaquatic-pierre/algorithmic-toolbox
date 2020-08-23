def fast_algorithm(self, *args, **kwargs):
    distance = kwargs.get("distance")
    tank_cap = kwargs.get("tank_cap")
    stations = kwargs.get("stations")

    stops = 0
    stations_reversed = sorted(list(set(stations)), reverse=True)
    last_station = 0
    original_distance = distance

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

                if last_station + tank_cap >= original_distance:
                    return stops

                break

        if not made_station:
            return -1

    return stops


def working_algorithm(self, *args, **kwargs):
    dist = kwargs.get("distance")
    miles = kwargs.get("tank_cap")
    gas_stations = kwargs.get("stations")
    n = len(gas_stations)

    num_refill, curr_refill, limit = 0, 0, miles
    while limit < dist:  # While the destination cannot be reached with current fuel
        if curr_refill >= n or gas_stations[curr_refill] > limit:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while curr_refill < n - 1 and gas_stations[curr_refill + 1] <= limit:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        limit = gas_stations[curr_refill] + miles  # Fill up the tank
        curr_refill += 1

    result = num_refill

    return result
