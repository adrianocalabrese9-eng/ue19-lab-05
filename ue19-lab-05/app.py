import requests
import json

def get_random_joke():
    """Récupère une blague aléatoire depuis l'API JokeAPI"""
    try:
        url = "https://v2.jokeapi.dev/joke/Any?type=single"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        joke_data = response.json()
        
        if joke_data.get("error", False):
            return "Désolé, aucune blague disponible pour le moment."
        
        return joke_data.get("joke", "Blague non disponible")
        
    except requests.exceptions.RequestException as e:
        return f"Erreur de connexion: {e}"
    except json.JSONDecodeError:
        return "Erreur lors du traitement de la réponse"

def main():
    """Fonction principale"""
    print("=== Générateur de Blagues ===")
    print("Chargement d'une blague aléatoire...")
    print()
    
    joke = get_random_joke()
    print(f"🤡 {joke}")
    print()
    print("Bonne journée! 😊")

if __name__ == "__main__":
    main()
