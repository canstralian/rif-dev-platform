import typer
from rich import print
from rif.config import init_config, load_config

app = typer.Typer()

@app.command("init")
def init():
    init_config()
    print("[green]✓ Configuration initialised[/green]")

@app.command("show")
def show():
    print(load_config())
