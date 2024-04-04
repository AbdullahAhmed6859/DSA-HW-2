def addVertices(G: dict, vertices: list):
    for vertex in vertices:
        if vertex not in G:
            G[vertex] = []


def addEdges(G: dict, edges: list):
    for edge in edges:
        if edge[0] not in G:
            G[edge[0]] = []
        G[edge[0]].append((edge[1], edge[2]))


def create_flight_network(filename: str, option: int):
    G = {}
    with open(filename, 'r') as file:
        next(file)  # skip the field names
        for line in file:
            data = line.strip().split(",")
            origin, destination = data[0], data[1]
            weight = int(data[option + 1])

            if origin not in G:
                G[origin] = []
            G[origin].append((destination, weight))

    return G


def get_flight_connections(graph: dict, city: str, option: str) -> list:
    flights = graph.get(city)
    if not flights:
        return []

    if option == "o":
        return [x[0] for x in flights]

    out = []
    for origin, flight in graph.items():
        # if city == origin:
        #     continue
        for destination, _ in flight:
            if destination == city:
                out.append(origin)
                break
    return out


def get_number_of_flight_connections(
        graph: dict,
        city: str,
        option: str) -> int:
    if option == "o":
        flights = graph.get(city)
        return len(flights) if flights else 0

    count = 0
    for origin, flight in graph.items():
        if city == origin:
            continue
        for destination, _ in flight:
            if destination == city:
                count += 1
                break
    return count


def get_flight_details(graph: dict, origin: str, destination: str) -> int:
    flights = graph.get(origin)
    if not flights:
        return None
    for city, weight in flights:
        if city == destination:
            return weight
    return -1


def add_flight(graph: dict, origin: str, destination: str, weight: int):
    flights = graph.get(origin)
    if not flights:
        print(f"{origin} is not accessed by the flight network")
        return
    if destination not in graph:
        print(f"{destination} is not accessed by the flight network")
        return

    for i, (city, _) in enumerate(flights):
        if city == destination:
            flights[i] = (destination, weight)
            return

    flights.append((destination, weight))


def add_airport(graph: dict, city: str, destination: str, weight: int):
    if city in graph or destination not in graph:
        print("Airport Already exists")
        return
    graph[city] = [(destination, weight)]


def get_secondary_flights(graph: dict, city: str):
    flights = graph.get(city)
    if not flights:
        return

    out = []
    for (city1, _) in flights:
        for city2, _ in graph[city1]:
            if city2 not in out:
                out.append(city2)
    return out


def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    flights_A, flights_B = graph[cityA], graph[cityB]
    return len(list(set(flights_A + flights_B)))


def remove_flight(graph: dict, origin: str, destination: str):
    # Remove the destination from the origin's list of flights
    if origin in graph:
        graph[origin] = [(city, weight)
                         for city, weight in graph[origin] if city != destination]

    # Remove the origin from the destination's list of flights
    if destination in graph:
        graph[destination] = [(city, weight) for city,
                              weight in graph[destination] if city != origin]


def remove_airport(graph: dict, city: str):
    # Remove the city from the graph
    graph.pop(city, None)

    # Remove the city from the destination lists of other cities
    for origin in graph:
        graph[origin] = [(destination, weight) for destination,
                         weight in graph[origin] if destination != city]


def DFS_all_routes(
        graph: dict,
        origin: str,
        destination: str,
        route: list,
        all_routes: list):
    pass


def find_all_routes(graph: dict, origin: str, destination: str):
    if origin not in graph or destination not in graph:
        return None
    edges = graph[origin]


def DFS_layovers(
        graph: dict,
        origin: str,
        destination: str,
        route: list,
        layovers_lst: list):
    pass


def find_number_of_layovers(graph: dict, origin: str, destination: str):
    pass
