# myfilter
My filter is an api used to rewrite something that you wish to send to someone.

If you are worried that your message is unprofessional, use the endpoint ``gentleman`` to rewrite it.

Do you want your message to be writen in a beautiful haiku? no problem, use the endpoint ``sage``

# How to use it
- Install the requirements using the requirements.txt file (a virtual environment is highly recommended): ``pip install -r requirements.txt``
- Set up the on ``OPENAI_API_KEY``(see the example on ``.env_example``) ``.env`` file with your secret key from OpenAI.
- run the project using ``flask run —port 8000``
- request send a ``GET`` request with a Json body, request body example:
    ``{"message": "your message here"}``
