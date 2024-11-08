import os
from dotenv import load_dotenv
load_dotenv()
from src.app import create_app

env_name =os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
    port = os.getenv('FLASK_PORT')
    app.run(host='0.0.0.0', port=port)