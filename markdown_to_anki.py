import os
from typing import List

import re
from markdown2 import markdown as md2
from functools import partial
import genanki
from pydantic import BaseModel, Field
from fire import Fire


class UserInput(BaseModel):
    source_file: str = Field(..., regex=r'([A-z_.-]+)')
    output_file: str = Field(..., regex=r'([A-z_-]+)')
    anki_model_id: int = Field(...)
    anki_deck_id: int = Field(...)
    anki_deck_name: str = Field(..., regex=r'([A-Za-zА-Яа-я _-]+)')


class ProcessMD:
    def __init__(self, markdonwn_file_name: str):
        with open(markdonwn_file_name) as f:
            self._raw = f.read()

    def __call__(self, *args, **kwargs):
        return self.__parse()

    def __parse(self):
        # https://github.com/trentm/python-markdown2/wiki/Extras
        transformer = partial(md2, extras=['tables', 'pyshell', 'fenced-code-blocks'])
        regex = re.compile(r'(#### [Question|Answer]+)')
        data: List[str] = regex.split(self._raw)[1:]
        qa = [item for i, item in enumerate(data) if i % 2 != 0]
        a = [transformer(item) for i, item in enumerate(qa) if i % 2 != 0]
        q = [transformer(item) for i, item in enumerate(qa) if i % 2 == 0]
        return zip(q, a)


def get_model(model_id, deck_id, deck_name):
    print(locals())
    my_model = genanki.Model(
        model_id,
        deck_name,
        fields=[{'name': 'Question'}, {'name': 'Answer'}],
        templates=[
            {
                'name': deck_name,
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            }
        ],
    )
    my_deck = genanki.Deck(deck_id, deck_name)
    return my_model, my_deck


# deck_id = 2059400555
# model_id = 1607392555
# deck_name = 'Политические термины'


def main(source, deck_name, model_id, deck_id, output='anki_output_deck'):
    try:
        user_input = UserInput(
            source_file=source,
            output_file=output,
            anki_model_id=model_id,
            anki_deck_id=deck_id,
            anki_deck_name=deck_name,
        )
    except ValueError as e:
        print(e)
        exit(0)
    my_model, my_deck = get_model(
        user_input.anki_model_id, user_input.anki_deck_id, user_input.anki_deck_name
    )
    data = ProcessMD(user_input.source_file)()

    for guid, item in enumerate(data):

        my_note = genanki.Note(model=my_model, fields=[item[0], item[1]], guid=guid)

        my_deck.add_note(my_note)

    output_dir_name = 'anki_output'
    if not os.path.exists(output_dir_name):
        os.makedirs(output_dir_name)
    full_output_path = os.path.join(output_dir_name, f'{user_input.output_file}.apkg')
    genanki.Package(my_deck).write_to_file(full_output_path)


if __name__ == '__main__':
    Fire(main)
