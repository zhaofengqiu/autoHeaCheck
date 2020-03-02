from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import InfoForm
from models import Info
from exts import db,app
bs = Bootstrap(app)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/add", methods=['GET','POST'])
def add():
    form = InfoForm()
    if form.validate_on_submit():
        data = form.getDataDict()

        schoolnum = Info.query.filter_by(name=data['schoolnum']).first()
        print(schoolnum)
        if schoolnum:
            flash(message="student id is exists")
        else:
            info = Info()
            for i in data:
                if hasattr(info, i):
                    setattr(info, i, data[i])
            db.session.add(info)
            db.session.commit()
            flash("commit successed!")
    return render_template("forms.html",form=form)
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)