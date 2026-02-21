from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.1-8b-instant"
)

def generate_restaurant_name_and_items(cuisine):

    # Step 1: Generate restaurant name
    name_prompt = ChatPromptTemplate.from_template(
        "I want to open a restaurant for {cuisine} food. "
        "Give me ONLY ONE fancy restaurant name. No explanation."
    )

    name_chain = name_prompt | llm
    name_response = name_chain.invoke({"cuisine": cuisine})
    restaurant_name = name_response.content.strip()

    # Step 2: Generate menu items
    menu_prompt = ChatPromptTemplate.from_template(
        "Suggest 5 menu items for {restaurant_name}. "
        "Return ONLY comma separated food items."
    )

    menu_chain = menu_prompt | llm
    menu_response = menu_chain.invoke({"restaurant_name": restaurant_name})
    menu_items = menu_response.content.strip()

    return {
        "restaurant_name": restaurant_name,
        "menu_items": menu_items
    }