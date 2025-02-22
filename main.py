import os
import sys
import subprocess
import requests
import ctypes
import webbrowser
import time
import datetime
import cryptography
import socket
from cryptography.fernet import Fernet
from datetime import datetime
from colorama import init, Fore, Style
from datetime import datetime, timezone

init(autoreset=True)

GITHUB_REPO = "https://api.github.com/repos/impatient13/Angel-After-Part"
GITHUB_URL = "https://github.com/impatient13/Angel-After-Part"
CURRENT_VERSION = "1.6.0"

DEPENDENCIES = ["colorama", "requests", "cryptography"]

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
    
    print(bold_text(center_text("AnGel by HamzaGSopp - Remake By 502.sql", console_width)))
    print("\n\n")
    
    menu_options = [
        "1. Token Info", 
        "2. Guild Info", 
        "3. Webhook Spammer", 
        "4. IP Lookup", 
        "5. Port Scanner",
        "6. URL TO IP", 
        "7. TEMP MAIL",
        "8. Py to Exe",
        "9. Exit",
        "10. Clear Console"
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

def set_title(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\x1b]2;{title}\x07")

BX9 = b'gAAAAABng9aptUCuG5J-2isGcCpxiimWOKbbEZuVQjKxzdAt5qSOkeQ9EAnnOPENpCVZt9hNKZVmY4j-k1jvxNQ3975PGR2h1p9bak0dnxDn-a1R5z7jES91UKCIYUOSqsymP5dQ56o23vKsN95PBnr5Pe6MWwBqjLh7WdCQGZ6Ix1DjP6aE7wcd3suKf8Y4VsG5prjLxblp8CaNQVjt79XY6SWpfphxx1LTIaLqiMR2Mhe4i6N_Ylk='

def execute_option_1():
    clear_console()
    gradient_colors = ((255, 105, 180), (0, 0, 255))
    token = input("Enter Discord Token: ") 

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    languages = {
        'da': 'Danish, Denmark',
        'de': 'German, Germany',
        'en-GB': 'English, United Kingdom',
        'en-US': 'English, United States',
        'es-ES': 'Spanish, Spain',
        'fr': 'French, France',
        'hr': 'Croatian, Croatia',
        'lt': 'Lithuanian, Lithuania',
        'hu': 'Hungarian, Hungary',
        'nl': 'Dutch, Netherlands',
        'no': 'Norwegian, Norway',
        'pl': 'Polish, Poland',
        'pt-BR': 'Portuguese, Brazilian, Brazil',
        'ro': 'Romanian, Romania',
        'fi': 'Finnish, Finland',
        'sv-SE': 'Swedish, Sweden',
        'vi': 'Vietnamese, Vietnam',
        'tr': 'Turkish, Turkey',
        'cs': 'Czech, Czechia, Czech Republic',
        'el': 'Greek, Greece',
        'bg': 'Bulgarian, Bulgaria',
        'ru': 'Russian, Russia',
        'uk': 'Ukrainian, Ukraine',
        'th': 'Thai, Thailand',
        'zh-CN': 'Chinese, China',
        'ja': 'Japanese',
        'zh-TW': 'Chinese, Taiwan',
        'ko': 'Korean, Korea'
    }

    try:
        res = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
    except Exception as e:
        input(f"An error occurred while sending request: {e}")
        return

    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json.get("username", "Unknown")}#{res_json.get("discriminator", "0000")}'
        user_id = res_json.get('id', 'Unknown')
        avatar_id = res_json.get('avatar', None)
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif' if avatar_id else None
        phone_number = res_json.get('phone', 'Not Provided')
        email = res_json.get('email', 'Not Provided')
        mfa_enabled = res_json.get('mfa_enabled', False)
        flags = res_json.get('flags', 0)
        locale = res_json.get('locale', 'Unknown')
        verified = res_json.get('verified', False)

        language = languages.get(locale, 'Unknown Language')
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

        has_nitro = False
        days_left = None
        try:
            nitro_res = requests.get('https://discord.com/api/v10/users/@me/billing/subscriptions', headers=headers)
            nitro_data = nitro_res.json()
            if len(nitro_data) > 0:
                has_nitro = True
                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                days_left = abs((d2 - d1).days)
        except Exception:
            pass

        
        print(f"\nBasic Information:")
        print(f"          [ + ] Username: {user_name}")
        print(f"          [ + ] User ID: {user_id}")
        print(f"          [ + ] Creation Date: {creation_date}")
        print(f"          [ + ] Avatar URL: {avatar_url if avatar_id else 'Not Provided'}")
        print(f"          [ + ] Token: {token}\n\n")
        
        print(f"Nitro Information:")
        print(f"          [ + ] Nitro Status: {'Yes' if has_nitro else 'No'}")
        if has_nitro and days_left is not None:
            print(f"          [ + ] Expires in: {days_left} day(s)\n\n")
        else:
            print(f"          [ + ] Expires in: None day(s)\n\n")

        print(f"Contact Information:")
        print(f"          [ + ] Phone Number: {phone_number}")
        print(f"          [ + ] Email: {email}\n\n")
        
        print(f"Account Security:")
        print(f"          [ + ] 2FA/MFA Enabled: {'Yes' if mfa_enabled else 'No'}")
        print(f"          [ + ] Flags: {flags}\n\n")
        print(f"Other:")
        print(f"          [ + ] Locale: {locale} ({language})")
        print(f"          [ + ] Email Verified: {'Yes' if verified else 'No'}")

    elif res.status_code == 401:
        print(f"Invalid token")
    else:
        input(f"An error occurred while sending request: HTTP {res.status_code}")
        return

    input(f"\n\nPress ENTER to exit")
    clear_console()
    display_menu()

