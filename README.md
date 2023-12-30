# Sign Language Animator

**Sign Language Animator** is a Django-based web application that enables users to input words or sentences, preprocess the input using Natural Language Processing (NLP) techniques, and generate corresponding sign language animations. The project utilizes the NLTK library, Blender dataset, and incorporates features such as text recognition and audio recognition.

## Features

- **NLP Preprocessing:**
  The user's input undergoes preprocessing using Natural Language Processing techniques to enhance the accuracy of animations.

- **Animation Generation:**
  Each processed word or alphabet is associated with a specific animation stored in the database. The application retrieves the relevant animation and displays it to the user.

- **Text Recognition:**
  Users can input words or sentences via text, and the application recognizes and processes the text to generate animations.

- **Audio Recognition:**
  The application accepts audio input, converts it into text using audio recognition techniques, and then proceeds to generate corresponding sign language animations.

## Technologies Used

- **Django:** The web framework used to build the application.
- **NLTK (Natural Language Toolkit):** Utilized for Natural Language Processing tasks.
- **Blender Dataset:** The dataset used for deriving sign language animations.
- **Other Dependencies:** Audio Recongnition(Speech to text javascript api)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RuAmey27/SignLanguageAnimator.git
   ```
   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   python manage.py migrate
   ```
   ```bash
   python manage.py runserver
   ```
   
2. **Access the Application:**
  Open your web browser and go to http://localhost:8000/ to access the Sign Language Animator application.

# Usage
**Input:**
    Enter a word or sentence using the provided input form.
**Processing:**
    The input undergoes NLP preprocessing to extract relevant information.
**Animation Output:**
    The application fetches the corresponding animations from the database and displays them to the user.
**Audio Input (Optional):**
    Users can provide input through audio, and the application converts it to text for processing.

## Purpose and Impact

Communication barriers can be challenging, especially for individuals who are not familiar with sign language. This project addresses these challenges by providing a platform where users can input words or sentences, and the application generates corresponding sign language animations. This not only facilitates communication for those unfamiliar with sign language but also enhances the overall inclusivity of interactions with the deaf community.

## How it Helps

- **Communication without Prior Sign Language Knowledge:**
  - Individuals who do not know sign language can effectively communicate with deaf individuals using the application. The animations serve as a visual representation of the spoken or written words.

- **Enhanced Understanding:**
  - Deaf individuals can benefit from the visual representation of words or sentences, improving their understanding of the communicated message.

- **Audio Input Option:**
  - The inclusion of audio input recognition ensures that users can provide input through spoken words, further bridging the communication gap.

## Contributing to Accessibility

By contributing to this project, you are actively contributing to the accessibility and inclusivity of communication for the deaf community. Feel free to suggest improvements, contribute new features, or report issues to help make this tool even more effective and user-friendly.

