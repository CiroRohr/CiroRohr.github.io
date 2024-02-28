#! bin/bash

echo "starting flask server..."
export FLASK_APP=blog
export FLASK_ENV=development
flask --debug run
