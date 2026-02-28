import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def analyze_news_with_ia(articles: list[dict], query: str) -> str | None:

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    context = "\n".join(
        [
            f"- {article['title']}: {(article.get('description') or '')[:100]}..."
            for article in articles[:10]
        ]
    )

    prompt = f"""
        Basandose en estas noticias: {context}

        Pregunta: {query}

        Responde de forma concisa en español.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content