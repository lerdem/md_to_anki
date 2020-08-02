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


#### Rule for card creation
 * Keep decks simple (1 per exam) and use tags for systems, mnemonics etc
 * Understand first then memorize so you can apply what you learn on test day (makes learning quicker)
 * Lay foundations first (80/20) focus on highest yield information big picture basics before details
 * Minimum information principal (don’t make complex cards with sub items, make a bunch of simple cards for each sub item)
 * Cloze Deletions are AmAzInG! (Helps with step 4)
 * Images Photos and Figures (better than a bunch of text) even an “unrelated” image that makes you think of the topic — image occlusion enchanted
