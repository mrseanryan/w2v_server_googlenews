# w2v_server_googlenews - Sean

Python web server that runs a pretrained word2vec model based on Google news (3 million words).

this is a fork from [RaRe-Technologies/w2v_server_googlenews](https://github.com/RaRe-Technologies/w2v_server_googlenews)

this fork adds a couple of REST methods:

- similarity: how similar are 2 words
- similarityMultiple: how similar are pairs from 2 sets of words

- from observation, a minimum similarity of 0.4 seems to be a good threshold for 'is similar'

also adds notes and scripts for use on Windows.

see below for example URLs.

# setup

- download the google news zip

https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

- extract it (think this speeds up the python server startup)

can use 7-zip for Windows

- edit w2v_hetzner.conf to point to the unzipped bin file

- install Python 2.7

- install Python pip

```
install-pip.bat
```

(or use a Windows installer)

- C++ compiler for python (Windows)
  http://aka.ms/vcpython27

- install cherry web server, gensim (wraps word2vec and other ML algorithms in python)

```
install.bat
```

# run

```
run.bat
```

# test (from browser)

http://localhost:8889/status

http://localhost:8889/most_similar?positive%5B%5D=woman&positive%5B%5D=king&negative%5B%5D=man

http://localhost:8889/most_dissimilar?words%5B%5D=dinner+cereal+breakfast+lunch

http://localhost:8889/suggest?term=kin

## added by Sean

similarity
http://localhost:8889/similarity?words%5B%5D=sweden+germany

similarityMultiple - can kind of categorize the words!
http://localhost:8889/similarityMultiple?used[]=sweden+germany+banana&available[]=france+italy+argentina+thailand+zimbabwe+apricot+tuna

- the behavior of `similarityMultiple` is intended as: "Here are some words I've used, here's a list of the available words - tell me which of those are most similar to those already used."

- the use case could be some kind of suggestion mechanism to suggest selections to a user.
