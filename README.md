# myfilter
How to use it:
- Install the requirements using the requirements.txt file (a virtual environment is highly recommended): ``pip install -r requirements.txt``
- Set up the on ``OPENAI_API_KEY``(see the example on ``.env_example``) ``.env`` file with your secret key from OpenAI.
- run the project using ``flask run —port 8000``
- request send a ``GET`` request with a Json body, request body example:
    ``{"message": "your message here"}``
