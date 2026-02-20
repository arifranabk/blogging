from pytrends.request import TrendReq
import logging
import pandas as pd
import time

class Brain:
    def __init__(self, hl='en-US', tz=360):
        self.pytrends = TrendReq(hl=hl, tz=tz)
        self.logger = logging.getLogger('SEO_Toolkit')

    def find_trending_topics(self, keyword, timeframe='today 12-m'):
        """
        Finds related queries and rising topics for a given keyword.
        """
        try:
            self.logger.info(f"Analyzing trends for keyword: {keyword}")
            self.pytrends.build_payload([keyword], cat=0, timeframe=timeframe)
            
            related_queries = self.pytrends.related_queries()
            if not related_queries:
                return []

            rising = related_queries[keyword]['rising']
            top = related_queries[keyword]['top']
            
            topics = []
            if rising is not None:
                topics.extend(rising['query'].tolist())
            if top is not None:
                topics.extend(top['query'].tolist())
            
            # Simple dedup
            return list(set(topics))[:10]
            
        except Exception as e:
            self.logger.error(f"Error fetching trends: {e}")
            return []

    def generate_content_plan(self, niche):
        """
        Generates a list of article titles based on trending topics.
        """
        topics = self.find_trending_topics(niche)
        plan = []
        for topic in topics:
            plan.append({
                'topic': topic,
                'title': f"The Ultimate Guide to {topic.title()}",
                'keywords': [topic, niche]
            })
        return plan
