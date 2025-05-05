import typer
from db.core import save_user_profile

app = typer.Typer(no_args_is_help=True)

@app.callback()
def main():
    """CLI for Meal Planning."""
    pass

@app.command()
def create_profile():
    """Create or update your user profile."""
    name = typer.prompt("🧑 Name")
    skill = typer.prompt("🍳 Cooking skill level (Beginner, Intermediate, Advanced)")
    diet = typer.prompt("🥗 Dietary tags (comma-separated, e.g. vegan, gluten-free)")
    allergies = typer.prompt("🚫 Allergies (comma-separated, e.g. peanuts, shellfish, dairy)")
    time = typer.prompt("⏱️ Max time per meal (in minutes)")
    servings = typer.prompt("👨‍👩‍👧‍👦 Number of servings")
    budget = typer.prompt("💰 Weekly budget (in dollars)")

    typer.echo("\n✅ Profile Created:")
    typer.echo(f"Name: {name}")
    typer.echo(f"Skill Level: {skill}")
    typer.echo(f"Diet Tags: {diet}")
    typer.echo(f"Allergies: {allergies}")
    typer.echo(f"Time per Meal: {time} minutes")
    typer.echo(f"Servings: {servings}")
    typer.echo(f"Budget: ${budget}")

    profile = {
        name: "name",
        skill: "skill",
        diet: "diet",
        allergies: "allergies",
        time: "time",
        servings: "servings",
        budget: "budget"
    }

    save_user_profile(profile)
    typer.echo("💾 Profile saved to database.")