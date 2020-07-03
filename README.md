### Convert markdown file with keywords #### Question and #### Answer to anki card deck


#### Installation
```bash
git clone https://github.com/lerdem/md_to_anki.git && cd md_to_anki
pip install -r requirements.txt
```

#### Usage
For example you have markdown file with keywords (#### Question and #### Answer)
see [example-file-here](examples/simple.md)

convert the file with next command
```bash
python markdown_to_anki.py examples/simple.md "my test deck name" 1607342555 2059400555
# for details
# python markdown_to_anki.py --help
# locate your anki file
ls anki_output/anki_output_deck.apkg
```

After creation import anki_output_deck.apkg into you anki [app](https://f-droid.org/en/packages/com.ichi2.anki/)
