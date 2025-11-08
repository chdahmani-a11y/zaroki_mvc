class StatisticsView:
    def show_statistics(self, summary):
        print("\n===== STATISTIQUES =====")
        print(f"Nombre total de membres : {summary.total_members}\n")

        print("Abonnements (paid vs pending):")
        print(summary.subscription_stats.to_string(), "\n")

        print("Top compétences:")
        print(summary.top_skills.to_string(), "\n")
