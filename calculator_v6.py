class Calculator:
    def __init__(self):
        self.expresion = ""
        self.final_result = []

    def get_input(self):
        self.expresion = input("Expresion: ")
    
    def calculate_expresion(self):
        try:
            result = eval(self.expresion)
            self.final_result.append(f"{self.expresion}={result}")
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def display_result(self):
        result = self.calculate_expresion()
        if "Error" not in result:
            print(f"{self.expresion}={result}")
        else:
            print(result)
            
    def display_final_result(self):
        print("\n".join(self.final_result))

def main():        
    calc = Calculator()
    while True:
        calc.get_input()
        calc.calculate_expresion()
        check = input("Do you want more?(Y/N) ").lower().strip()
        if check != "y":
            calc.display_final_result()
            break

main()