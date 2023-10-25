import requests

def fetch_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se la richiesta ha avuto successo

        # Restituisci il contenuto della pagina
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Si è verificato un errore durante la richiesta: {e}"

if __name__ == "__main__":
    url = input("Inserisci l'URL della pagina web: ")
    webpage_content = fetch_webpage_content(url)

    print("Contenuto della pagina:")
    print(webpage_content)
