# Structure for services/ai.py
import os
import openai
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def build_meal_plan_prompt(user_profile):
    """
    Convert user profile data into a well-structured prompt for GPT
    """
    # TODO: Format the user profile data into a clear prompt
    # Consider extracting: diet_tags, skill_level, time_per_meal, etc.
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