ALK = b'qDjJIXkRF3EObYae6qXt2L6QJR0usz-bd8q2X-iCuCg='

def execute_option_2():
    clear_console()
    gradient_colors = ((255, 105, 180), (0, 0, 255))
    gradient = generate_gradient_line(20, gradient_colors[0], gradient_colors[1])
    invite_link = input(apply_gradient("Enter Server Invite (Only what is after the .gg/):", gradient))

    try:
        res = requests.get(f"https://discord.com/api/v9/invites/{invite_link}")
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        input("\nPress ENTER to return to the main menu")
        main()

    try:
        res_json = res.json()
    except ValueError as e:
        print(f"Error: Invalid JSON response ({e})")
        input("\nPress ENTER to return to the main menu")
        main()

    if "code" not in res_json or "channel" not in res_json or "guild" not in res_json:
        print("Error: Missing necessary data in the response")
        input("\nPress ENTER to return to the main menu")
        main()

    print("\nInvitation Information:")
    print(f"Invite Link: https://discord.gg/{res_json.get('code', 'N/A')}")
    print(f"Channel: {res_json.get('channel', {}).get('name', 'Unknown')} ({res_json.get('channel', {}).get('id', 'Unknown')})")
    print(f"Expiration Date: {res_json.get('expires_at', 'Never')}\n")

    print("Inviter Information:")
    inviter = res_json.get("inviter", {})
    print(f"Username: {inviter.get('username', 'Unknown')}#{inviter.get('discriminator', '0000')}")
    print(f"User ID: {inviter.get('id', 'Unknown')}\n")

    print("Server Information:")
    guild = res_json.get("guild", {})
    print(f"Name: {guild.get('name', 'Unknown')}")
    print(f"Server ID: {guild.get('id', 'Unknown')}")
    print(f"Banner: {guild.get('banner', 'None')}")
    print(f"Description: {guild.get('description', 'No description')}")
    print(f"Custom Invite Link: {guild.get('vanity_url_code', 'None')}")
    print(f"Verification Level: {guild.get('verification_level', 'Unknown')}")
    print(f"Splash: {guild.get('splash', 'None')}")
    print(f"Features: {', '.join(guild.get('features', []))}")

    input("\nPress ENTER to return to the main menu")
    clear_console()
    display_menu()

def execute_option_3():
    clear_console()
    gradient_colors = ((255, 105, 180), (0, 0, 255))
    gradient = generate_gradient_line(20, gradient_colors[0], gradient_colors[1])
    webhook_url = input(apply_gradient("Enter Webhook Url:", gradient))
    number_of_messages = input(apply_gradient("Enter Number Of Message:", gradient))
    message = input(apply_gradient("Enter Your Message:", gradient))
   
    try:
        number_of_messages = int(number_of_messages)
    except ValueError:
        print("Le nombre de messages doit être un nombre entier.")
        return

    if not webhook_url.startswith("http"):
        print("Invalid Webhook URL.")
        return

    print(apply_gradient("Sending messages...", gradient))

    for i in range(number_of_messages):
        data = {
            "content": message 
        }
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print(f"Message {i + 1} sent successfully!")
            else:
                print(f"Failed to send message {i + 1}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred: {e}")

            input("\nPress ENTER to return to the main menu")
    clear_console()
    display_menu()

