def main():
    input_text = "xibu4xpset beesftt jt pvucpbse.hsje.sfkpjot"
    output_text = "".join([letter if letter in [' ', '.'] else chr(ord(letter) - 1) for letter in input_text])
    print(output_text)


if __name__ == "__main__":
    main()
