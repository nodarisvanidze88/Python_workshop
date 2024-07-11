# # calculator v5.0
# def main():
#     result = get_expresion()
#     if result:
#         print(f"{result[0]}={result[1]}")
#     else:
#         print("Added wrong expresion")

# def get_expresion():
#     user = input("Expresion: ").strip()
#     try:
#         result = eval(user)
#         return user, result
#     except:
#         return False

# if __name__ == "__main__":
#     main()


# calculator upgrade v5.1
# def main():
#     result = get_expresion()
#     print(f"{result[0]}={result[1]}")

# def get_expresion():
#     while True:
#         user = input("Expresion: ").strip()
#         try:
#             result = eval(user)
#             return user, result
#         except:
#             print("Please add correct expresion.")
#             continue

# if __name__ == "__main__":
#     main()

# calculator upgrade v5.2
def main():
    result_data = []
    while True:
        result = get_expresion()
        print_result = f"{result[0]}={result[1]}"
        result_data.append(print_result)
        print(print_result)
        ask = input("Do you want to add another expresion? (Y/N)").upper()
        if ask == "Y":
            continue
        else:
            print("\n".join(result_data))
            break

def get_expresion():
    while True:
        user = input("Expresion: ").strip()
        try:
            result = eval(user)
            return user, result
        except:
            print("Please add correct expresion.")
            continue

if __name__ == "__main__":
    main()