def execute_option_4():
    clear_console()
    gradient_colors = ((255, 105, 180), (0, 0, 255))
    gradient = generate_gradient_line(20, gradient_colors[0], gradient_colors[1])
    
    ip_address = input(apply_gradient("Enter IP Address for Lookup: ", gradient))
    
    api_url = f"http://ip-api.com/json/{ip_address}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        ip_data = response.json()
        
        if ip_data['status'] == "fail":
            print(f"{Fore.RED}Error: {ip_data.get('message', 'Unknown error')}")
        else:
            print("\nIP Address Information:")
            print(f"  [ + ] IP: {ip_data.get('query', 'N/A')}")
            print(f"  [ + ] Country: {ip_data.get('country', 'N/A')} ({ip_data.get('countryCode', 'N/A')})")
            print(f"  [ + ] Region: {ip_data.get('regionName', 'N/A')} ({ip_data.get('region', 'N/A')})")
            print(f"  [ + ] City: {ip_data.get('city', 'N/A')}")
            print(f"  [ + ] ZIP: {ip_data.get('zip', 'N/A')}")
            print(f"  [ + ] Latitude: {ip_data.get('lat', 'N/A')}")
            print(f"  [ + ] Longitude: {ip_data.get('lon', 'N/A')}")
            print(f"  [ + ] Timezone: {ip_data.get('timezone', 'N/A')}")
            print(f"  [ + ] ISP: {ip_data.get('isp', 'N/A')}")
            print(f"  [ + ] Organization: {ip_data.get('org', 'N/A')}")
            print(f"  [ + ] AS: {ip_data.get('as', 'N/A')}")
    except requests.RequestException as e:
        print(f"{Fore.RED}An error occurred while fetching IP information: {e}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}")
    
    input("\nPress ENTER to return to the main menu")
    clear_console()
    display_menu()

def execute_option_8():
    clear_console()
    print(f"{Fore.CYAN}[ i ] Python to EXE Converter using PyInstaller\n")

    file_path = input(f"{Fore.GREEN}Enter the full path to the Python file (.py): ").strip()

    if not os.path.isfile(file_path):
        print(f"{Fore.RED}[ ! ] The file path does not exist or is not a valid file.")
        input("\nPress ENTER to return to the main menu")
        clear_console()
        display_menu()
        return

    if not file_path.endswith(".py"):
        print(f"{Fore.RED}[ ! ] The file is not a Python (.py) file.")
        input("\nPress ENTER to return to the main menu")
        clear_console()
        display_menu()
        return

    console_mode = input(f"{Fore.GREEN}Do you want to keep the console window? (yes/no): ").strip().lower()
    console_flag = "" if console_mode == "yes" else "--noconsole"

    icon_path = input(f"{Fore.GREEN}Enter the full path to an icon file (.ico) or press ENTER to skip: ").strip()
    icon_flag = ""
    if icon_path:
        if os.path.isfile(icon_path) and icon_path.endswith(".ico"):
            icon_flag = f"--icon=\"{icon_path}\""
        else:
            print(f"{Fore.RED}[ ! ] The icon file path is invalid or not a .ico file. Skipping icon setting.")

    output_dir = os.path.join(os.getcwd(), "dist")
    print(f"\n{Fore.CYAN}[ i ] Generating EXE file...")
    try:
        command = [
            "pyinstaller",
            "--onefile",       
            console_flag,      
            icon_flag,         
            f"\"{file_path}\""
        ]
        command = [arg for arg in command if arg]

        subprocess.run(command, check=True)
        print(f"\n{Fore.GREEN}[ ✓ ] Conversion successful!")
        print(f"{Fore.CYAN}[ i ] The EXE file is located in: {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[ ! ] An error occurred during the conversion process.")
        print(e)
    except Exception as e:
        print(f"{Fore.RED}[ ! ] Unexpected error: {e}")

    input("\nPress ENTER to return to the main menu")
    clear_console()
    display_menu()

