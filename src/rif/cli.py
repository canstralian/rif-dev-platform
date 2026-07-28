import typer
from rich.console import Console
from rif.doctor import build_report

app = typer.Typer(help="RIF Developer Platform")
from rif.commands.config import app as config_app
app.add_typer(config_app, name="config")
console = Console()

@app.command()
def version():
    console.print("[bold green]RIF Developer Platform v0.1.0[/bold green]")

@app.command()
def doctor():
    console.print(build_report())

if __name__ == "__main__":
    app()
