class ConsoleView:

    def show_message(self, message):
        print("\n" + message)

    def display_member_list(self, members):
        print("\n=== Liste des membres ===")
        for m in members[:20]:
            print(f"- {m}")
        print(f"... ({len(members)} membres au total)")

    def ask_new_member_data(self):
        print("\n=== Ajouter un nouveau membre ===")
        student_id = input("ID Étudiant : ").strip()
        family_name = input("Nom : ").strip()
        first_name = input("Prénom : ").strip()
        email = input("Email : ").strip()
        phone = input("Téléphone : ").strip()
        address = input("Adresse : ").strip()
        join_date = input("Date d'adhésion (MM/JJ/YYYY) : ").strip()
        subscription_status = input("Statut (paid/pending) : ").strip().lower()

        return {
            "student_id": student_id,
            "family_name": family_name,
            "first_name": first_name,
            "email": email,
            "phone": phone,
            "address": address,
            "join_date": join_date,
            "subscription_status": subscription_status,
            "skills": "",
            "interests": ""
        }

    def ask_member_id(self):
        return input("\nEntrez l'ID du membre : ").strip()

    def ask_skill_name(self):
        print("\n=== Recherche par compétence ===")
        return input("Entrez le nom de la compétence : ").strip()

    def ask_update_data(self, member):
        print("\n=== Modifier les informations du membre ===")
        print("Laisser vide pour garder la valeur actuelle.\n")

        member.family_name = input(f"Nom ({member.family_name}) : ").strip() or member.family_name
        member.first_name = input(f"Prénom ({member.first_name}) : ").strip() or member.first_name
        member.email = input(f"Email ({member.email}) : ").strip() or member.email
        member.phone = input(f"Téléphone ({member.phone}) : ").strip() or member.phone
        member.address = input(f"Adresse ({member.address}) : ").strip() or member.address
        member.subscription_status = input(f"Statut ({member.subscription_status}) : ").strip().lower() or member.subscription_status
        
        return member

    def display_search_results(self, results):
        if not results:
            print("\n[Aucun membre n'a cette compétence]")
        else:
            print("\n=== Membres trouvés ===")
            for m in results:
                print(f"- {m}")
