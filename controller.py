from flask import Flask, render_template, request
import xarm
import time

arm = xarm.Controller('USB')


app = Flask(__name__)


@app.route('/')
def index():
    # Render the home page with sliders and buttons
    return render_template('index.html')

@app.route('/set_position', methods=['POST'])
def set_position():
    # Get the values of the sliders from the form submission
    joint1 = float(request.form['joint1'])
    joint2 = float(request.form['joint2'])
    joint3 = float(request.form['joint3'])
    joint4 = float(request.form['joint4'])
    joint5 = float(request.form['joint5'])
    joint6 = float(request.form['joint6'])
    duration = int(request.form['duration'])

    # Set the position of the arm using the xarm library
    arm.setPosition(1, joint1, duration=duration)
    arm.setPosition(2, joint2, duration=duration)
    arm.setPosition(3, joint3, duration=duration)
    arm.setPosition(4, joint4, duration=duration)
    arm.setPosition(5, joint5, duration=duration)
    arm.setPosition(6, joint6, duration=duration)

    return 'Success'

@app.route('/get_position')
def get_position():
    # Get the current position of the arm using the xarm library
    joint1 = arm.getPosition(1)
    joint2 = arm.getPosition(2)
    joint3 = arm.getPosition(3)
    joint4 = arm.getPosition(4)
    joint5 = arm.getPosition(5)
    joint6 = arm.getPosition(6)

    # Return the current position as a JSON object
    return {
        'joint1': joint1,
        'joint2': joint2,
        'joint3': joint3,
        'joint4': joint4,
        'joint5': joint5,
        'joint6': joint6
    }

if __name__ == '__main__':
    app.run(debug=True)