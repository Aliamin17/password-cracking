import hashlib
import time

class PasswordCracker:
    def __init__(self, dictionary_path):
        self.dictionary_path = dictionary_path
        self.digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['&', '=', '!', '?', '.', '~', '*', '^', '#', '$']
        self.load_dictionary()

    def load_dictionary(self):
        with open(self.dictionary_path, "r") as file:
            self.dictionary = [line.strip() for line in file]

    def generate_combinations(self, word):
        for i in range(len(word) + 1):
            for digit in self.digits:
                word_with_digit = word[:i] + digit + word[i:]
                for j in range(len(word_with_digit) + 1):
                    for symbol in self.symbols:
                        yield word_with_digit[:j] + symbol + word_with_digit[j:]

    def crack_password(self, hash_to_crack):
        attempts = 0
        start_time = time.time()
        for word in self.dictionary:
            for candidate in self.generate_combinations(word):
                attempts += 1
                if hashlib.sha256(candidate.encode()).hexdigest() == hash_to_crack:
                    end_time = time.time()
                    return candidate, attempts, end_time - start_time
        end_time = time.time()
        return None, attempts, end_time - start_time

if __name__ == "__main__":
    dictionary_path = "C:\\Users\\Aly Ameen\\Desktop\\dictionary.txt"
    cracker = PasswordCracker(dictionary_path)

    hash_to_crack = "bafdf277d45fb7faabf58f0911600b0f3cdac6ebbf28adaff92e7c0e4e4fb98a"  # Replace this with the actual hash
    cracked_password, attempts, duration = cracker.crack_password(hash_to_crack)

    if cracked_password:
        print(f"Cracked Password: {cracked_password}")
    else:
        print("Password could not be cracked.")
    print(f"Total Attempts: {attempts}")
    print(f"Time Taken: {duration:.2f} seconds")
