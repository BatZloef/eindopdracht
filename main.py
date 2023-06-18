import pickle
from System import *

def main():
    try:
        with open('pickle.data', 'rb') as f:
            verder_string = input("\nDruk 'v' om verder te gaan op de vorige situatie of 'o' om opnieuw te beginnen:")
            if verder_string == "v":
                app = pickle.load(f) 
            else:
                app = System()
    except FileNotFoundError:
        app = System()
    app.terminal()
    with open("pickle.data", "wb") as f:
        pickle.dump(app, f)

def maak_txt(file_path, data):
    with open(file_path, "w") as f:
        f.write(data)

file_path = "requirements.txt"
data = "Gebruikte libraries:\n  -pickle\n   -random\n   -folium\n  -geojson\n   -webbrowser"

main()    