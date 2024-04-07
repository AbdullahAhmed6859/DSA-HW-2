def create_flight_network(filename: str, option: int):
    G = {}
    index = option + 1
    with open(filename, 'r') as file:
        # ignore the first line
        next(file)

        for line in file:
            dat = line.strip().split(",")
            # choose the right weight from duration and destination
            origin, destination, weight = dat[:2] + [dat[index]]

            # add the edge to the graph
            if origin not in G:
                G[origin] = []
            G[origin].append((destination, int(weight)))

    return G


def get_flight_connections(
        graph: dict[str, list[tuple[str, int]]], city: str, option: str) -> list:

    flights = graph.get(city)
    # if flight is not in city return empty list
    if not flights:
        return []

    # if outbound flights then return the cities from the cities from the
    # (city, weight) list
    if option == "o":
        return [x[0] for x in flights]

    # if inbound flights then loop through the graph
    out = []
    for origin, flight in graph.items():
        for destination, _ in flight:
            # if this origin has a connection with the input city then add to
            # the output list
            if destination == city:
                out.append(origin)
                break
    return out


def get_number_of_flight_connections(
        graph: dict[str, list[tuple[str, int]]],
        city: str,
        option: str) -> int:

    # if outbound calculate length of the (city, weight) edges list
    if option == "o":
        flights = graph.get(city, [])
        return len(flights)

    # if outbound then count the number of cities whihc have connection to the
    # input city
    count = 0
    for origin, flight in graph.items():
        if city == origin:
            continue
        # loop thorugh edges of the city to see if it has connection with the
        # input city
        for destination, _ in flight:
            if destination == city:
                count += 1
                break
    return count


def get_flight_details(graph: dict[str, list[tuple[str, int]]],
                       origin: str, destination: str) -> int:
    flights = graph.get(origin)
    if not flights:
        return None

    # return the weight of the flight if it exists else -1
    for city, weight in flights:
        if city == destination:
            return weight
    return -1


def add_flight(graph: dict[str, list[tuple[str, int]]], origin: str,
               destination: str, weight: int):
    flights = graph.get(origin)
    # if either destination or origin does not exost then give suitable output
    if not flights:
        print(f"{origin} is not accessed by the flight network")
        return
    if destination not in graph:
        print(f"{destination} is not accessed by the flight network")
        return

    # loop through the graph and if the flight to destination exists update its
    # weight
    for i, (city, _) in enumerate(flights):
        if city == destination:
            flights[i] = (destination, weight)
            return

    # else just add the new flight
    flights.append((destination, weight))


def add_airport(graph: dict[str, list[tuple[str, int]]], city: str,
                destination: str, weight: int):
    if city in graph:
        print("Airport Already exists")
        return
    elif destination not in graph:
        print("Destination is not in the graph")

    # create the airport and add the flight to destination
    graph[city] = [(destination, weight)]


def get_secondary_flights(graph: dict[str, list[tuple[str, int]]], city: str):
    flights = graph.get(city)
    # if city does not exist return None
    if not flights:
        return

    out = []
    # loop through edges of the first city
    for (city1, _) in flights:
        # loop through edges edges of second city
        for city2, _ in graph[city1]:
            # add these cities to ouptu list
            if city2 not in out:
                out.append(city2)
    return out


def counting_common_airports(
        graph: dict[str, list[tuple[str, int]]], cityA: str, cityB: str) -> int:
    # convert to list of outgoing edges to set of cities and find the
    # length of it's intersection
    return len(set(city for city, _ in graph.get(cityA, [])) &
               set(city for city, _ in graph.get(cityB, [])))


def remove_flight(
        graph: dict[str, list[tuple[str, int]]], origin: str, destination: str):
    # Remove the destination from the origin's list of flights
    if origin in graph:
        graph[origin] = [(city, weight)
                         for city, weight in graph[origin] if city != destination]

    # Remove the origin from the destination's list of flights
    if destination in graph:
        graph[destination] = [(city, weight) for city, weight
                              in graph[destination] if city != origin]


def remove_airport(graph: dict[str, list[tuple[str, int]]], city: str):
    # Remove the city from the graph
    graph.pop(city, None)

    # Remove the city from the destination lists of other cities
    for origin in graph:
        graph[origin] = [(destination, weight) for destination,
                         weight in graph[origin] if destination != city]


def DFS_all_routes(
        graph: dict[str, list[tuple[str, int]]],
        origin: str,
        destination: str,
        route: list,
        all_routes: list[list[str]]) -> None:
    
    # add the origin to the route
    route.insert(len(route), origin)

    if origin == destination:
        # add route to the all routes
        all_routes.append(route.copy())

    else:
        # for outbound connection airports of origin
        for airport, _ in graph.get(origin, []):
            if airport in route:
                continue
            DFS_all_routes(graph, airport, destination, route, all_routes)

    route.remove(origin)


def find_all_routes(graph: dict[str, list[tuple[str, int]]],
                    origin: str, destination: str) -> list[list[str]]:

    if origin not in graph or destination not in graph:
        return None
    elif origin is destination:
        return []

    # get output from DFS all routes
    DFS_all_routes(graph, origin, destination, [], routes := [])
    return routes


def DFS_layovers(graph: dict[str, list[tuple[str, int]]],
                 origin: str,
                 destination: str,
                 route: list,
                 layovers_lst: list):

    # add origin to the DFS
    route.insert(len(route), origin)
    
    if origin == destination:
        # add length of the route to output list
        layovers_lst.append(len(route))
    else:
        # for outbound connection airports of origin
        for airport, _ in graph.get(origin, []):
            if airport in route:
                continue
            DFS_layovers(graph, airport, destination, route, layovers_lst)

    route.remove(origin)


def find_number_of_layovers(
        graph: dict[str, list[tuple[str, int]]], origin: str, destination: str) -> list[list[str]]:
    if origin not in graph or destination not in graph:
        return None
    elif origin is destination:
        return []

    DFS_layovers(graph, origin, destination, [], layovers := [])
    # subtract 2 from all layovers 
    return sorted([x - 2 for x in layovers if x >= 2])