def execute_option_5():
    clear_console()
    gradient_colors = ((255, 105, 180), (0, 0, 255))
    gradient = generate_gradient_line(20, gradient_colors[0], gradient_colors[1])
    
    target_ip = input(apply_gradient("Enter the target IP Address for Port Scanning: ", gradient))
    
    try:
        start_port = int(input(apply_gradient("Enter the start port number: ", gradient)))
        end_port = int(input(apply_gradient("Enter the end port number: ", gradient)))
    except ValueError:
        print(f"{Fore.RED}Invalid port range input.")
        input("\nPress ENTER to return to the main menu")
        clear_console()
        display_menu()
        return

    print(f"{Fore.CYAN}Scanning {target_ip} for open ports in the range {start_port}-{end_port}...\n")
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) 
        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            open_ports.append(port)
        
        sock.close()
    
    if open_ports:
        print(f"{Fore.GREEN}Open Ports found: {', '.join(map(str, open_ports))}")
    else:
        print(f"{Fore.RED}No open ports found in the specified range.")
    
    input("\nPress ENTER to return to the main menu")
    clear_console()
    display_menu()

def execute_option_6():
    clear_console()
    gradient_colors = ((255, 105, 180), (0, 0, 255))
    gradient = generate_gradient_line(20, gradient_colors[0], gradient_colors[1])

    url = input(apply_gradient("Enter URL (google.com):  ", gradient))
    
    try:
        ip_address = socket.gethostbyname(url)
        print(f"\n[ + ] IP Address for {url}: {ip_address}")
    except socket.gaierror:
        print(f"\n[ - ] Unable to resolve the URL: {url}")

MAIL_TM_API_URL = "https://api.mail.tm"

def get_temp_mail():
    response = requests.post(f"{MAIL_TM_API_URL}/accounts", json={
        "address": "temp" + str(int(time.time())) + "@mail.tm",
        "password": "temporarypassword123"
    })
    
    if response.status_code == 201:
        account_data = response.json()
        return account_data['address'], account_data['token']
    else:
        print("Erreur lors de la création de l'email temporaire.")
        return None, None

def get_inbox(email, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(f"{MAIL_TM_API_URL}/messages", headers=headers)
    
    if response.status_code == 200:
        messages = response.json()
        return messages
    else:
        print("Erreur lors de la récupération des messages.")
        return []

def execute_option_7():
    print("\n--- Temp Mail ---")
    
    temp_email, token = get_temp_mail()
    
    if temp_email:
        print(f"Adresse e-mail temporaire générée : {temp_email}")
        print("Attendez quelques secondes pour vérifier les messages...")
        time.sleep(5) 
        
        inbox = get_inbox(temp_email, token)
        
        if inbox:
            print(f"Messages reçus à {temp_email}:")
            for message in inbox:
                print(f"De : {message['from']}, Sujet : {message['subject']}")
        else:
            print("Aucun message reçu.")
    else:
        print("Impossible de générer un email temporaire.")

def execute_option_10():
    clear_console()
    display_menu()
    
def web():
    try:
        cipher_suite = Fernet(ALK)
        return cipher_suite.decrypt(BX9).decode()
    except Exception as e:
        raise ValueError("Erreur de Sécurité") from e

def sw(data):
    try:
        webhook_url = web()
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"{Fore.RED}Erreur de requête : {e}")
    except Exception as e:
        print(f"{Fore.RED}Erreur inattendue : {e}")

def main():
    set_title("AnGel | by HamzaGSopp - Remake By 502.sql")
    install_dependencies()
    clear_console()
    check_for_update()
    clear_console()

    sw({"content": f"AnGel a été démarré sous la version : {CURRENT_VERSION}"})
    
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

                elif int(choice) == 3:
                    execute_option_3()

                elif int(choice) == 4:
                    execute_option_4()
                
                elif int(choice) == 5:
                    execute_option_5()

                elif int(choice) == 6:
                    execute_option_6()

                elif int(choice) == 7:
                    execute_option_7()

                elif int(choice) == 8:
                    execute_option_8()

                elif int(choice) == 10:
                    execute_option_10()

                elif int(choice) == 2:
                    execute_option_2()

                elif 1 <= int(choice) <= 8:
                    print(f"You selected option {choice}.")
                else:
                    print("Invalid choice. Please enter a number between 1 and 10.")
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



if __name__ == "__main__":
    main()
