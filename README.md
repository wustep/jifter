# jifter
🎁 Gift suggestion Alexa skill for Amazon Intern Global Hackathon 2018. Took 3rd place!

Note: This repo is missing its final commit and some other details (like the questions), so it's not in a working state at the moment :'(

**Submission summary:**
```
Jifter (pronounced with a J) is an Alexa app to help you find the perfect gift. By asking you a few quick questions to narrow down your options, Jifter will look through its database of (currently) 500 products--books, movies, and various gifts--and find the top gifts for you.
```

## Features
Jifter is a Gift Suggestion Alexa skill. After asking you 8 yes/no/maybe questions and a price range, the app narrows down some potential gift ideas.

### Questions
Each question has tag weights, narrowing down the gifts jifter may suggest. These are all stored in MongoDB.

### Sources
- UncommonGoods: gifts and crafts store
- IMDB: Movie recommendations
- GoodReads: Book recommendations

### Extension
Currently, it returns the top product, but eventually, it could return a scrollable list of gifts. Additionally, we could use Twilio or emailing to email direct links to every product, or even have it purchase products on Amazon for you as well.

## Structure
- [api] Backend API (Python Flask)
- [alexa] Alexa API (also Python Flask)
- [crawler] web scraper 
- [web] unused web front-end
