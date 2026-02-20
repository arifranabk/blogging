import os
import google.generativeai as genai
from openai import OpenAI
import logging

class Writer:
    def __init__(self):
        self.logger = logging.getLogger('SEO_Toolkit')
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        
        if self.gemini_api_key:
            genai.configure(api_key=self.gemini_api_key)
            self.model = genai.GenerativeModel('gemini-pro')
            self.provider = "gemini"
        elif self.openai_api_key:
            self.client = OpenAI(api_key=self.openai_api_key)
            self.provider = "openai"
        else:
            self.logger.warning("No LLM API keys found. Writer will run in simulation mode.")
            self.provider = "simulation"

    def generate_article(self, topic, keywords):
        """
        Generates a full SEO article based on the topic and keywords.
        """
        prompt = f"""
        Write a comprehensive, SEO-optimized article about "{topic}".
        Target Keywords: {', '.join(keywords)}
        
        Structure:
        1. Engaging H1 Title
        2. Introduction with hook
        3. Detailed Body with H2/H3 subheadings
        4. FAQ Section
        5. Conclusion
        
        Format: HTML (semantic tags only, no <html>/<body> wrappers)
        Tone: Professional, Authoritative, yet Accessible.
        Minimum Word Count: 1000 words.
        """

        self.logger.info(f"Generating content for topic: {topic} using {self.provider}")

        if self.provider == "gemini":
            try:
                response = self.model.generate_content(prompt)
                return response.text
            except Exception as e:
                self.logger.error(f"Gemini generation failed: {e}")
                return self._simulation_content(topic)
                
        elif self.provider == "openai":
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are an expert SEO content writer."},
                        {"role": "user", "content": prompt}
                    ]
                )
                return response.choices[0].message.content
            except Exception as e:
                self.logger.error(f"OpenAI generation failed: {e}")
                return self._simulation_content(topic)
        
        else:
            return self._simulation_content(topic)

    def _simulation_content(self, topic):
        return f"""
        <h1>The Ultimate Guide to {topic.title()}</h1>
        <p>This is a simulated article. Please configure an LLM API Key to generate real content.</p>
        <h2>Introduction</h2>
        <p>Lorem ipsum dolor sit amet...</p>
        """
