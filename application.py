from flask import Flask, render_template, request, url_for
import get_info
import map_generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def get_nickname():
    nickname = request.form.get('nickname')
    friends_location = get_info.main(nickname)

    if (not nickname) or (friends_location == {}):
        return render_template('failure.html')

    # generate the map
    friends_map = map_generator.generate_map(friends_location)

    return friends_map


if __name__ == '__main__':
    app.run(debug=True)