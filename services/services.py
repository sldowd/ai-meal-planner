# Structure for services/ai.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPEN_AI_KEY")
print(f"API Key loaded: {'Yes' if api_key else 'No'}")

client = OpenAI(api_key=api_key)

try:
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": "Say this is a test",
        }],
        model="gpt-4.1",
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")

response = client.responses.create(
    model="gpt-4.1",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

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