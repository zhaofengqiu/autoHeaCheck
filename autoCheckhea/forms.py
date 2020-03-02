from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import Length, DataRequired, Required
from flask_wtf import FlaskForm

class InfoForm(FlaskForm):
    name =  StringField(u"姓名", render_kw={'placeholder':'吴佳帅'} ,validators=[DataRequired(message=u"姓名不能为空"), Length(1,10)])
    sex  = SelectField(u"性别",  validators=[Required(message=u"请选择")], choices=[('boy','男生'),('girl','女生')])
    schoolnum = StringField(u"学号", validators=[DataRequired(message=u"学号不能为空"), Length(1,20)])
    bumen = StringField(u"部门", render_kw={'value':'行政组织架构/计算机与人工智能学院/网络工程(卓工超豪实验班)/17网工1'} ,validators=[DataRequired(message=u"部门不能为空"), Length(1,100)])
    phone = StringField(u"你的电话号码", validators=[DataRequired(message=u"电话号码不能为空"), Length(1,20)])
    email = StringField(u"邮箱地址", render_kw={'placeholder':'每天提交后，会将提交结果反馈到这个邮箱'},validators=[ Length(1,20)])
    submit = SubmitField("确认无误,提交")
    def getDataDict(self):
        return {
            "name":self.name.data,
            "sex":self.sex.data,
            "schoolnum":self.schoolnum.data,
            "bumen":self.bumen.data,
            "phone": self.phone.data,
            "email": self.email.data
        }