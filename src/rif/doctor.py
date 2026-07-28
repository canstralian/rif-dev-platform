import platform
import shutil
from rich.table import Table


def _check(command: str):
    return shutil.which(command)


def build_report() -> Table:
    table = Table(title="RIF Doctor")
    table.add_column("Component")
    table.add_column("Status")
    table.add_column("Details")

    def add(name: str, value: str | None):
        if value:
            table.add_row(name, "[green]✓[/green]", value)
        else:
            table.add_row(name, "[red]✗[/red]", "Not Found")

    table.add_row("Python", "[green]✓[/green]", platform.python_version())
    table.add_row("Platform", "[green]✓[/green]", platform.platform())

    add("Git", _check("git"))
    add("uv", _check("uv"))
    add("Docker", _check("docker"))
    add("GitHub CLI", _check("gh"))
    add("Ollama", _check("ollama"))
    add("NVIDIA SMI", _check("nvidia-smi"))

    return table
