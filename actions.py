from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai
import webbrowser
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Set your OpenAI API key
openai.api_key = "### "  # Place your OpenAI API key here #confidential 

# Google Classroom API setup
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']
SERVICE_ACCOUNT_FILE = r'E:\chatbot\brave-wave-445013-d7-6e9ebc345a79.json'  # Correct path to your service account file

# Function to get Google Classroom courses
def get_google_classroom_courses():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('classroom', 'v1', credentials=credentials)
    results = service.courses().list().execute()
    courses = results.get('courses', [])
    return courses

# OpenAI GPT function
def chatgpt_clone(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response.choices[0].text

# Custom Action to play video
class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"

    async def run(self, dispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        video_url = "https://youtu.be/-F6h43DRpcU"
        dispatcher.utter_message("Wait... Playing your video.")
        webbrowser.open(video_url)
        return []

# Custom Action to show owner profile
class ActionOwner(Action):
    def name(self) -> Text:
        return "action_owner"

    async def run(self, dispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        url = "https://www.linkedin.com/in/karan-kadam-251978195"
        dispatcher.utter_message("Wait... Owner's profile is loading.")
        webbrowser.open(url)
        return []

# Custom Action for GPT-based search
class ActionSearch(Action):
    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher, tracker, domain):
        text = tracker.latest_message.get("text")
        response = chatgpt_clone(text)
        dispatcher.utter_message(response)
        return []

# Custom Action to recommend resources based on subject
class ActionRecommendResources(Action):
    def name(self) -> Text:
        return "action_recommend_resources"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        subject = tracker.get_slot("subject")
        if subject:
            resources = {
                "mathematics": ["Math resource 1", "Math resource 2"],
                "physics": ["Physics resource 1", "Physics resource 2"],
                "Python": ["Python tutorial 1", "Python tutorial 2"],
            }
            message = resources.get(subject, f"Sorry, I have no resources for {subject}.")
        else:
            message = "Please specify a subject you'd like resources for."
        dispatcher.utter_message(text=message)
        return []

# Custom Action to fetch Google Classroom courses
class ActionGoogleClassroomContent(Action):
    def name(self) -> Text:
        return "action_google_classroom_content"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        courses = get_google_classroom_courses()
        if courses:
            course_names = "\n".join([course['name'] for course in courses])
            dispatcher.utter_message(text=f"Here are your courses:\n{course_names}")
        else:
            dispatcher.utter_message(text="No courses found in Google Classroom.")
        return []
