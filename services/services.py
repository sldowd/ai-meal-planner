import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openai import OpenAI
from dotenv import load_dotenv
from db.core import retrieve_user_profile

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPEN_AI_KEY")
print(f"API Key loaded: {'Yes' if api_key else 'No'}")

client = OpenAI(api_key=api_key)
        

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
                
                # The output is available in response.output_text
                print(response.output)
                return response.output_text
        except Exception as e:
            print(f"Error: {e}")

    except Exception as e:
         print(f"Error: {e}")

    pass

def generate_meal_plan(user_profile):
    """
    Call OpenAI API with user profile data to generate a meal plan
    """
    # TODO: Build prompt
    # TODO: Call OpenAI API
    # TODO: Parse and structure the response
    pass

def parse_meal_plan_response(response_text):
    """
    Convert the raw API response into structured data for storage
    """
    # TODO: Extract days, meals, descriptions from response
    pass

build_meal_plan_prompt()