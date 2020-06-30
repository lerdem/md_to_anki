from typing import List

import re
from markdown2 import markdown as md2
from functools import partial
import genanki


class ProcessMD:
    def __init__(self, markdonwn_file_name: str):
        with open(markdonwn_file_name) as f:
            self._raw = f.read()

    def __call__(self, *args, **kwargs):
        return self.__parse()

    def __parse(self):
        # https://github.com/trentm/python-markdown2/wiki/Extras
        transformer = partial(md2, extras=["tables", "pyshell", "fenced-code-blocks"])
        regex = re.compile(r"(#### [Question|Answer]+)")
        data: List[str] = regex.split(self._raw)[1:]
        qa = [item for i, item in enumerate(data) if i % 2 != 0]
        a = [transformer(item) for i, item in enumerate(qa) if i % 2 != 0]
        q = [transformer(item) for i, item in enumerate(qa) if i % 2 == 0]
        return zip(q, a)


my_model = genanki.Model(
    1607392555,
    "Simple Model",
    fields=[{"name": "Question"}, {"name": "Answer"}],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "{{Question}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Answer}}',
        }
    ],
)

my_deck = genanki.Deck(2059400555, "Политические термины")

data = ProcessMD("data.md")()

for guid, item in enumerate(data):

    my_note = genanki.Note(model=my_model, fields=[item[0], item[1]], guid=guid)

    my_deck.add_note(my_note)

genanki.Package(my_deck).write_to_file("politic_terminology.apkg")
