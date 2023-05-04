from setuptools import setup, find_packages

setup(
    name="flashcardify",
    version="0.0.1",
    description="A tool for creating flashcards from text",
    author="Gabriel Simmons",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "flashcardify = flashcardify.flashcardify:flashcardify",
            "fcfy = flashcardify.flashcardify:flashcardify",
        ]
    },
)
