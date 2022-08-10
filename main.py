from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///robot-movement.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class RobotMovement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movement = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Sensor moved to {self.movement}>"


# creating the db
# db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/save_move")
def save_move():
    movement = request.values.get('move')
    message = "You Moved to "
    if movement is not None:
        print("None")
        if movement in "lrfbs":
            new_movement = RobotMovement(movement=movement)
            db.session.add(new_movement)
            db.session.commit()
            print("Added")
        if movement == "l":
            message += f" left. ({movement})"
        elif movement == "r":
            message += f" right. ({movement})"
        elif movement == "f":
            message += f" forward. ({movement})"
        elif movement == "b":
            message += f" backward. ({movement})"
        elif movement == "s":
            message = f"You Stopped ({movement})."
        else:
            message = "That is not a movement"

        return f"<h1> { message }</h1>"
    return f"<h1>Error No Value to Save</h1>"


if __name__ == '__main__':
    app.run(debug=True)
