# 🧠 InterviewBot

**InterviewBot** is an AI-powered virtual interviewer built with [Streamlit](https://streamlit.io) and [Ollama](https://ollama.com). It combines large language models, speech recognition, and text-to-speech to simulate dynamic interview conversations. Ideal for practicing interviews or building custom dialogue systems.


# Data Flow

![dfd](https://static.swimlanes.io/2e264bf3df9ef8fcdb1f90a09760ab94.png)

![QnA](https://static.swimlanes.io/06181cc7265a05098cc384f75f888640.png)
---

# Want to Support
[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/freeEngineer)

## ✨ Features

- 🎙️ **Speech-to-Text** using Whisper
- 🗣️ **Text-to-Speech** streaming with real-time feedback
- 🤖 **LLM-powered responses** using local models via Ollama (e.g., Mistral, LLaMA2)
- 👥 **Multi-agent architecture** for extensible dialogue
- ⚡ **Streamlit-based UI** for fast prototyping and interaction

---

## 🧰 Requirements
Make sure you have the following installed:

- Python 3.10.12 (via pyenv)
- Make

## ⚙️ Installation
### 1. Clone the repo

```bash
$ git clone https://github.com/yourusername/interviewbot.git
$ cd interviewbot
```

### 2. Set up Python environment and dependencies
```bash
$ make setup
```

### 3. Install Ollama and pull the model
```bash
$ make setup-ollama
```

### 4. Run the Streamlit app
```bash
$ make run-app
```

### 🛠 Available Make Commands
```bash
$ make setup           # Set up virtual environment and install Python dependencies
$ make setup-ollama    # Install Ollama and pull the default model
$ make run-app         # Run the Streamlit app
$ make stop-app        # Stop the Streamlit app
$ make clean           # Stop services and delete virtual environment
$ make help            # Display all available commands
```

## 🙋‍♂️ Contributing
*Contributions are welcome! Please fork the repository and submit a pull request.*

## 📬 Contact
*For questions or issues, please open an [issue](https://github.com/SinghJagpreet096/InterviewBot/issues) on GitHub.*

[![LinkedIn](https://img.icons8.com/color/48/000000/linkedin.png)](https://www.linkedin.com/in/singhjagpreet096/) [![Hugging Face](https://huggingface.co/front/assets/huggingface_logo-noborder.svg)](https://huggingface.co/singhjagpreet)
[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/freeEngineer)


