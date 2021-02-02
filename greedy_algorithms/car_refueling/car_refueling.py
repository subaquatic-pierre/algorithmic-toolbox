# python3
import sys


def compute_min_refills(distance, tank, stops):
    distance = distance
    tank_cap = tank
    stations = stops

    dist = distance
    miles = tank
    gas_stations = stations
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


if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
