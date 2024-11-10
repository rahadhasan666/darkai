import openai
import argparse

# Set up OpenAI API key (replace with your actual key)
openai.api_key = "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"

def main():
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="DarkAI - Universal Command Recognizer and AI Code Generator.")
    parser.add_argument("--command", "-c", help="Command for the AI to recognize and execute.", type=str)
    args = parser.parse_args()
    
    if args.command:
        interpret_command(args.command)
    else:
        print("No command provided. Use '--command' followed by a command or question for the AI to process.")

def interpret_command(command):
    # Construct a prompt for OpenAI to understand and respond to the command
    prompt = f"You are an expert AI that understands and generates code for any language. Respond appropriately to: {command}"
    
    # Make the API call to OpenAI's GPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    
    # Output the response
    print("\nAI Response:\n" + response.choices[0].text.strip())

if __name__ == "__main__":
    main()
