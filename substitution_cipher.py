# sample cipher_text
cipher_text = "lm hcd jcce iy wriy hcd ri,a l. jlmap hcd’jj ijwihx ri,a vcbaz lm hcd jcce iy wriy hcd nc.’y ri,a l. jlmap hcd’jj .a,ab ri,a a.cdgrz"

#sample substitution cipher key value pair
substitution_dict = {'Letter': 'Substitution', 'a': 'i', 'b': 'f', 'c': 'q', 'd': 'n', 'e': 'a', 'f': 'm', 'g': 'g', 'h': 'r', 'i': 'l', 'j': 's', 'k': 'e', 'l': 'j', 'm': 'v', 'n': '.', 'o': 'c', 'p': '?', 'q': 't', 'r': 'b', 's': 'x', 't': 'y', 'u': 'd', 'v': ',', 'w': 'w', 'x': 'o', 'y': 'h', 'z': 'u', ';': ';', '?': 'k', ',': 'p', '.': 'z'}

#function to decrypt cipher text using substitution cipher when key values are given
def decrypt(cipher_text, substitution_dict):
    cipher_text = list(cipher_text)
    keys = list(substitution_dict.keys())
    values = list(substitution_dict.values())
    decrypted_letter = ""
    decrypted_message = []
    for i in cipher_text:
        if i in values:
            decrypted_letter = keys[values.index(i)]
        else:
            decrypted_letter = i
        decrypted_message.append(decrypted_letter)
    return print(''.join(decrypted_message))


if __name__ == "__main__":
    decrypt(cipher_text, substitution_dict)
