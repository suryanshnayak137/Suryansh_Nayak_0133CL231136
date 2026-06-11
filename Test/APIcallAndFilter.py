
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        users = response.json()

        print(f"Status Code: {response.status_code} OK\n")
        print("Users from Gwenborough:")
        print("-" * 40)

        for user in users:
            if user["address"]["city"] == "Gwenborough":
                print(f"Name    : {user['name']}")
                print(f"Email   : {user['email']}")
                print(f"Phone   : {user['phone']}")
                print(f"Company : {user['company']['name']}")
                print("-" * 40)
    else:
        print(f"Failed. Status code: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Error: No internet connection.")
except requests.exceptions.Timeout:
    print("Error: Request timed out.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")