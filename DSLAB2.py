class RecursionMethod:
    """
    A class that encapsulates the prefix to postfix conversion method using recursion.
    """

    def prefix_to_postfix_rec(self, prefix: str, index: list[int]) -> tuple[str, bool]:
        """
        Recursively converts a prefix expression to a postfix expression.

        Args:
            prefix: The prefix expression to be converted.
            index: A list containing a single integer representing the current index in the prefix expression.

        Returns:
            A tuple containing the resulting postfix expression (if successful) and a boolean indicating success.
        """

        # If the index is out of range, return an empty string and False indicating failure.
        if index[0] >= len(prefix):
            return "", False

        # Get the next token in the prefix expression.
        token = prefix[index[0]]
        index[0] += 1

        # If the token is alphanumeric, return it and True indicating success.
        if token.isalnum():
            return token, True
        else:
            # Recursively get the postfix expressions for the left and right subtrees.
            left, success1 = self.prefix_to_postfix_rec(prefix, index)
            right, success2 = self.prefix_to_postfix_rec(prefix, index)

            # If both subtrees were successfully converted to postfix, combine them with the operator and return the
            # resulting postfix expression and True indicating success.
            if success1 and success2:
                return left + right + token, True
            else:
                # Otherwise, return an empty string and False indicating failure.
                return "", False

    def prefix_to_postfix(self, input_file: str, output_file: str) -> None:
        """
        Processes an input file containing prefix expressions and converts them to postfix expressions.

        Args:
            input_file: The path to the input file.
            output_file: The path to the output file.
        """

        # Print a message indicating which file is being processed.
        print(f"Processing file: {input_file}")

        # Open the input file and print its contents.
        with open(input_file, 'r') as f:
            print(f.read())

        # Open the input file again and create a list of non-blank lines.
        with open(input_file, 'r') as f:
            non_blank_lines = [line.strip() for line in f if line.strip()]

        # Initialize an empty list to store the results.
        results = []

        # Iterate over each non-blank line in the input file.
        for i, line in enumerate(non_blank_lines):
            # If the line is blank, skip it.
            if not line:
                continue

            # If there are any spaces in the line, it's an invalid expression, so append an error message to the
            # results and move on to the next line.
            if ' ' in line:
                results.append(f"Error [{i}]: Invalid expression - spaces not allowed")
                continue

            # Strip any trailing whitespace from the line and initialize an index indicating the current position in
            # the line.
            line = line.rstrip()
            index = [0]

            # Call the recursive prefix-to-postfix conversion method and store the result and success indicator.
            result, success = self.prefix_to_postfix_rec(line, index)

            # If the conversion was not successful, append an error message to the results indicating the reason for
            # failure.
            if not success or index[0] != len(line):
                if not success:
                    results.append(f"Error [{i}]: Invalid expression")
                elif index[0] < len(line):
                    results.append(f"Error [{i}]: Invalid expression - too many operands or operators")
                else:
                    token = line[index[0]-1]
                    if token in ('+', '-', '*', '/', '$', '^'):
                        results.append(f"Error [{i}]: Not enough operands for operator: {token}")
                    else:
                        results.append(f"Error [{i}]: Invalid expression - undefined operator: {token}")
            else:
                # Otherwise, append the resulting postfix expression to the results.
                results.append(result)

        # Open the output file and write the results to it.
        with open(output_file, 'w') as f:
            for result in results:
                f.write(result + '\n')

        # Print a message indicating where the results were written, and print the contents of the output file.
        print(f"Results written to file: {output_file}")
        with open(output_file, 'r') as f:
            print(f.read())


if __name__ == '__main__':
    # Create an instance of the class and call it with the required input and output files.
    method = RecursionMethod()
    method.prefix_to_postfix('Required_Input.txt', 'Required_Output.txt')
    method.prefix_to_postfix('Additional_Input.txt', 'Additional_Output.txt')





