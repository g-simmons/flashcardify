BASIC = """
These are examples of excellent flashcards for spaced repetition. 
Notice how they are atomic, and how they are written in a way that makes them easy to remember.
Notice how flashcards are created for both claims from the content AND background information.
Notice how they include the author and title of the content they are based on, ONLY for facts and claims 
that originate from the content, and not for background information.

### Example 1:

Metadata:

    Title: {title}
    Author: {author}

Content: 

    {content}

Instructions:

    Make {style} style flashcards using {syntax} syntax from the above content. 

    Isolate atomic information from the content.

    When author and title information is present, include the author and title in flashcards about claims from the content. 
    
    For example:

        In title, author claims that ...

    {syntax_instructions}

    {custom_instructions}

    Number of flashcards: {num_cards}

Cards:
"""
