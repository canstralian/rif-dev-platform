import typer
from rich.console import Console
from rif.doctor import build_report

app = typer.Typer(help="RIF Developer Platform")
from rif.commands.config import app as config_app
from rif.commands.bootstrap import app as bootstrap_app
app.add_typer(config_app, name="config")
app.add_typer(bootstrap_app, name="bootstrap")
console = Console()

@app.command()
def version():
    console.print("[bold green]RIF Developer Platform v0.1.0[/bold green]")

@app.command()
def doctor():
    console.print(build_report())

if __name__ == "__main__":
    app()
