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

    """Helena"""
    @Rule(Fact(action='diagnose'),
          Fact(pain_urination="yes"),
          Fact(fever="yes"),
          Fact(blood_in_urine="yes"))
    def diagnose_uti(self):
        """Diagnosis: UTI."""
        self.diagnoses.append("- Urinary Tract Infection (UTI) [NHS: UTI]")

    @Rule(Fact(action='diagnose'),
          Fact(pain_urination="yes"),
          Fact(blood_in_urine="yes"),
          Fact(lower_back_pain="yes"))
    def diagnose_kstones(self):
        """Diagnosis: Kidney Stones."""
        self.diagnoses.append("- Kidney Stones [Mayo Clinic - Kidney Stones]")

    @Rule(Fact(action='diagnose'),
          Fact(frequent_urination="yes"),
          Fact(weak_urine_stream="yes"),
          Fact(d_start_urine="yes"))
    def diagnose_bph(self):
        """Diagnosis: BPH."""
        self.diagnoses.append("- Benign Prostatic Hyperplasia (BPH) [Mayo Clinic - BPH]")

    @Rule(Fact(action='diagnose'),
          Fact(blood_in_urine="yes"),
          Fact(pelvic_pain="yes"),
          Fact(fever="no"))
    def diagnose_bladderc(self):
        """Diagnosis: Bladder Cancer.
        sibyla"""
        self.diagnoses.append("- Bladder Cancer [Mayo clinic - Bladder Cancer]")

    @Rule(Fact(action='diagnose'),
          Fact(testicular_swelling="yes"),
          Fact(fever="no"))
    def diagnose_hydrocele(self):
        """Diagnosis: Hydrocele.
        sibyla"""
        self.diagnoses.append("- Hydrocele [Mayo Clinic - Hydrocele]")

    @Rule(Fact(action='diagnose'),
          Fact(testicular_swelling="yes"),
          Fact(fever="yes"))
    def diagnose_epididymitis(self):
        """Diagnosis: Epididymitis
        sibyla."""
        self.diagnoses.append("- Epididymitis [Mayo Clinic - Epididymitis]")

    @Rule(Fact(action='diagnose'),
          Fact(lower_back_pain="yes"),
          Fact(fever="yes"),
          Fact(blood_in_urine="yes"))
    def diagnose_pyelonephritis(self):
        """Diagnosis: Pyelonephritis."""
        self.diagnoses.append("- Kidney Infection (Pyelonephritis) [Mayo Clinic - Pyelonephritis]")

    @Rule(Fact(action='diagnose'),
          Fact(pelvic_pain="yes"),
          Fact(frequent_urination="yes"),
          Fact(pain_urination="yes"))
    def diagnose_interstitialc(self):
        """Diagnosis: Interstitial Cystitis."""
        self.diagnoses.append("- Interstitial Cystitis [NHS - Interstitial Cystitis]")

    """Helena"""
    @Rule(Fact(action='diagnose'),
          Fact(pain_ejaculation="yes"),
          Fact(pain_urination="yes"))
    def diagnose_prostatitis(self):
        """Diagnosis: Prostatitis."""
        self.diagnoses.append("- Prostatitis [NHS - Prostatitis]")


    """Armando"""    
    @Rule(Fact(action='diagnose'),
          Fact(frequent_urination="yes"),
          Fact(blood_in_urine="yes"),
          Fact(pelvic_pain="yes"))
    def diagnose_renalc(self):
        """Diagnosis: Renal Cancer."""
        self.diagnoses.append("- Renal Cancer [Mayo clinic - Kidney Cancer]")

    @Rule(Fact(action='diagnose'),
          Fact(lower_back_pain="yes"),
          Fact(weak_urine_stream="yes"))
    def diagnose_neurogenicb(self):
        """Diagnosis: Neurogenic Bladder."""
        self.diagnoses.append("- Neurogenic Bladder Disorder [NHS- Neurogenic Bladder]")

    @Rule(Fact(action='diagnose'),
          Fact(testicular_swelling="yes"),
          Fact(pain_ejaculation="yes"))
    def diagnose_varicocele(self):
        """Diagnosis: Varicocele."""
        self.diagnoses.append("- Varicocele [Mayo Clinic - Varicocele]")

    @Rule(Fact(action='diagnose'),
          salience=-10)
    def show_diagnoses(self):
        """Show all diagnoses after the test."""
        if self.diagnoses:
            print(f"\n Ok {self.user_name}, based on your symptoms, here are the possible diagnoses:")
            for d in self.diagnoses:
                print(d)
        else:
            print(f"\n {self.user_name}, you don't seem to be presenting symptoms for the conditions evaluated. Keep going.")

        print("\n Please consult a healthcare professional for a more detailed evaluation.")
        self.halt()

# Run the engine
engine = UrologyDiagnosis()
engine.reset()
engine.run()