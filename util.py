import math

def calculer_distance(point1, point2):
    """
    Calcule la distance euclidienne entre deux points sur la terre spécifiés par latitude/longitude.
    Les points sont censés être des tuples de (latitude, longitude).
    Notez que cette fonction ne prend pas en compte la courbure de la Terre. Cependant, si l'objectif est de comparer 
    des distances les unes avec les autres plutôt que de chercher une distance absolue exacte, cette simplification 
    ne devrait pas poser de problème.

    Args:
    point1 (tuple): Un tuple contenant la latitude et la longitude du premier point.
    point2 (tuple): Un tuple contenant la latitude et la longitude du deuxième point.

    Returns:
    float: La distance euclidienne entre les deux points.
    """
    lat1, lon1 = point1
    lat2, lon2 = point2

    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

def trouver_station_proche(lat, lon, stations):
    """
    Trouve la station la plus proche d'un point donné.

    Args:
    lat (float): La latitude du point.
    lon (float): La longitude du point.
    stations (pandas.DataFrame): Un DataFrame contenant les informations des stations, avec des colonnes "Latitude" et "Longitude".

    Returns:
    pandas.Series: La ligne du DataFrame correspondant à la station la plus proche.
    """
    distances = stations.apply(lambda station: calculer_distance((lat, lon), (station['Latitude'], station['Longitude'])), axis=1)
    index_station_proche = distances.idxmin()
    return stations.loc[index_station_proche]