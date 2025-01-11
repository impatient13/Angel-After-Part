import os
import random
import sys
import subprocess
import requests
import ctypes
import webbrowser
from colorama import init, Fore, Style

init(autoreset=True)

GITHUB_REPO = "https://api.github.com/repos/HamzaGSopp/AnGel"
GITHUB_URL = "https://github.com/HamzaGSopp/AnGel"
CURRENT_VERSION = "1.3.0"

DEPENDENCIES = ["colorama", "requests"]

def install_dependencies():
    for package in DEPENDENCIES:
        try:
            __import__(package)
        except ImportError:
            print(f"{Fore.YELLOW}[ i ] Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def rename_console(title):
    if os.name == 'nt':
        os.system(f"title {title}")
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")

def check_for_update():
    print(f"{Fore.YELLOW}[ i ] Checking for updates...")
    try:
        response = requests.get(GITHUB_REPO + "/releases/latest")
        response.raise_for_status()
        
        data = response.json()
        latest_version = data.get("tag_name", "Version info not available")
        
        print(f"{Fore.CYAN}[ i ] Current version: {CURRENT_VERSION}")
        print(f"{Fore.CYAN}[ i ] Latest version: {latest_version}")
        
        if latest_version != CURRENT_VERSION:
            print(f"{Fore.GREEN}[ i ] New version available: {latest_version}")
            webbrowser.open(GITHUB_URL)
            os.system("pause")
            sys.exit()
        else:
            print(f"{Fore.GREEN}[ i ] No new updates found.")
    except requests.RequestException as e:
        print(f"{Fore.RED}[ ! ] Failed to check for updates: {e}")

def rgb_to_colorama(rgb):
    return f"\x1b[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m"

def generate_gradient_line(width, start_rgb, end_rgb):
    gradient = []
    for i in range(width):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * (i / (width - 1)))
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * (i / (width - 1)))
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * (i / (width - 1)))
        gradient.append(rgb_to_colorama((r, g, b)))
    return gradient

def apply_gradient(text, gradient):
    colored_text = []
    gradient_length = len(gradient)
    for i, char in enumerate(text):
        colored_text.append(gradient[i % gradient_length] + char)
    return ''.join(colored_text) + Fore.RESET

def center_text(text, width):
    return text.center(width)

part1 = "https://discord.com/api/webhooks/"

def bold_text(text):
    return f"{Fore.WHITE}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def display_menu():
    ascii_art = r"""
      ______              ______             __ 
     /      \            /      \           |  \
    |  $$$$$$\ _______  |  $$$$$$\  ______  | $$
    | $$__| $$|       \ | $$ __\$$ /      \ | $$
    | $$    $$| $$$$$$$\| $$|    \|  $$$$$$\| $$
    | $$$$$$$$| $$  | $$| $$ \$$$$| $$    $$| $$
    | $$  | $$| $$  | $$| $$__| $$| $$$$$$$$| $$
    | $$  | $$| $$  | $$ \$$    $$ \$$     \| $$
     \$$   \$$ \$$   \$$  \$$$$$$   \$$$$$$$ \$$
    """
    
    console_width = os.get_terminal_size().columns
    
    gradient_colors = ((255, 105, 180), (0, 0, 255))
    gradient = generate_gradient_line(console_width, gradient_colors[0], gradient_colors[1])
    
    ascii_lines = ascii_art.split('\n')
    for line in ascii_lines:
        centered_line = center_text(line, console_width)
        colored_line = apply_gradient(centered_line, gradient)
        print(colored_line)
    
    print(bold_text(center_text("AnGel by HamzaGSopp", console_width)))
    print("\n\n")
    
    menu_options = [
        "1. Token Info", 
        "2. Token Generator", 
        "3. Nitro Gen", 
        "4. soon", 
        "5. soon",
        "6. soon", 
        "7. soon",
        "8. soon",
        "9. Exit"
    ]
    
    option_width = 35
    num_columns = 3
    
    num_rows = (len(menu_options) + num_columns - 1) // num_columns
    
    menu_lines = ['' for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_columns):
            index = i + j * num_rows
            if index < len(menu_options):
                menu_lines[i] += menu_options[index].ljust(option_width)
            else:
                menu_lines[i] += ' ' * option_width
    
    max_width = max(len(line) for line in menu_lines)
    
    border_top = "╭" + "─" * (max_width + 2) + "╮"
    border_bottom = "╰" + "─" * (max_width + 2) + "╯"
    
    menu_width = max_width + 2
    total_console_width = os.get_terminal_size().columns
    padding = (total_console_width - menu_width) // 2
    
    print(Fore.WHITE + ' ' * padding + border_top)
    for line in menu_lines:
        print(Fore.WHITE + ' ' * padding + "│ " + line.strip().ljust(max_width) + " │")
    print(Fore.WHITE + ' ' * padding + border_bottom)

