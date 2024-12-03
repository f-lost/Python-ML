import requests
import json


def coordinate_città(città_nome):
    """Restituisce le coordinate GPS (latitudine, longitudine) per una città data."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={città_nome}&count=1&language=en&format=json"
    
    response = requests.get(url)
    data = response.json()

    # Verifica che ci siano risultati nella risposta
    if 'results' in data and data['results']:
        città_data = data['results'][0]
        latitudine = città_data['latitude']
        longitudine = città_data['longitude']
        print(f"Coordinate di {città_nome}: Latitudine {latitudine}, Longitudine {longitudine}")
        return latitudine, longitudine
    else:
        print("Città non trovata.")
        return None, None


# Inizializzazione delle variabili
precipitazioni = ""
vento = ""

# Richiesta dell'opzione per le precipitazioni
scelta_precipitazioni = input("Vuoi mostrare le probabilità di precipitazione?: (Y/N)").lower()
if scelta_precipitazioni == "y":
    precipitazioni = ",precipitation_probability"

# Richiesta dell'opzione per la velocità del vento
scelta_vento = input("Vuoi mostrare la velocità del vento?: (Y/N)").lower()
if scelta_vento == "y":
    vento = ",wind_speed_10m"

# Ciclo per chiedere il numero di giorni da mostrare (1, 3, 7)
choice = True
while choice:
    scelta = int(input("Quanti giorni vuoi mostrare?: (1/3/7)"))
    if scelta in [1, 3, 7]:
        giorni = scelta
        choice = False
    else:
        print("Giorni non supportati.")

# Richiesta del nome della città
città = input("Inserisci una città: ").lower()

# Ottieni le coordinate della città
latitudine, longitudine = coordinate_città(città)

# Costruzione del link per ottenere i dati meteo
link = f"https://api.open-meteo.com/v1/forecast?latitude={latitudine}&longitude={longitudine}&hourly=temperature_2m{precipitazioni}{vento}&forecast_days={giorni}"

# Esegui la richiesta per ottenere i dati meteo
risposta = requests.get(link)

# Verifica che la risposta sia corretta
if risposta.status_code != 200:
    print("ERRORE")
else:
    risposta_text = risposta.text
    risposta_json = json.loads(risposta_text)

    # Stampa i dati meteo in base alle scelte dell'utente
    if scelta_vento == "y" and scelta_precipitazioni == "y":
        print("data/ora \t probabilità di precipitazione (%) \t velocità vento (km/h) \t temperatura (C°)")
        for i in range(len(risposta_json["hourly"]["time"])):
            print(risposta_json["hourly"]["time"][i], "\t", risposta_json["hourly"]["precipitation_probability"][i], "\t",
                  risposta_json["hourly"]["wind_speed_10m"][i], "\t", risposta_json["hourly"]["temperature_2m"][i])

    elif scelta_vento != "y" and scelta_precipitazioni == "y":
        print("data/ora \t probabilità di precipitazione (%) \t temperatura (C°)")
        for i in range(len(risposta_json["hourly"]["time"])):
            print(risposta_json["hourly"]["time"][i], "\t", risposta_json["hourly"]["precipitation_probability"][i], "\t",
                  risposta_json["hourly"]["temperature_2m"][i])

    elif scelta_vento != "y" and scelta_precipitazioni != "y":
        print("data/ora \t temperatura (C°)")
        for i in range(len(risposta_json["hourly"]["time"])):
            print(risposta_json["hourly"]["time"][i], "\t", risposta_json["hourly"]["temperature_2m"][i])

    elif scelta_vento == "y" and scelta_precipitazioni != "y":
        print("data/ora \t velocità vento (km/h) \t temperatura (C°)")
        for i in range(len(risposta_json["hourly"]["time"])):
            print(risposta_json["hourly"]["time"][i], "\t", risposta_json["hourly"]["wind_speed_10m"][i], "\t",
                  risposta_json["hourly"]["temperature_2m"][i])