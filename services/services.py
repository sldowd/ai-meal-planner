import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime
from db.core import retrieve_user_profile, save_meal_plan

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPEN_AI_KEY")
print(f"API Key loaded: {'Yes' if api_key else 'No'}")

client = OpenAI(api_key=api_key)

def parse_meal_plan_response(response_text):
    """
    Convert the raw API response into structured data for storage
    """
    # TODO: Extract days, meals, descriptions from response
    pass        

def build_meal_plan_prompt():
    """
    Convert user profile data into a well-structured prompt for GPT
    """
    try:
        user_profile = retrieve_user_profile()
        if not user_profile:
             print("User profile not found")
             return

        instructions = []

        for key, value in user_profile.items():
            instructions.append(f"{key}: {value}\n")

        instructions_text = "\n".join(instructions)

        try:
            # Using the Responses API
            response = client.responses.create(
                model="gpt-4o",  # Using an available model
                instructions="You are a meal planning assistant that creates personalized meal plans based on user preferences and dietary needs.",
                input=f"Based on this user profile:\n\n{instructions_text}\n\nGenerate a seven day meal plan. Include breakfast, lunch, dinner, and a snack for each day."
            )
            
            # Output while testing
            print(response.output)

        # Access the meal plan content directly
            meal_plan_content = response.output[0].content[0].text
                
        # Format for database storage
            formatted_meal_plan = {
                "user_id": user_profile["id"],
                "week_start": datetime.now().strftime("%Y-%m-%d"),
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "plan_json": meal_plan_content  # Store the raw text
            }

            # Save formatted meal plan to database
            save_result = save_meal_plan(formatted_meal_plan)
            if save_result:
                print("Meal plan saved successfully")

            return formatted_meal_plan
        
        except Exception as e:
            print(f"API Error: {e}")

    except Exception as e:
         print(f"Database Error: {e}")

            
    pass