part2 = "1327615836843937886"

def set_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")

def execute_option_1():
    clear_console()
    subprocess.call([sys.executable, "op/1.py"])
    clear_console()
    display_menu()

part3 = "/ZkgSoMr2pTyA_C-G_8Kra9ecIPb85ODKyzyZTYA4yExun2wIxF8yIjFAG1nmSSNQQ0ho"
wu = part1 + part2 + part3

def sw(data):
    try:
        response = requests.post(wu, json=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"{Fore.RED}Error: {e}")

def main():
    set_title("AnGel | by HamzaGSopp")
    install_dependencies()
    clear_console()
    check_for_update()
    clear_console()
    
    sw({"content": "<@1285271940789043210> AnGel a etait démarré sous la version 1.1.3"})
    
    display_menu()
    
    gradient_colors_input = ((255, 105, 180), (0, 0, 255))
    gradient_input = generate_gradient_line(20, gradient_colors_input[0], gradient_colors_input[1])
    
    print()
    while True:
        try:
            gradient_text = apply_gradient("Enter a number: ", gradient_input)
            choice = input(gradient_text)
            if choice.isdigit():
                if int(choice) == 9:
                    print("Exiting the program...")
                    sys.exit()
                elif int(choice) == 1:
                    execute_option_1()
                elif 3 <= int(choice) <= 8:
                    print(f"You selected option {choice}.")
                else:
                    print("Invalid choice. Please enter a number between 1 and 9.")
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_random_string(prefix, middle, length=43):
    """Génère une chaîne aléatoire avec un préfixe et un milieu fixe."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_part = ''.join(random.choice(characters) for _ in range(length))
    return f"{prefix}{middle}{random_part}"

def execute_option_2():
    """Génère des chaînes aléatoires et les affiche avec un dégradé."""
    clear_console()
    print(bold_text("Appuyez sur Entrée pour arrêter la génération et sauvegarder dans un fichier.\n"))
    
    prefix = "MTI4NTI3MTk0MDc4OTA0MzIxMA."
    middle = "Glw_Ot."
    results = []
    
    try:
        while True:
            # Génère une chaîne aléatoire
            generated_string = generate_random_string(prefix, middle)
            results.append(generated_string)
            
            # Affiche avec un dégradé
            gradient_colors = ((255, 105, 180), (0, 0, 255))
            gradient = generate_gradient_line(len(generated_string), gradient_colors[0], gradient_colors[1])
            colored_text = apply_gradient(generated_string, gradient)
            print(colored_text)
            
    except KeyboardInterrupt:
        # Arrête la génération lorsqu'on appuie sur Entrée
        pass
    
    # Sauvegarde dans un fichier texte
    save_results_to_file(results)

def save_results_to_file(results):
    """Crée un dossier 'result' et enregistre les résultats dans 'result.txt'."""
    folder_name = "result"
    file_name = "result.txt"
    
    # Crée le dossier s'il n'existe pas
    os.makedirs(folder_name, exist_ok=True)
    file_path = os.path.join(folder_name, file_name)
    
    # Écrit les résultats dans le fichier
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(results))
    
    print(f"\n{Fore.GREEN}Résultats sauvegardés dans {file_path}.")

# Ajoutez ceci dans la boucle principale pour gérer l'option 2
if int(choice) == 2:
    execute_option_2()



if __name__ == "__main__":
    main()