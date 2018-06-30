# w2v_server_googlenews - Sean

Python web server that runs a pretrained word2vec model based on Google news (3 million words).

# setup

- download the google news zip

https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

- extract it (think this speeds up the python server startup)

can use 7-zip for Windows

- edit w2v_hetzner.conf to point to the unzipped bin file

- install Python 2.7
- install Python pip
  install-pip.bat (or use a Windows installer)

- install cherry web server, gensim (wraps word2vec and other ML algorithms in python)
  install.bat

# run

run.bat

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
