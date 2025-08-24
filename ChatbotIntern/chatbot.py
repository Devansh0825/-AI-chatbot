import json
import os
from openai import OpenAI
from knowledge_base import InternshipKnowledgeBase

class InternshipChatbot:
    def __init__(self):
        # the newest OpenAI model is "gpt-5" which was released August 7, 2025.
        # do not change this unless explicitly requested by the user
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.knowledge_base = InternshipKnowledgeBase()
        self.conversation_context = []
        
    def get_response(self, user_message):
        """
        Process user message and return appropriate response
        """
        try:
            # Add user message to context
            self.conversation_context.append({"role": "user", "content": user_message})
            
            # Keep only last 10 messages for context
            if len(self.conversation_context) > 10:
                self.conversation_context = self.conversation_context[-10:]
            
            # Get intent and generate response
            intent_result = self._classify_intent(user_message)
            print(f"Intent result: {intent_result}")
            
            if intent_result.get('confidence', 0) > 0.7:
                # High confidence AI classification - use contextual response
                response = self._generate_contextual_response(user_message, intent_result)
            elif intent_result.get('confidence', 0) > 0 and intent_result.get('intent') != 'other':
                # Keyword-based classification detected an intent - use knowledge base
                response = self._generate_knowledge_base_response(intent_result.get('intent'), user_message)
            else:
                # No clear intent detected - use fallback
                response = self._generate_fallback_response(user_message)
            
            # Add bot response to context
            self.conversation_context.append({"role": "assistant", "content": response['response']})
            
            return response
            
        except Exception as e:
            return {
                'response': 'I apologize, but I encountered a technical issue. Please try rephrasing your question or contact support.',
                'intent': 'error',
                'confidence': 0.0
            }
    
    def _classify_intent(self, message):
        """
        Classify user intent using OpenAI or fallback to keyword matching
        """
        try:
            system_prompt = f"""
            You are an intent classifier for an internship FAQ chatbot. 
            Classify the user's message into one of these intents and provide a confidence score:
            
            Available intents:
            - application_process: Questions about how to apply for internships
            - requirements: Questions about eligibility, skills, or qualifications needed
            - timeline: Questions about application deadlines, program duration, start dates
            - compensation: Questions about salary, stipends, benefits
            - location: Questions about where internships are located, remote work
            - selection_process: Questions about interviews, assessments, selection criteria
            - program_details: Questions about what interns will do, projects, mentorship
            - company_culture: Questions about work environment, dress code, office culture
            - preparation: Questions about how to prepare for internships or interviews
            - general_info: General questions about internships
            - greeting: Greetings and conversation starters
            - goodbye: Farewell messages
            - other: Anything not related to internships
            
            Respond with JSON in this format:
            {{"intent": "intent_name", "confidence": 0.95, "entities": ["relevant", "keywords"]}}
            """
            
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ],
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            if not content:
                return self._classify_intent_fallback(message)
            return json.loads(content)
            
        except Exception as e:
            print(f"Intent classification error: {e}")
            # Use keyword-based fallback when OpenAI is unavailable
            return self._classify_intent_fallback(message)
    
    def _classify_intent_fallback(self, message):
        """
        Keyword-based intent classification when OpenAI is unavailable
        """
        message_lower = message.lower()
        
        # Define keyword mappings for each intent
        intent_keywords = {
            'application_process': ['apply', 'application', 'submit', 'resume', 'cv', 'cover letter', 'portfolio'],
            'requirements': ['requirements', 'qualifications', 'skills', 'eligible', 'gpa', 'prerequisites'],
            'timeline': ['when', 'deadline', 'timeline', 'duration', 'how long', 'start date', 'end date'],
            'compensation': ['pay', 'paid', 'salary', 'wage', 'money', 'compensation', 'benefits', 'stipend'],
            'location': ['where', 'location', 'remote', 'work from home', 'relocate', 'city', 'office'],
            'selection_process': ['interview', 'selection', 'process', 'chosen', 'assessment', 'test'],
            'program_details': ['what do', 'responsibilities', 'tasks', 'projects', 'mentor', 'training'],
            'company_culture': ['culture', 'environment', 'dress code', 'workplace', 'team'],
            'preparation': ['prepare', 'ready', 'tips', 'advice', 'how to'],
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon'],
            'goodbye': ['bye', 'goodbye', 'thank you', 'thanks', 'see you']
        }
        
        # Calculate scores for each intent
        best_intent = 'general_info'
        best_score = 0
        
        for intent, keywords in intent_keywords.items():
            score = sum(1 for keyword in keywords if keyword in message_lower)
            if score > best_score:
                best_score = score
                best_intent = intent
        
        # Set confidence based on keyword matches
        confidence = min(0.9, best_score * 0.3) if best_score > 0 else 0.1
        
        return {
            'intent': best_intent,
            'confidence': confidence,
            'entities': []
        }
    
    def _generate_contextual_response(self, message, intent_result):
        """
        Generate response based on classified intent and knowledge base
        """
        intent = intent_result.get('intent', 'general_info')
        
        # Get relevant FAQ from knowledge base
        relevant_faq = self.knowledge_base.get_faq_by_intent(intent)
        
        context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.conversation_context[-4:]])
        
        system_prompt = f"""
        You are a helpful internship advisor chatbot. Your goal is to provide accurate, helpful information about internships.
        
        Current conversation context:
        {context}
        
        User's intent: {intent}
        Confidence: {intent_result.get('confidence', 0)}
        
        Relevant FAQ information:
        {relevant_faq}
        
        Guidelines:
        1. Be friendly, professional, and helpful
        2. Provide specific, actionable advice when possible
        3. If you don't know something, be honest and suggest alternatives
        4. Keep responses concise but informative (2-3 sentences typically)
        5. Use the FAQ information as a reference but don't just copy it verbatim
        6. Maintain conversation flow and refer to previous context when relevant
        
        Respond naturally to the user's question about internships.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message}
                ]
            )
            
            return {
                'response': response.choices[0].message.content,
                'intent': intent,
                'confidence': intent_result.get('confidence', 0)
            }
            
        except Exception as e:
            print(f"Response generation error: {e}")
            # Use knowledge base directly when OpenAI is unavailable
            return self._generate_knowledge_base_response(intent, message)
    
    def _generate_fallback_response(self, message):
        """
        Generate fallback response for low confidence or error cases
        """
        fallback_responses = [
            "I'm not sure I understand your question completely. Could you please rephrase it or ask about specific aspects of internships like application process, requirements, or timelines?",
            "That's an interesting question! While I specialize in internship-related topics, I'd be happy to help if you could ask about internship applications, requirements, or program details.",
            "I want to make sure I give you the most accurate information. Could you please clarify what specific aspect of internships you'd like to know about?",
            "I'm here to help with internship-related questions. Feel free to ask about application processes, eligibility requirements, timelines, or any other internship topics!"
        ]
        
        import random
        return {
            'response': random.choice(fallback_responses),
            'intent': 'fallback',
            'confidence': 0.0
        }
    
    def _generate_knowledge_base_response(self, intent, message):
        """
        Generate response directly from knowledge base when OpenAI is unavailable
        """
        if intent in self.knowledge_base.faq_data:
            faq = self.knowledge_base.faq_data[intent]
            
            # For specific intents, provide the most relevant answer
            if intent == 'greeting':
                response = "Hello! I'm here to help you with internship-related questions. Feel free to ask about application processes, requirements, timelines, compensation, and more!"
            elif intent == 'goodbye':
                response = "Thank you for using the internship FAQ assistant! Best of luck with your internship search and applications!"
            else:
                # Use the first answer from the knowledge base
                response = faq['answers'][0]
            
            return {
                'response': response,
                'intent': intent,
                'confidence': 0.8
            }
        else:
            # Return general internship information
            return {
                'response': "I can help you with various internship topics including: application processes, eligibility requirements, timelines, compensation, interview processes, and program details. What specific aspect would you like to know about?",
                'intent': 'general_info',
                'confidence': 0.6
            }
    
    def reset_context(self):
        """
        Reset conversation context
        """
        self.conversation_context = []
