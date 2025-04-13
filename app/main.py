"""
Chatbot to answer questions about a PDF using LangChain and Ollama.
"""

from langchain.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def create_model():
    """Creates the LLM model and embeddings."""
    llm = Ollama(model='llama3')
    embeddings = OllamaEmbeddings(model='znbang/bge:small-en-v1.5-f32')
    return llm, embeddings


def load_and_prepare_retriever(pdf_path, embeddings):
    """Loads the PDF and creates the retriever with smaller chunks."""
    loader = PyPDFLoader(pdf_path)
    pages = loader.load_and_split()
    store = DocArrayInMemorySearch.from_documents(pages, embedding=embeddings)
    return store.as_retriever()


def create_prompt_template():
    """Creates the prompt template."""
    template = """
    Answer the question based only on the provided context, always in English.

    Context: {context}

    Question: {question}
    """
    return PromptTemplate.from_template(template)


def format_docs(docs):
    """Formats the documents into a single text."""
    return "\n\n".join(doc.page_content for doc in docs)


def build_chain(retriever, llm, prompt):
    """Builds the chain of operations."""
    return (
        {
            'context': retriever | format_docs,
            'question': RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )


def main():
    """Main function to run the chatbot."""
    try:
        # 1. Create the model and embeddings
        llm, embeddings = create_model()

        # 2. Load the PDF and prepare the retriever
        retriever = load_and_prepare_retriever('app/data/the_curious_fox.pdf', embeddings)

        # 3. Create the prompt template
        prompt = create_prompt_template()

        # 4. Build the chain of operations
        chain = build_chain(retriever, llm, prompt)

        # 5. Question and answer loop
        while True:
            question = input('What do you want to know about the document?\n')
            print()
            print(chain.invoke({'question': question}))
            print()
    except Exception as e:
        print(f"Error processing: {e}")


if __name__ == "__main__":
    main()
