from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from forms import ContactForm, MorseCodeForm
from morsecode import MorseCode
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SE4d3njGs7IlkHjS9nMwKaQ'
Bootstrap(app)

current_year = date.today().year

@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = ContactForm()
    morse = MorseCodeForm()
    if request.method == 'POST' and form.validate_on_submit():
        flash(u'Successfully sent your message')
        return redirect(url_for('home_page', form=form, m_form=morse))

    return render_template('index.html', year=current_year, form=form, m_form=morse)

if __name__ == "__main__":
    app.run(debug=True)
