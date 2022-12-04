#!/usr/bin/env python3

import os
import sys

import openai


def main():
    firstArg = sys.argv[1]
    if firstArg == "models":
        models()
    else:
        print(complete(' '.join(sys.argv)))


def complete(prompt):
    openai.api_key = token()
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=1000)

    return response.choices[0].text


def models():
    openai.api_key = token()
    response = openai.Model.list(token())

    print(response)


def token():
    return os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    main()
