import tkinter as tk
from tkinter import scrolledtext
import unicodedata

class MedicalDiagnoser:
    def __init__(self):
        # Symptom storage
        self.symptoms = set()
        # Simple rule-based mapping: frozenset of symptoms -> (diagnosis, explanation)
        self.rules = {
            frozenset(["febre", "tosse"]): (
                "Gripe",
                "A combinação de febre e tosse é típica de infecções virais como a gripe."
            ),
            frozenset(["dor de cabeça", "náusea"]): (
                "Enxaqueca",
                "Dor de cabeça intensa acompanhada de náusea pode indicar enxaqueca."
            ),
            frozenset(["dor no peito", "falta de ar"]): (
                "Possível problema cardíaco",
                "Dor no peito e dificuldade para respirar podem ser sinais de complicações cardíacas."
            ),
            frozenset(["dor abdominal", "diarreia"]): (
                "Gastroenterite",
                "Dor abdominal acompanhada de diarreia é comum em quadros de gastroenterite."
            ),
            frozenset(["dor de garganta", "febre"]): (
                "Amigdalite",
                "Dor de garganta com febre pode indicar uma inflamação nas amígdalas."
            ),
            frozenset(["espirros", "coriza"]): (
                "Rinite alérgica",
                "Espirros e coriza são sintomas típicos de uma crise de rinite alérgica."
            ),
            frozenset(["dor lombar", "formigamento na perna"]): (
                "Hérnia de disco",
                "Dor nas costas e formigamento podem indicar compressão nervosa como em hérnia de disco."
            ),
            frozenset(["tontura", "visão turva"]): (
                "Hipotensão",
                "Tontura acompanhada de visão turva pode ser um sinal de pressão baixa."
            ),
            frozenset(["sede excessiva", "urina frequente"]): (
                "Diabetes",
                "Sede exagerada e necessidade frequente de urinar são sintomas clássicos de diabetes."
            ),
            frozenset(["dor no corpo", "febre", "fraqueza"]): (
                "Dengue",
                "Dor no corpo, febre e fraqueza são sintomas sugestivos de dengue."
            ),
            frozenset(["suor excessivo", "palpitações"]): (
                "Ansiedade",
                "Palpitações e sudorese excessiva podem indicar crise de ansiedade."
            ),
            frozenset(["manchas vermelhas", "coceira"]): (
                "Alergia de contato",
                "Coceira com manchas vermelhas pode ser uma reação alérgica."
            ),
            frozenset(["dor nos olhos", "sensibilidade à luz"]): (
                "Conjuntivite",
                "Sensibilidade à luz com dor nos olhos pode indicar conjuntivite."
            ),
            frozenset(["fadiga", "perda de apetite"]): (
                "Anemia",
                "Fadiga persistente e perda de apetite podem ser sinais de anemia."
            ),
            frozenset(["enjoo", "tontura"]): (
                "Labirintite",
                "Tontura com enjoo pode indicar labirintite."
            ),
            frozenset(["dor ao urinar", "urina turva"]): (
                "Infecção urinária",
                "Dor e urina turva são sintomas comuns de infecção urinária."
            ),
            frozenset(["inchaço", "dor nas articulações"]): (
                "Artrite",
                "Dor e inchaço nas articulações podem indicar artrite."
            ),
            frozenset(["dificuldade para dormir", "irritabilidade"]): (
                "Insônia",
                "Dificuldade para dormir acompanhada de irritabilidade pode indicar insônia."
            ),
            frozenset(["dor no pescoço", "rigidez"]): (
                "Torcicolo",
                "Dor e rigidez no pescoço são comuns em torcicolo."
            ),
            frozenset(["falta de ar", "cansaço"]): (
                "Asma",
                "Cansaço com falta de ar pode indicar uma crise de asma."
            )
        }

    def normalize(self, text):
        text = text.strip().lower()
        text = ''.join(
            c for c in unicodedata.normalize('NFD', text)
            if unicodedata.category(c) != 'Mn'
        )
        return text

    def parse_input(self, text):
        text = self.normalize(text)
        keywords = [
            "febre", "tosse", "dor de cabeca", "dor no peito", "nausea", "falta de ar",
            "dor abdominal", "diarreia", "dor de garganta", "espirros", "coriza", "dor lombar",
            "formigamento na perna", "tontura", "visao turva", "sede excessiva", "urina frequente",
            "dor no corpo", "fraqueza", "suor excessivo", "palpitacoes", "manchas vermelhas",
            "coceira", "dor nos olhos", "sensibilidade a luz", "fadiga", "perda de apetite",
            "enjoo", "dor ao urinar", "urina turva", "inchaco", "dor nas articulacoes",
            "dificuldade para dormir", "irritabilidade", "dor no pescoco", "rigidez", "cansaco"
        ]
        found = []
        for kw in keywords:
            if kw in text:
                found.append(kw)
        return set(found)

    def update_symptoms(self, new_syms):
        self.symptoms.update(new_syms)

    def diagnose(self):
        for rule_syms, (diag, expl) in self.rules.items():
            if rule_syms.issubset(self.symptoms):
                return diag, expl
        return None, None

class DiagnoserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot de Diagnóstico Médico")
        self.diagnoser = MedicalDiagnoser()

        self.chat_area = scrolledtext.ScrolledText(root, state='disabled', wrap='word', width=60, height=20)
        self.chat_area.pack(padx=10, pady=10)

        self.user_entry = tk.Entry(root, width=50)
        self.user_entry.pack(side='left', padx=(10,0), pady=(0,10))
        self.user_entry.bind('<Return>', self.on_enter)

        self.send_btn = tk.Button(root, text="Enviar", command=self.on_enter)
        self.send_btn.pack(side='left', padx=10, pady=(0,10))

        self.post_message("Bot", "Olá! Por favor, descreva seus sintomas.")

    def post_message(self, sender, message):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

    def on_enter(self, event=None):
        user_text = self.user_entry.get().strip()
        if not user_text:
            return
        self.post_message("Você", user_text)
        self.user_entry.delete(0, tk.END)

        new_syms = self.diagnoser.parse_input(user_text)
        if new_syms:
            self.diagnoser.update_symptoms(new_syms)
            self.post_message("Bot", f"Entendi que você relata: {', '.join(new_syms)}.")

        diag, expl = self.diagnoser.diagnose()
        if diag:
            self.post_message("Bot", f"Possível diagnóstico: {diag}.\nExplicação: {expl}")
            self.diagnoser.symptoms.clear()
        else:
            self.post_message("Bot", "Continue descrevendo outros sintomas, por favor.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DiagnoserApp(root)
    root.mainloop()
