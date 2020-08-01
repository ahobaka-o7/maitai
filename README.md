# maitai
Japanese Kanji Bot

## Install

```bash
pip install -r requirements.txt
```

## Usage

Make sure Twitter secret environment variables are set.

```python
from bots import TwitterBot
from config import AppConfig

app_config = AppConfig()
bot = TwitterBot(app_config.twitter)
bot.run()
```
