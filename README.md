# jifter
🎁 Gift suggestion Alexa skill for Amazon Intern Global Hackathon 2018. Took 3rd place!

Note: This repo is missing its final commit and some other details (like the questions), so it's not in a working state at the moment :'(

## Features
Jifter is a Gift Suggestion Alexa skill. After asking you 8 yes/no/maybe questions and a price range, the app narrows down some potential gift ideas.

### Questions
Each question has tag weights, narrowing down the gifts jifter may suggest. These are all stored in MongoDB.

### Sources
- UncommonGoods: gifts and crafts store
- IMDB: Movie recommendations
- GoodReads: Book recommendations

## Structure
- [api] Backend API (Python Flask)
- [alexa] Alexa API (also Python Flask)
- [crawler] web scraper 
- [web] unused web front-end
