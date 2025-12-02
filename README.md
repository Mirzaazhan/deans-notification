## Configuration & Environment Variables

**Refactoring Note:** For security and modern deployment best practices, all API keys and sensitive credentials are now loaded from **Environment Variables** instead of the `config.ini` file. Please ensure these variables are set in your environment before starting the server.

Variable Name 
| **GMAIL_USER** | The email address for sending reports.  `email_client.py` 
| **GMAIL_PASSWORD** | The application-specific password for the Gmail account.  `email_client.py` 
| **TWILIO_ACCOUNT_SID** | Your Twilio Account SID.  `sms_client.py`
| **TWILIO_TOKEN** | Your Twilio Auth Token.  `sms_client.py` 
| **TWITTER_CKEY** | Twitter Consumer Key (API Key).  `twitter_client.py` 
| **TWITTER_CSECRET** | Twitter Consumer Secret (API Secret).  `twitter_client.py` 
| **TWITTER_ATOKEN** | Twitter Access Token.  `twitter_client.py` 
| **TWITTER_ASECRET** | Twitter Access Token Secret.  `twitter_client.py` 
| **FACEBOOK_PAGE_ID** | The Facebook Page ID where messages are posted.  `facebook_client.py` 
| **FACEBOOK_USER_TOKEN** | The User Access Token required for posting to the page.  `facebook_client.py` 
| **PRODUCTION** | Set to `1` in a production deployment (e.g., in Docker) to explicitly disable Flask debug mode.  `message_manager.py` 
