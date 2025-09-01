# Hackmerlin.io Automated Puzzle Solver

An AI-powered automated puzzle solver for [hackmerlin.io](https://hackmerlin.io) using Browser Use and OpenAI's GPT-4o-mini.

## ⚠️ Current Status

**Important Note**: The `browser-use` library currently has a bug in the `Agent` class (issue with `max_steps` parameter). This affects the full automation functionality.

**Workarounds Available**:
1. **Demo Mode** (`main.py`) - Shows the setup and browser initialization
2. **Working Solver** (`working_solver.py`) - Uses browser + OpenAI directly for puzzle solving
3. **Wait for Fix** - Monitor browser-use library updates for the Agent class fix

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

### Option 1: Demo Mode (Shows Setup)
```bash
python main.py
```
This demonstrates the project setup and browser initialization, but won't fully automate puzzle solving due to the library bug.

### Option 2: Working Puzzle Solver
```bash
python working_solver.py
```
This version works around the Agent class bug by using the browser directly with OpenAI integration for puzzle solving.

### Option 3: Full Automation (When Bug is Fixed)
Once the browser-use library fixes the Agent class bug, you can use the full automation by uncommenting the Agent code in `main.py`.

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
├── main.py                 # Main demo script (shows setup)
├── working_solver.py       # Working puzzle solver (bypasses Agent bug)
├── pyproject.toml         # Project configuration
├── .env                   # Environment variables (create from .env.example)
├── prompts/
│   └── examples.md        # Puzzle examples and patterns
└── README.md              # This file
```

## Troubleshooting

### Current Known Issues

1. **Agent Class Bug**: The `browser-use` Agent class has a `max_steps` parameter bug
   - **Status**: Known issue in library
   - **Workaround**: Use `working_solver.py` or wait for library update
   - **Tracking**: Monitor browser-use library releases

### Common Issues

1. **"OPENAI_API_KEY not found"**
   - Make sure you've created a `.env` file with your API key
   - Check that the key is valid and has sufficient credits

2. **Browser doesn't open**
   - Ensure you have Chrome/Chromium installed
   - Check that no other browser automation is running

3. **Agent initialization fails**
   - This is the known library bug
   - Use `working_solver.py` as an alternative

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

## Alternative Approaches

If you need full automation immediately, consider:

1. **Selenium + OpenAI**: Direct browser automation with Selenium
2. **Playwright + OpenAI**: Modern browser automation alternative
3. **Custom Browser Integration**: Build custom automation using browser-use's Browser class

## License

This project is for educational and testing purposes.

## Disclaimer

This tool is designed for educational purposes and puzzle-solving practice. Please respect the terms of service of hackmerlin.io and use responsibly.

## Contributing

If you find a solution to the Agent class bug or want to contribute:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request with your improvements