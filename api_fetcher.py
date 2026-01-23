import requests 
import json 

def menu():
	print("Menu:")
	print("1. View all users")
	print("2. View selected user")
	print("3. View selected user's posts")
	print("4. Exit")
	choice = int(input("Input your choice: "))

def fetch_users():
	print("All users:")
	for user in users: 
		if "id" in user and "name" in user:
			print(f"{index}. Name: {user['name']}, Id: {user['Id']}")

def fetch_user_details(user):
	id_choice = int(input("Enter user Id: "))
	print("User details:")
	
	
	

print("Welcome to reminisce's api fetcher!")
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    response.raise_for_status()
    users = response.json()
except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")
except requests.exceptions.ConnectionError:
    print("Connection error. Check your internet.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

while True:
	menu()
	if choice == 1:
		fetch_users()

	elif choice == 2:
		
		

	elif choice == 3:

	else:
		print("Thanks for using reminisce's api fetcher")
		break
	
	

