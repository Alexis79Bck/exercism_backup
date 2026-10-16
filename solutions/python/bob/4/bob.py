"""Bob is a lackadaisical teenager. In conversation, his responses are very limited.
Bob answers 'Sure.' if you ask him a question.
He answers 'Whoa, chill out!' if you yell at him.
He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else."""

RESPONSE_SILENCE = "Fine. Be that way!"
RESPONSE_YELLING = "Whoa, chill out!"
RESPONSE_YELLING_QUESTION = "Calm down, I know what I'm doing!"
RESPONSE_QUESTION = "Sure."
RESPONSE_DEFAULT = "Whatever."

def response(hey_bob: str) -> str:
    """Bob's response to a given statement."""
    message = hey_bob.strip()

    if not message:
        return RESPONSE_SILENCE
    
    if message.isupper():
      if message.endswith("?"):
        return RESPONSE_YELLING_QUESTION
      return RESPONSE_YELLING
    
    if message.endswith("?"):
        return RESPONSE_QUESTION
    
    return RESPONSE_DEFAULT
