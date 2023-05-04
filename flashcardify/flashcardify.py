import langchain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import click
import yaml

from langchain.chains import LLMChain, ConversationChain
from langchain.chains.conversation.memory import ConversationEntityMemory
from langchain.chains.conversation.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain.llms import OpenAI
from flashcardify.constants import FLASHCARDIFY_DIR
from flashcardify.cards import Card
from flashcardify.prompts import BASIC

# from flashcardify.configs import Config

load_dotenv()


def notimplemented_check(database: str, style: str):
    if database != "obsidian":
        raise NotImplementedError("Only obsidian database is currently supported")

    if style != "cloze":
        raise NotImplementedError("Only cloze style is currently supported")


# def get_config():
#     config_path = FLASHCARDIFY_DIR / "config.yaml"
#     if config_path.exists():
#         config = Config.from_file(config_path)
#     else:
#         config = Config(
#             models=[],
#             databases=[],
#             styles=[],
#             syntaxes=[],
#         )
#         config.write(config_path)

#     return config


@click.command()
@click.argument("content")
@click.option(
    "--style",
    type=click.Choice(choices=["front-back", "cloze"]),
    default="cloze",
    help="The style of flashcard to create",
)
@click.option(
    "--syntax",
    type=click.Choice(choices=["markdown", "anki"]),
    default="markdown",
    help="The syntax to use for the flashcard",
)
@click.option(
    "--model", default="text-davinci-003", help="The model to use for the flashcard"
)
@click.option(
    "--database", default="obsidian", help="The database to use for the flashcard"
)
@click.option(
    "--interactive/--no-interactive",
    is_flag=True,
    help="Whether to prompt the user for missing values",
    default=True,
)
@click.option(
    "--author", default=None, help="The author of the content to be flashcardified"
)
@click.option(
    "--title", default=None, help="The title of the content to be flashcardified"
)
@click.option(
    "--num-cards",
    default=None,
    help="The number of flashcards to create from the content",
)
def flashcardify(
    content: str,
    style: str = "cloze",
    syntax: str = "markdown",
    model: str = "gpt-3.5-turbo",
    database: str = "obsidian",
    interactive: bool = True,
    author: str = None,
    title: str = None,
    num_cards: int = None,
):
    notimplemented_check(database, style)
    # config = get_config()

    # DB = getattr(__import__("flashcardify.databases", fromlist=[database]), database)
    # db = DB()
    prompt = BASIC

    prompt = PromptTemplate(
        input_variables=[
            "style",
            "title",
            "author",
            "content",
            "syntax",
            "syntax_instructions",
            "custom_instructions",
            "num_cards",
        ],
        template=prompt,
    )

    kwargs = click.get_current_context().params

    def collect_missing_kwargs():
        for key, value in kwargs.items():
            if value is None:
                # ask the user for the missing value
                kwargs[key] = click.prompt(key)

    if interactive:
        collect_missing_kwargs()

    chain = LLMChain(llm=OpenAI(model_name=model, max_tokens=140), prompt=prompt)

    kwargs[
        "syntax_instructions"
    ] = """

    Markdown syntax uses **bold** to denote cloze deletions.

    """

    kwargs[
        "custom_instructions"
    ] = """

    For definitional content, like "[term] is [definition]", if you are using cloze style, use the following syntax:

    **[term]** is **[definition]**.

    For cards about the main claims of content, if you are using cloze style, use the following syntax:

    In **[title]**, *[author]** claims that **[claim]**.

    """

    kwargs_in_prompt = {k: v for k, v in kwargs.items() if k in prompt.input_variables}

    print(prompt.format(**kwargs_in_prompt))

    results = chain.run(
        **kwargs,
    )
    print(results)

    # TODO: use a syntax to convert the results to a flashcard

    # card = Card(front=results.strip())
    # print(card.front)

    # if database is not None:
    #     db.store(card)


if __name__ == "__main__":
    flashcardify()
