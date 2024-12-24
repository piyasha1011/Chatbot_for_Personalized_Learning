# Chatbot_for_Personalized_Learning


This project is a personalized chatbot designed to provide educational assistance by integrating with Google Classroom API. It offers features such as fetching course details and enrolling users in courses through a conversational interface.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Customization](#customization)
- [API Integration](#api-integration)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features

- Fetch detailed information about courses available in Google Classroom.
- Enroll users in specified courses through a conversational interface.
- Intelligent dialogue management using Rasa.
- Expandable to other LMS APIs or educational features.

## Technologies Used

- **Rasa Framework**: For natural language understanding (NLU) and dialogue management.
- **Python**: For backend logic and API integration.
- **REST API**: To communicate with Google Classroom.
- **Anaconda**: For managing Python environments.

## Setup Instructions

### Prerequisites

1. Python (3.7 or later)
2. Anaconda (optional but recommended)
3. Rasa (install using `pip install rasa`)
4. Google Classroom API Token 
### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-name
   ```

2. Create a virtual environment:

   ```bash
   conda create -n installingrasa python=3.8
   conda activate installingrasa
   ```

3. Install dependencies:

   ```bash
   pip install rasa rasa-sdk requests
   ```

4. Train the Rasa model:

   ```bash
   rasa train
   ```

5. Start the Rasa server:

   ```bash
   rasa run
   ```

6. Start the action server for custom actions:

   ```bash
   rasa run actions
   ```

## File Structure

```
project-root/
├── actions/
│   └── actions.py         # Custom action code
├── data/
│   ├── nlu.yml           # Training data for NLU
│   ├── stories.yml       # Training stories for dialogue
│   └── rules.yml         # Dialogue rules
├── models/
│   └── [model files]     # Trained Rasa models
├── config.yml            # Rasa pipeline and policies configuration
├── credentials.yml       # Credentials for connectors
├── endpoints.yml         # Configuration for action server
└── domain.yml            # Domain file (intents, slots, responses)
```

## Usage

1. Start a conversation with the bot by sending a message to the Rasa REST endpoint:

   ```bash
   curl -X POST http://localhost:5005/webhooks/rest/webhook         -H "Content-Type: application/json"         -d '{"sender": "user", "message": "Tell me about the Python course"}'
   ```

2. Follow the bot's responses to fetch course details or enroll in a course.

## Customization

- **Modify Intents**: Update `nlu.yml` to add new intents and training examples.
- **Add Actions**: Extend the `actions.py` file for additional custom functionality.
- **Update API**: Replace the API endpoint and token in `actions.py` with those specific to Google Classroom.

## API Integration

This project uses the Google Classroom API. Replace the placeholders in `actions.py` with your actual API details:

- API URL
- API Token (store securely using environment variables)

Example:

```python
api_url = "https://classroom.googleapis.com/v1/courses"
token = os.getenv("GOOGLE_CLASSROOM_API_TOKEN")
```

## Troubleshooting

1. **Error: Unable to Fetch Course Details**

   - Ensure the API token is correct and has the required permissions.
   - Verify the Google Classroom API setup.

2. **Rasa Model Not Responding**

   - Check the Rasa server logs for errors.
   - Retrain the model using `rasa train`.

3. **Action Server Not Working**

   - Confirm the action server is running on the correct port (`5055` by default).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
