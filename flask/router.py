from flask import Flask
from flask import request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # 如果post进来密码了就是已经输入了，直接跳转
    password = request.form.get("password")
    if password is not None:
        return redirect(url_for("patient_list"))
    # 判断是哪种登录方式
    type = request.args.get("type")
    pswd = True
    if type == "face":
        pswd = False
    return render_template("login.html", pswd=pswd)


@app.route("/patient_list")
def patient_list():
    patients = [
        {"name": "赵", "age": "20", "gender": "男", "priority": "高", "filename": "zhao.nii.gz"},
        {"name": "钱", "age": "23", "gender": "男", "priority": "中", "filename": "qian.nii.gz"},
        {"name": "孙", "age": "25", "gender": "男", "priority": "低", "filename": "sun.nii.gz"},
        {"name": "李", "age": "27", "gender": "女", "priority": "低", "filename": "li.nii.gz"},
    ]
    return render_template("patient_list.html", patients=patients)


@app.route("/report", methods=["GET"])
def report():
    file = request.args.get("file")
    return render_template("report.html", file_name=file)


# @app.route("/recsys", methods=["GET", "POST"])
# def promo():
#     post = request.form.get("password")
#     print(post)
#     get = request.args.get("password")
#     return "testing"


if __name__ == "__main__":
    # app.run(host, port, debug, options)
    # app.run(host="0.0.0.0", port=5000, ssl_context=("/root/cer/zdcd.online.cer", "/root/cer/zdcd.online.key"))

    app.run(host="0.0.0.0", port=5000)
