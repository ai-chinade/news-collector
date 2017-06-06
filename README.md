# news-collector
Collecting AI related news

## Dependencies
- Ubuntu/Mac recommended.
- `jq`: https://stedolan.github.io/jq/

If JQ only stay in version 1.3 and can't be upgraded, we can use following steps to upgrade it into version 1.5. 
```bash
wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
chmod +x jq-linux64
sudo mv jq-linux64 $(which jq)
```
https://stackoverflow.com/questions/36462955/upgrading-jq-to-1-5-on-ubuntu

If ca-certificate path problem shows concerning curl, following steps can be tried.
```bash
sudo apt-get install ca-certificates
echo 'cacert=/etc/ssl/certs/ca-certificates.crt' > ~/.curlrc
``` 


## Running
```bash
pip install -r requirements.txt
python ./write_news.py
```
