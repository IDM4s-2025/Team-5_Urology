from experta import *
class UrologyDiagnosis(KnowledgeEngine):
    """
    Expert system for diagnosing urological diseases.
    Sibyla
    """
    user_name = ""
    diagnoses = []

    @DefFacts()
    def _initial_action(self):
        """We will start action."""
        yield Fact(action="start")

    @Rule(Fact(action='start'))
    def welcome_user(self):
        """We started giving the welcome to the user.
        Sibyla."""
        
        print("Welcome to our Expert System")
        print("I'm here to assist you with a preliminary diagnosis for the area of urology.")
        print("Please answer carefully.")
        self.declare(Fact(action="name"))

    @Rule(Fact(action='name'))
    def name(self):
        """Ask name.
        Sibyla """
        name = input("What's your name? ")
        self.user_name = name
        print(f"\nNice to meet you, {self.user_name}!")
        self.declare(Fact(name=name))
        self.declare(Fact(action="age"))

    @Rule(Fact(action='age'))
    def age(self):
        """Ask age.
        Sibyla"""
        print(f"Ok, {self.user_name}, now tell me your age.")
        age = input(" What's your age? ")
        self.declare(Fact(age=age))
        self.declare(Fact(action="gender"))

    @Rule(Fact(action='gender'))
    def gender(self):
        """Ask gender.
        Sibyla"""
        print(f" Now, {self.user_name}, what´s your gender?")
        gender = input(" (male/female): ").lower()
        self.declare(Fact(gender=gender))
        self.declare(Fact(action="symptoms"))