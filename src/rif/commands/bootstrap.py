from pathlib import Path
import typer
from rich import print

app = typer.Typer(help="Bootstrap new projects")

@app.command()
def fastapi(name: str):
    root = Path(name)
    (root / "app").mkdir(parents=True, exist_ok=True)
    (root / "tests").mkdir(exist_ok=True)
    (root / "README.md").write_text(f"# {name}\n")
    (root / "app" / "__init__.py").touch()
    (root / "app" / "main.py").write_text(
        'from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get("/")\ndef root():\n    return {"status":"ok"}\n'
    )
    print(f"[green]✓ Created FastAPI project '{name}'[/green]")
