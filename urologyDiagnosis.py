from experta import *

class UrologyDiagnosis(KnowledgeEngine):
    """
    Expert system for diagnosing urological diseases.
    SIBYLA
    """
    user_name = ""
    diagnoses = []

    @DefFacts()
    def _initial_action(self):
        """We will start action.
        SIBYLA """
        yield Fact(action="start")

    @Rule(Fact(action='start'))
    def welcome_user(self):
        """We started giving the welcome to the user
        SIBYLA."""
        print("Welcome to our Expert System")
        print("I'm here to assist you with a preliminary diagnosis for the area of urology.")
        print("Please answer carefully.")
        self.declare(Fact(action="name"))

    @Rule(Fact(action='name'))
    def name(self):
        """Ask name.
        SIBYLA"""
        name = input("What's your name? ")
        self.user_name = name
        print(f"\nNice to meet you, {self.user_name}!")
        self.declare(Fact(name=name))
        self.declare(Fact(action="age"))

    @Rule(Fact(action='age'))
    def age(self):
        """Ask age
        SIBYLA."""
        print(f"Ok, {self.user_name}, now tell me your age.")
        age = input(" What's your age? ")
        self.declare(Fact(age=age))
        self.declare(Fact(action="gender"))

    @Rule(Fact(action='gender'))
    def gender(self):
        """Ask gender.
        SIBYLA"""
        print(f" Now, {self.user_name}, what´s your gender?")
        gender = input(" (male/female): ").lower()
        self.declare(Fact(gender=gender))
        self.declare(Fact(action="symptoms"))

    """Ofelia"""
    @Rule(Fact(action='symptoms'))
    def symptoms(self):
        """Now we are gonna do a little test about symptoms."""
        print(f"\n Alright {self.user_name}, now I'll ask you about some of your symptoms one by one.")
        symptoms = {}
        symptoms['pain_urination'] = input(" Do you experience pain during urination? (yes/no) ").lower()
        symptoms['blood_in_urine'] = input(" Do you see blood in your urine? (yes/no) ").lower()
        symptoms['frequent_urination'] = input(" Do you urinate more often than usual? (yes/no) ").lower()
        symptoms['fever'] = input(" Do you have fever? (yes/no) ").lower()
        symptoms['lower_back_pain'] = input(" Do you feel lower back pain? (yes/no) ").lower()
        symptoms['d_start_urine'] = input(" Difficulty starting urination? (yes/no) ").lower()
        symptoms['weak_urine_stream'] = input(" Weak or interrupted urine stream? (yes/no) ").lower()
        symptoms['testicular_swelling'] = input(" Any swelling in the testicle area? (yes/no) ").lower()
        symptoms['pain_ejaculation'] = input(" Pain during ejaculation? (yes/no) ").lower()
        symptoms['pelvic_pain'] = input(" Pelvic or bladder pain? (yes/no) ").lower()

        for key, value in symptoms.items():
            self.declare(Fact(**{key: value}))
        self.declare(Fact(action="diagnose"))