import typer
from db.core import save_user_profile, retrieve_user_profile
from services.services import build_meal_plan_prompt, parse_meal_plan_response

app = typer.Typer(no_args_is_help=True)

@app.callback()
def main():
    """CLI for Meal Planning."""
    pass

@app.command()
def create_profile():
    """Create or update your user profile."""
    name = typer.prompt("🧑 Name")
    skill_level = typer.prompt("🍳 Cooking skill level (Beginner, Intermediate, Advanced)")
    diet = typer.prompt("🥗 Dietary tags (comma-separated, e.g. vegan, gluten-free)")
    allergies = typer.prompt("🚫 Allergies (comma-separated, e.g. peanuts, shellfish, dairy)")
    time = typer.prompt("⏱️ Max time per meal (in minutes)")
    servings = typer.prompt("👨‍👩‍👧‍👦 Number of servings")
    budget = typer.prompt("💰 Weekly budget (in dollars)")

    typer.echo("\n✅ Profile Created:")
    typer.echo(f"Name: {name}")
    typer.echo(f"Skill Level: {skill_level}")
    typer.echo(f"Diet Tags: {diet}")
    typer.echo(f"Allergies: {allergies}")
    typer.echo(f"Time per Meal: {time} minutes")
    typer.echo(f"Servings: {servings}")
    typer.echo(f"Budget: ${budget}")

    profile = {
        "name": name,
        "skill_level": skill_level,
        "diet_tags": diet,
        "allergies": allergies,
        "time_per_meal": int(time),
        "servings": int(servings),
        "budget": float(budget)
    }

    save_user_profile(profile)
    typer.echo("💾 Profile saved to database.")

@app.command()
def view_profile():
    # Retrieve user profile from database
    user_profile = retrieve_user_profile()
    # Loop through user_profile dictionary and print
    for key, value in user_profile.items():
        print(f"{key}: {value}")


@app.command()
def generate_meal_plan():
    # call prompt builder from ai services
    meal_plan = build_meal_plan_prompt()
    
    parse_meal_plan_response(meal_plan)
