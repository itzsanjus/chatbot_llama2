# A QnA system for any PDF files using LLaMA 2


***The objective of the project is to develop a Question-Answering (QnA) system capable of extracting information from PDF files using LLaMA 2 (Language Learning for Machine-Assisted Modeling). This system aims to provide accurate answers to questions based on the context found within the PDF documents, enabling efficient information retrieval from textual resources.***
***
Requirements -

* PyPDF: Extract text and metadata from PDF documents.
* Langchain: Implement natural language processing pipelines for multilingual text.
* Accelerate: Utilize GPU acceleration for faster numerical computations.
* Bitsandbytes: For qunatization of the model.
* Transformers: Perform state-of-the-art natural language processing tasks.
* CTransformers: Utilize transformer-based models for machine translation tasks.
* Sentence Transformers: Generate dense vector representations for sentences and paragraphs.
* Faiss_cpu: Perform efficient similarity search and clustering on large-scale datasets.
* Chainlit: Build the UI.
***

## Installation

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/itzsanjus/chatbot.git
    cd chatbot
    ```

2. Create a Python virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the required language model (https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin) then move it to the directory and put pdf document inside the folder 'data'. Please refer to the Langchain documentation for specific instructions on how to download and set up the language model and vector store.

5. Set up the necessary paths and configurations in your project, including the `DB_FAISS_PATH` variable and other configurations as per your needs.

## Getting Started

To get started with the Llama2 ChatBot, you need to:

1. Set up your environment and install the required packages as described in the Installation section.

2. Configure your project by updating the `DB_FAISS_PATH` variable and any other custom configurations in the code.

3. Prepare the language model and data as per the Langchain documentation.

4. Start the bot by running the provided Python script or integrating it into your application.

## Usage

The Llama2 Chat Bot can be used for answering queries from uploaded PDF. To use the bot, you can follow these steps:

1. Start the bot by running the application or using the provided Python script.

2. Send a any query you want from the data to the bot.

3. The bot will provide a response based on the information available in its database.

4. If sources are found, they will be provided alongside the answer.

5. The bot can be customized to return specific information based on the query and context provided.
