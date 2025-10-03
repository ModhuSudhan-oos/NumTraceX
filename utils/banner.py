from colorama import Fore, Style, init

init(autoreset=True)

def show_banner():
    banner = f"""
{Fore.RED}███╗   ██╗██╗   ██╗███╗   ███╗████████╗██████╗  █████╗  ██████╗███████╗
{Fore.YELLOW}████╗  ██║██║   ██║████╗ ████║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝
{Fore.GREEN}██╔██╗ ██║██║   ██║██╔████╔██║   ██║   ██████╔╝███████║██║     █████╗  
{Fore.CYAN}██║╚██╗██║██║   ██║██║╚██╔╝██║   ██║   ██╔═══╝ ██╔══██║██║     ██╔══╝  
{Fore.BLUE}██║ ╚████║╚██████╔╝██║ ╚═╝ ██║   ██║   ██║     ██║  ██║╚██████╗███████╗
{Fore.MAGENTA}╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝
    {Style.BRIGHT}NumTraceX — Phone Number Intelligence Toolkit
    """
    print(banner)


