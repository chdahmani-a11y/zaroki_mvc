# views/web_view.py
from flask import Flask, render_template, request, send_file, Response
from controllers.member_controller import MemberController
from controllers.statistics_controller import StatisticsController
from views.console_view import ConsoleView
import io

app = Flask(__name__)



member_controller = MemberController("data/association_data.csv", ConsoleView())
stats_controller = StatisticsController("data/association_data.csv", "data/skills.csv")

@app.route("/")
def index():
    members = member_controller.storage.load_members()
    return render_template("members_list.html", members=members)

@app.route("/search", methods=["GET", "POST"])
def search():
    results = None
    if request.method == "POST":
        skill = request.form.get("skill", "").strip()
        results = member_controller.search_by_skill(skill)
    return render_template("search.html", results=results)

@app.route("/stats")
def stats():
    summary = stats_controller.get_summary()
    
    return render_template(
        "statistics.html",
        total_members=summary.total_members,
        subscription_stats=summary.subscription_stats.to_dict() if hasattr(summary.subscription_stats, "to_dict") else summary.subscription_stats.to_dict(),
        top_skills=summary.top_skills.to_dict()
    )

@app.route("/stats_plot.png")
def stats_plot_png():
    img_bytes = stats_controller.plot_subscriptions_bytes()
    return Response(img_bytes, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
