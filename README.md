# Research Helper Tool

This is a Streamlit-based tool that helps users understand complex research papers using AI. The app uses the Google Gemini 2.0 Flash model via LangChain to generate summaries of selected research papers in different styles and lengths.

## Features

- Choose from popular research papers:
  - Attention Is All You Need
  - BERT: Pre-training of Deep Bidirectional Transformers
  - GPT-3: Language Models are Few-Shot Learners
  - Diffusion Models Beat GAN on Image Synthesis

- Select explanation style:
  - Beginner-friendly
  - Technical
  - Code oriented
  - Mathematical

- Choose summary length:
  - Short (1–2 paragraphs)
  - Medium (3–5 paragraphs)
  - Long (detailed explanation)

The application uses a prompt template to format user input and generates accurate, structured responses based on the selected paper and options.

## Requirements

To run this project, you need:

- Python 3.x
- Streamlit
- LangChain
- langchain-google-genai
- python-dotenv

Install dependencies using:

```bash
pip install streamlit langchain langchain-google-genai python-dotenv
