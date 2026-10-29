from data_analysis import incarca_date
from ai_agent import raspunde_la_intrebare

df = incarca_date("banking_data.csv")

print("=== AI BANKING ANALYST ===")
print("Scrie 'exit' pentru a inchide aplicatia.")

while True:
    intrebare = input("\nTu: ")

    if intrebare.lower() == "exit":
        print("AI Banking Analyst: La revedere!")
        break

    raspuns = raspunde_la_intrebare(intrebare, df)

    print("\nAI Banking Analyst:")
    print(raspuns)