# Hackmerlin.io Automated Puzzle Solver

An AI-powered automated puzzle solver for [hackmerlin.io](https://hackmerlin.io) using Browser Use and OpenAI's GPT-4o-mini.

## Features

- 🤖 Automated puzzle solving using AI
- 🌐 Browser automation with Browser Use
- 🧩 Handles various puzzle types (uppercase, one-token, yes/no, multiple choice)
- 🔄 Automatic retry on formatting errors
- 📊 Real-time step-by-step progress tracking

## Prerequisites

- Python 3.11 or higher
- OpenAI API key
- Modern web browser (Chrome/Chromium recommended)

## Setup

1. **Clone and navigate to the project:**
   ```bash
   cd Spearbit-Labs-Take-Home-Test
   ```

2. **Install the project in development mode:**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables:**
   ```bash
   # Create .env file from example
   cp .env.example .env
   
   # Edit .env file and add your OpenAI API key
   # OPENAI_API_KEY=your_actual_api_key_here
   ```

4. **Get your OpenAI API key:**
   - Visit [OpenAI Platform](https://platform.openai.com/api-keys)
   - Create a new API key
   - Add it to your `.env` file

## Usage

Run the automated puzzle solver:

```bash
python main.py
```

The script will:
1. Open https://hackmerlin.io in a browser
2. Start solving puzzles automatically
3. Display each step and observation in the console
4. Continue until interrupted or all puzzles are solved

## How It Works

The solver uses:
- **Browser Use**: For web automation and interaction
- **OpenAI GPT-4o-mini**: For puzzle analysis and decision making
- **System Prompt**: Guides the AI on puzzle-solving strategies

### Puzzle Types Handled

- ✅ Uppercase single-token answers
- ✅ Yes/No questions (YES/NO format)
- ✅ Multiple choice selections
- ✅ Mathematical problems
- ✅ Pattern recognition
- ✅ Format retry on errors

## Project Structure

```
.
├── main.py                 # Main solver script
├── pyproject.toml         # Project configuration
├── .env                   # Environment variables (create from .env.example)
├── prompts/
│   └── examples.md        # Puzzle examples and patterns
└── README.md              # This file
```

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not found"**
   - Make sure you've created a `.env` file with your API key
   - Check that the key is valid and has sufficient credits

2. **Browser doesn't open**
   - Ensure you have Chrome/Chromium installed
   - Check that no other browser automation is running

3. **Puzzle solving fails**
   - The AI might need to retry with different formatting
   - Check the console output for specific error messages

### Stopping the Solver

Press `Ctrl+C` to stop the solver at any time. The browser will be closed automatically.

## Development

To contribute or modify the solver:

1. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

2. Run code formatting:
   ```bash
   black .
   ```

3. Run linting:
   ```bash
   flake8 .
   ```

## License

This project is for educational and testing purposes.

## Disclaimer

This tool is designed for educational purposes and puzzle-solving practice. Please respect the terms of service of hackmerlin.io and use responsibly.