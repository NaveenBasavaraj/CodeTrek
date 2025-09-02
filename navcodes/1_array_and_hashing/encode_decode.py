class Crypto:
    def encode(self, words):
        encoded_str = ""
        for word in words:
            encoded_str += str(len(word)) + "#" + word
        return encoded_str 
    
    def decode(self, encoded_str):
        decoded_words = []
        i = 0

        while i < len(encoded_str):
            j = i
            while encoded_str[j] != "#":
                j += 1
            length = int(encoded_str[i:j])
            i = j + 1
            word = encoded_str[i:i+length]
            decoded_words.append(word)
            i += length

        return decoded_words


if __name__ == "__main__":
    crypto = Crypto()
    words = ["lint", "code", "love", "you"]
    encoded = crypto.encode(words)
    decoded = crypto.decode(encoded)
    print("Input:", words)
    print("Encoded:", encoded)
    print("Decoded:", decoded)
