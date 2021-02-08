from flask import Flask, render_template, send_from_directory, request
from flask_bootstrap import Bootstrap
from forms import Drawing
from fractals import LSystem


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.update(
    SEND_FILE_MAX_AGE_DEFAULT=0
)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Drawing()
    
    if request.method == 'GET':
        return render_template('index.html', form=form)
    
    else:
        initial_state, productions, number_steps, angle = form.initial_state.data, form.productions.data, form.number_steps.data, form.angle.data
        step_size = request.form['step_size'] #form.step_size.data

        fractal_path, fractal_possibilities = get_lsystem(initial_state, productions, number_steps)

        return render_template('drawing.html', form=form, fractal_path=fractal_path, step_size=step_size, angle=angle, fractal_possibilities=fractal_possibilities)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


def get_lsystem(initial_state, productions, number_of_steps):
    productions_dict = {}
    for p in productions.split('\n'):
        s = p.split('>')
        productions_dict[s[0].strip()] = s[1].strip()
    
    fractal = LSystem(initial_state, productions_dict.keys(), productions_dict)

    fractal.run_steps(number_of_steps)

    return fractal.current_instance, list(productions_dict.keys())


if __name__ == '__main__':
    app.run()
