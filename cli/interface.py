import typer

app = typer.Typer(no_args_is_help=True)

@app.callback()
def main():
    """CLI for Meal Planning."""
    pass

@app.command()
def hello():
    """Say hi and test the CLI."""
    typer.echo("👋 Hello! Your CLI is working.")