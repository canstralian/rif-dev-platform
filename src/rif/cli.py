import typer
from rich.console import Console

app = typer.Typer(help="RIF Developer Platform")
console = Console()

@app.command()
def version():
    console.print("[green]RIF Developer Platform v0.1.0[/green]")

@app.command()
def doctor():
    console.print("[cyan]Doctor not implemented yet.[/cyan]")

if __name__ == "__main__":
    app()
