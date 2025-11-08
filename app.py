#app.py
from views.web_view import app
from controllers.member_controller import MemberController
from controllers.statistics_controller import StatisticsController
from views.console_view import ConsoleView
from views.statistics_view import StatisticsView

def main():
    view = ConsoleView()
    stats_view = StatisticsView()

    controller = MemberController("data/association_data.csv", view)
    stats_controller = StatisticsController("data/association_data.csv", "data/skills.csv", stats_view)

    while True:
        print("\n===== MENU =====")
        print("1. Afficher les membres")
        print("2. Ajouter un membre")
        print("3. Rechercher un membre par compétence")
        print("4. Modifier un membre")
        print("5. Supprimer un membre")  
        print("6. Afficher les statistiques")
        print("7. Afficher graphique des abonnements par mois")
        print("8. Quitter")


        choix = input("Votre choix : ").strip()
       
        if choix == "1":
            controller.display_members()

        elif choix == "2":
            controller.add_member()

        elif choix == "3":
            skill_name = view.ask_skill_name()
            result = controller.search_by_skill(skill_name)
            view.display_search_results(result)

        elif choix == "4":
            controller.update_member()

        elif choix == "5":
            controller.delete_member()

        elif choix == "6":
            stats_controller.generate_statistics()    

        elif choix == "7":
            stats_controller.plot_subscriptions_over_time()

        elif choix == "8":
           print("À bientôt !")
           break

    
        else:
            print("Choix invalide, réessayez.")


if __name__ == "__main__":     
    app.run(debug=True)




#if __name__ == "__main__":
   # main()
