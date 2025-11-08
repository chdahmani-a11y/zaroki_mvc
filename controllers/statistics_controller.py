# controllers/statistics_controller.py
import pandas as pd
import matplotlib.pyplot as plt
import io

class StatisticsController:
    def __init__(self, members_file, skills_file=None, view=None):
        self.members_file = members_file
        self.skills_file = skills_file
        self.view = view

    def get_summary(self):
        try:
            members_df = pd.read_csv(self.members_file, delimiter=';')
            total_members = len(members_df)
            subscription_stats = members_df['subscription_status'].fillna('unknown').str.lower().value_counts()
            top_skills = {}
            if self.skills_file:
                skills_df = pd.read_csv(self.skills_file, delimiter=';')
                top_skills = skills_df['skill_name'].value_counts().head(10)
        
            return type("S", (), {
                "total_members": total_members,
                "subscription_stats": subscription_stats,
                "top_skills": top_skills
            })()
        except Exception as e:
            if self.view:
                self.view.show_message(f"[ERROR] {e}")
            return type("S", (), {"total_members": 0, "subscription_stats": pd.Series(dtype=int), "top_skills": pd.Series(dtype=int)})()

    def plot_subscriptions_bytes(self):
        try:
            members_df = pd.read_csv(self.members_file, delimiter=';')
            members_df['join_date'] = pd.to_datetime(members_df['join_date'], errors='coerce')
            paid_df = members_df[members_df['subscription_status'].str.lower() == 'paid']
            timeline = paid_df.groupby(paid_df['join_date'].dt.to_period('M')).size()
            plt.figure(figsize=(8,4))
            if timeline.empty:
                plt.text(0.5, 0.5, "No paid subscriptions", ha='center')
            else:
                timeline.index = timeline.index.to_timestamp()
                plt.plot(timeline.index, timeline.values, marker='o', linestyle='-')
                plt.title("Paid subscriptions by month")
                plt.xlabel("Month")
                plt.ylabel("Count")
                plt.xticks(rotation=45)
                plt.tight_layout()
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            return buf.getvalue()
        except Exception:
            
            import PIL.Image, PIL.ImageDraw
            buf = io.BytesIO()
            img = PIL.Image.new('RGB', (600,300), color=(255,255,255))
            d = PIL.ImageDraw.Draw(img)
            d.text((10,140), "Error generating plot", fill=(0,0,0))
            img.save(buf, format='PNG')
            buf.seek(0)
            return buf.getvalue()
