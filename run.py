from ailib import create_app
import os

#app = create_app(os.environ.get('AI_LIB_ENV'))
app = create_app('dev')

if __name__ == '__main__':
    app.run()
