# views/web_view.py

from flask import Flask, Response, render_template, request, redirect, url_for, flash
from controllers.member_controller import MemberController
from controllers.statistics_controller import StatisticsController
from controllers.event_controller import EventController
from controllers.interest_controller import InterestController
from storage.events_storage import EventStorage
from storage.interests_storage import InterestStorage
from views.console_view import ConsoleView


app = Flask(__name__)
app.secret_key = "dev"

# --- Controllers & Storage ---
member_controller = MemberController("data/association_data.csv", ConsoleView())

events_storage = EventStorage("data/events.csv")
interests_storage = InterestStorage("data/interests.csv")

events = events_storage.load_events()
interests = interests_storage.load_interests()


# ------------------- MEMBERS -------------------
@app.route("/")
def index():
    members = member_controller.storage.load_members()
    return render_template("members_list.html", members=members)


@app.route("/search", methods=["GET", "POST"])
def search():
    results = None
    if request.method == "POST":
        skill = request.form.get("skill", "")
        results = member_controller.search_by_skill(skill)
    return render_template("search.html", results=results)



@app.route("/edit/<student_id>", methods=["GET", "POST"])
def edit_member(student_id):
    member = member_controller.get_member_by_id(student_id)
    if not member:
        flash("Membre introuvable.")
        return redirect(url_for("index"))

    if request.method == "POST":
        data = {
            "family_name": request.form.get("family_name", ""),
            "first_name": request.form.get("first_name", ""),
            "email": request.form.get("email", ""),
            "phone": request.form.get("phone", ""),
            "address": request.form.get("address", ""),
            "join_date": request.form.get("join_date", ""),
            "subscription_status": request.form.get("subscription_status", ""),
            "skills": request.form.get("skills", ""),
        }

        member_controller.update_member(student_id, data)
        flash("✔ Membre mis à jour avec succès")
        return redirect(url_for("index"))

    return render_template("edit_member.html", member=member)


@app.route("/delete/<student_id>")
def delete_member(student_id):
    ok = member_controller.delete_member(student_id)
    flash("✔ Membre supprimé." if ok else "❌ ID introuvable.")
    return redirect(url_for("index"))


# ------------------- STATISTICS -------------------
@app.route("/stats")
def stats():
    sc = StatisticsController("data/association_data.csv", "data/skills.csv")
    summary = sc.get_summary()
    return render_template("stats.html", stats=summary)


@app.route("/stats/plot")
def stats_plot():
    sc = StatisticsController("data/association_data.csv", "data/skills.csv")
    img = sc.plot_subscriptions_bytes()
    return Response(img, mimetype="image/png")


# ------------------- EVENTS -------------------
@app.route("/events")
def events_page(): 
    events = events_storage.load_events()
    return render_template("events_list.html", events=events)


# ------------------- INTERESTS -------------------
@app.route("/interests")
def interests_page(): 
    interests = interests_storage.load_interests()
    return render_template("interests_list.html", interests=interests)






@app.route("/add", methods=["GET", "POST"])
def add_member():
    if request.method == "POST":
        data = {
            "student_id": request.form.get("student_id", "").strip(),
            "family_name": request.form.get("family_name", "").strip(),
            "first_name": request.form.get("first_name", "").strip(),
            "email": request.form.get("email", "").strip(),
            "phone": request.form.get("phone", "").strip(),
            "address": request.form.get("address", "").strip(),
            "join_date": request.form.get("join_date", "").strip(),
            "subscription_status": request.form.get("subscription_status", "").strip(),
            "skills": "",
            "interests": ""
        }

        controller.add_member_web(data) # type: ignore
        flash("✔ Nouveau membre ajouté avec succès.")
        return redirect(url_for("index"))

    return render_template("add_member.html")








# -------------------
if __name__ == "__main__":
    app.run(debug=True)
