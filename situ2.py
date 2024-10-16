import requests
import os
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
import logging

console = Console()

logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[RichHandler(rich_tracebacks=True)])
logger = logging.getLogger()

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_image(url, filename, headers=None):
    try:
        response = requests.get(url, headers=headers, stream=True, timeout=10, allow_redirects=False)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            logger.info(f"[green]Downloaded {filename}[/green]")
        elif 300 <= response.status_code < 400:
            redirect_url = response.headers.get('Location', '')
            if redirect_url:
                logger.info(f"[blue]Redirect detected, attempting to follow to {redirect_url}[/blue]")
                response = requests.get(redirect_url, headers=headers, stream=True, timeout=10)
                if response.status_code == 200:
                    with open(filename, 'wb') as f:
                        for chunk in response.iter_content(1024):
                            f.write(chunk)
                    logger.info(f"[green]Downloaded {filename} after redirect[/green]")
                else:
                    logger.warning(f"[yellow]Failed to download {filename} after redirect (status code: {response.status_code})[/yellow]")
            else:
                logger.warning(f"[yellow]Skipped (redirect) {url}[/yellow]")
        else:
            logger.error(f"[red]Failed to download {filename} (status code: {response.status_code})[/red]")
    except requests.exceptions.HTTPError as e:
        logger.error(f"[red]HTTP error: {e} for {url}[/red]")
    except requests.exceptions.ConnectionError as e:
        logger.error(f"[red]Connection error: {e} for {url}[/red]")
    except requests.exceptions.Timeout as e:
        logger.error(f"[red]Timeout error: {e} for {url}[/red]")
    except Exception as e:
        logger.error(f"[red]Unexpected error: {e} for {url}[/red]")

def crawl_images(base_url, start_id, end_id, headers=None, output_dir='downloads'):
    console.print("[bold blue]Starting image crawl...[/bold blue]")
    ensure_directory_exists(output_dir)

    for i in range(start_id, end_id + 1):
        img_url = f"{base_url}{i}.jpg"
        filename = os.path.join(output_dir, f"{i}.jpg")
        if not os.path.exists(filename):
            download_image(img_url, filename, headers)
        else:
            logger.info(f"[cyan]Skipping existing file {filename}[/cyan]")

def main():
    ascii_art = r"""
 

 ____ ___ _____ _   _   ____                             
/ ___|_ _|_   _| | | | |___ \                            
\___ \| |  | | | | | |   __) |                           
 ___) | |  | | | |_| |  / __/                            
|____/___| |_|  \___/  |_____|      _      _           _ 
| | | |_ __  _ __ ___  ___| |_ _ __(_) ___| |_ ___  __| |
| | | | '_ \| '__/ _ \/ __| __| '__| |/ __| __/ _ \/ _` |
| |_| | | | | | |  __/\__ \ |_| |  | | (__| ||  __/ (_| |
 \___/|_| |_|_|  \___||___/\__|_|  |_|\___|\__\___|\__,_|


    """
    console.print(Panel(ascii_art, title="Universitas Pasundan", subtitle="Mahasiswa Crawler By @buble", style="bold green"))
    console.print("[bold green]Crawler Mahasiswa UNPAS by @buble [/bold green]")
    console.print("[italic]This program Crawler Mahasiswa UNPAS from a specified range of IDs (Nomer induk mahasiswa - NIM/NRP).[/italic]")
    console.print("[italic]Type 'exit' at any prompt to quit the program.[/italic]")

    base_url = "https://situ2.unpas.ac.id/uploads/unpas/fotomhs/thumb/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.120 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'en-US;q=0.9,en;q=0.8',
        'Sx-User': '254505'
    }

    while True:
        start_id_input = console.input("[bold magenta]Enter the start ID (Masukan angka mulai, contoh mulai dari nrp 203040043) : [/bold magenta]")
        if start_id_input.lower() == 'exit':
            console.print("[red]Exiting the program.[/red]")
            return
        end_id_input = console.input("[bold magenta]Enter the end ID (Masukan angka akhir, contoh akhir sampai nrp 203040089) : [/bold magenta]")
        if end_id_input.lower() == 'exit':
            console.print("[red]Exiting the program.[/red]")
            return

        try:
            start_id = int(start_id_input)
            end_id = int(end_id_input)
        except ValueError:
            console.print("[red]Please enter valid integer IDs.[/red]")
            continue

        if start_id > end_id:
            console.print("[red]The start ID must be less than or equal to the end ID.[/red]")
            continue

        crawl_images(base_url, start_id, end_id, headers)
        break

if __name__ == "__main__":
    main()
